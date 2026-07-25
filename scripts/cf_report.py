#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cloudflare Web Analytics アクセスレポート

対象: Cloudflare Web Analytics に登録済みの全サイト（heli-coblog.com /
      notam.heli-coblog.com など）を自動検出して集計する。

使い方:
    python scripts/cf_report.py              # 直近4週の推移＋人気ページ＋流入元
    python scripts/cf_report.py --weeks 8    # 8週分の推移
    python scripts/cf_report.py --days 14    # 人気ページ/流入元の集計期間を14日に

    # 詳細レポート（デバイス／流入元／記事ランキング・既定30日）
    python scripts/cf_report.py --detail                     # 全サイト
    python scripts/cf_report.py --detail heli-coblog.com     # ブログのみ
    python scripts/cf_report.py --detail --detail-days 90    # 90日分

事前準備（1回だけ）:
    Cloudflare で「Account Analytics: 読み取り」権限の API トークンを発行し、
    シェルに設定する（wrangler のデプロイを壊さないため CLOUDFLARE_API_TOKEN
    という名前は使わないこと）:

        echo 'export CF_ANALYTICS_TOKEN="＜トークン＞"' >> ~/.zshrc && source ~/.zshrc

    ※ 値を貼るときに全角引用符（” ）が混入しないよう注意。

注意:
    数値は Cloudflare のサンプリング補正値。期間が長いほど丸めが粗くなる
    （日別はおおむね10単位）。傾向の把握用であって厳密な実数ではない。
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone

ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID", "2c7102fbb389f6ff0bb594b92f000838")
TOKEN = os.environ.get("CF_ANALYTICS_TOKEN", "")
GRAPHQL_URL = "https://api.cloudflare.com/client/v4/graphql"

# ホスト名 → 表示ラベル（未知のホストはそのまま表示）
LABELS = {
    "heli-coblog.com": "ブログ",
    "notam.heli-coblog.com": "NOTAM Map",
}


def die(msg: str) -> None:
    print(f"エラー: {msg}", file=sys.stderr)
    raise SystemExit(1)


def gql(query: str) -> dict:
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read())
    except urllib.error.HTTPError as e:
        die(f"HTTP {e.code}: {e.read().decode()[:300]}")
    except urllib.error.URLError as e:
        die(f"通信失敗: {e.reason}")
    if d.get("errors"):
        die("GraphQL: " + json.dumps(d["errors"][:2], ensure_ascii=False)[:400])
    accounts = d["data"]["viewer"]["accounts"]
    if not accounts:
        die(f"アカウント {ACCOUNT_ID} のデータが取得できません（トークンの権限を確認）")
    return accounts[0]


def iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def groups(since: datetime, until: datetime, dims: str, limit: int = 1000,
           host: str = "") -> list:
    host_filter = f', requestHost: "{host}"' if host else ""
    q = f'''query {{ viewer {{ accounts(filter: {{accountTag: "{ACCOUNT_ID}"}}) {{
      rumPageloadEventsAdaptiveGroups(
        filter: {{datetime_geq: "{iso(since)}", datetime_leq: "{iso(until)}"{host_filter}}}
        limit: {limit}
      ) {{ count sum {{ visits }} dimensions {{ {dims} }} }} }} }} }}'''
    return gql(q)["rumPageloadEventsAdaptiveGroups"]


def label_of(host: str) -> str:
    return LABELS.get(host, host)


def is_article(path: str) -> bool:
    """記事ページ（/blog/<slug>/）か。一覧・タグ・カテゴリ・特集は除く。"""
    return (path.startswith("/blog/") and path.count("/") == 3
            and not path.startswith(("/blog/page", "/blog/tag",
                                     "/blog/category", "/blog/series")))


def detail_report(host: str, days: int, now: datetime) -> None:
    """1サイトの詳細（デバイス・流入元・記事ランキング）"""
    since = now - timedelta(days=days)
    print("\n" + "=" * 62)
    print(f"■ 【{label_of(host)}】直近{days}日の詳細")
    print("=" * 62)

    # デバイス
    agg = defaultdict(int)
    for r in groups(since, now, "deviceType", host=host):
        agg[r["dimensions"]["deviceType"]] += r["count"]
    total = sum(agg.values()) or 1
    print("\n▼ デバイス")
    for k, v in sorted(agg.items(), key=lambda x: -x[1]):
        print(f"  {k:<10}{v:>7} PV ({v / total * 100:.0f}%)")

    # 流入元
    agg = defaultdict(int)
    for r in groups(since, now, "refererHost", host=host):
        agg[r["dimensions"]["refererHost"] or "(直接/不明)"] += r["count"]
    print("\n▼ 流入元 TOP10")
    for k, v in sorted(agg.items(), key=lambda x: -x[1])[:10]:
        print(f"  {v:>7} PV  {k}")

    # 記事ランキング（/blog/ 配下がある場合のみ）
    agg = defaultdict(int)
    for r in groups(since, now, "requestPath", host=host):
        p = r["dimensions"]["requestPath"]
        if is_article(p):
            agg[p] += r["count"]
    if agg:
        print("\n▼ 記事ランキング TOP15")
        for k, v in sorted(agg.items(), key=lambda x: -x[1])[:15]:
            print(f"  {v:>6} PV  {k}")
        print(f"  （記事ページ合計 {sum(agg.values())} PV / {len(agg)} 記事）")


def main() -> None:
    ap = argparse.ArgumentParser(description="Cloudflare Web Analytics レポート")
    ap.add_argument("--weeks", type=int, default=4, help="週次推移の週数（既定4）")
    ap.add_argument("--days", type=int, default=7, help="人気ページ/流入元の集計日数（既定7）")
    ap.add_argument("--detail", nargs="?", const="all", metavar="HOST",
                    help="詳細レポート（デバイス/流入元/記事ランキング）。"
                         "ホスト名指定で1サイトのみ、省略で全サイト")
    ap.add_argument("--detail-days", type=int, default=30,
                    help="詳細レポートの集計日数（既定30）")
    args = ap.parse_args()

    if not TOKEN:
        die("環境変数 CF_ANALYTICS_TOKEN が未設定です。ファイル冒頭の説明を参照してください。")

    now = datetime.now(timezone.utc)

    # 対象ホストを直近データから自動検出
    recent = groups(now - timedelta(days=args.weeks * 7), now, "requestHost")
    totals = defaultdict(int)
    for r in recent:
        totals[r["dimensions"]["requestHost"]] += r["count"]
    hosts = [h for h, _ in sorted(totals.items(), key=lambda x: -x[1])]
    if not hosts:
        die("対象期間にデータがありません。")

    # ── 詳細レポート（--detail 指定時はこれだけ出して終了）──
    if args.detail:
        targets = hosts if args.detail == "all" else [args.detail]
        unknown = [h for h in targets if h not in hosts]
        if unknown:
            die(f"ホスト {unknown[0]} のデータがありません。候補: {', '.join(hosts)}")
        for host in targets:
            detail_report(host, args.detail_days, now)
        print("\n※ 数値はCloudflareのサンプリング補正値。傾向把握用。")
        return

    # ── 週次推移 ──
    print("=" * 62)
    print(f"■ 週ごとの推移（直近{args.weeks}週・1週=7日）")
    print("=" * 62)
    weeks = []
    for w in range(args.weeks):
        end = now - timedelta(days=7 * w)
        start = end - timedelta(days=7)
        agg = defaultdict(lambda: [0, 0])
        for r in groups(start, end, "requestHost"):
            h = r["dimensions"]["requestHost"]
            agg[h][0] += r["count"]
            agg[h][1] += r["sum"]["visits"]
        weeks.append((start.date(), end.date(), agg))
    weeks.reverse()  # 古い→新しい

    for host in hosts:
        print(f"\n【{label_of(host)}】{host}")
        print(f"  {'期間':<26}{'PV':>8}{'訪問':>8}   前週比")
        prev = None
        for s, e, agg in weeks:
            pv, vs = agg.get(host, [0, 0])
            diff = "  —" if not prev else f"  {(vs - prev) / prev * 100:+.0f}%"
            print(f"  {str(s)}〜{str(e):<12}{pv:>8}{vs:>8}{diff:>8}")
            prev = vs

    since = now - timedelta(days=args.days)

    # ── 人気ページ ──
    print("\n" + "=" * 62)
    print(f"■ 直近{args.days}日 よく見られたページ TOP10")
    print("=" * 62)
    rows = groups(since, now, "requestHost requestPath")
    for host in hosts:
        hp = sorted((r for r in rows if r["dimensions"]["requestHost"] == host),
                    key=lambda r: -r["count"])
        print(f"\n【{label_of(host)}】")
        for r in hp[:10]:
            print(f"  {r['count']:>6} PV  {r['dimensions']['requestPath'][:52]}")
        if not hp:
            print("  （データなし）")

    # ── 流入元 ──
    print("\n" + "=" * 62)
    print(f"■ 直近{args.days}日 流入元 TOP8")
    print("=" * 62)
    rows = groups(since, now, "requestHost refererHost")
    for host in hosts:
        agg = defaultdict(int)
        for r in rows:
            if r["dimensions"]["requestHost"] != host:
                continue
            agg[r["dimensions"]["refererHost"] or "(直接/不明)"] += r["count"]
        print(f"\n【{label_of(host)}】")
        for ref, c in sorted(agg.items(), key=lambda x: -x[1])[:8]:
            print(f"  {c:>6} PV  {ref}")
        if not agg:
            print("  （データなし）")

    print("\n※ 数値はCloudflareのサンプリング補正値（期間が長いほど丸めが粗い）。傾向把握用。")


if __name__ == "__main__":
    main()

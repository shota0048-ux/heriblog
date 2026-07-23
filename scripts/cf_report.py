#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cloudflare Web Analytics アクセスレポート

対象: Cloudflare Web Analytics に登録済みの全サイト（heli-coblog.com /
      notam.heli-coblog.com など）を自動検出して集計する。

使い方:
    python scripts/cf_report.py              # 直近4週の推移＋人気ページ＋流入元
    python scripts/cf_report.py --weeks 8    # 8週分の推移
    python scripts/cf_report.py --days 14    # 人気ページ/流入元の集計期間を14日に

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


def groups(since: datetime, until: datetime, dims: str, limit: int = 1000) -> list:
    q = f'''query {{ viewer {{ accounts(filter: {{accountTag: "{ACCOUNT_ID}"}}) {{
      rumPageloadEventsAdaptiveGroups(
        filter: {{datetime_geq: "{iso(since)}", datetime_leq: "{iso(until)}"}}
        limit: {limit}
      ) {{ count sum {{ visits }} dimensions {{ {dims} }} }} }} }} }}'''
    return gql(q)["rumPageloadEventsAdaptiveGroups"]


def label_of(host: str) -> str:
    return LABELS.get(host, host)


def main() -> None:
    ap = argparse.ArgumentParser(description="Cloudflare Web Analytics レポート")
    ap.add_argument("--weeks", type=int, default=4, help="週次推移の週数（既定4）")
    ap.add_argument("--days", type=int, default=7, help="人気ページ/流入元の集計日数（既定7）")
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

---
title: 'AIC（航空情報サーキュラー）を日本語で一覧表示する機能を追加（NOTAM Map Japan）'
description: '国土交通省 SWIM が発行する AIC を日本語タイトルで検索・閲覧できるページを NOTAM Map Japan に追加しました。原文 PDF へワンクリックでアクセスできます。'
pubDate: '2026-06-02'
category: 'そのほか'
heroImage: '../../assets/posts/notam-map-aic-viewer-hero.jpg'
---

NOTAM Map Japan に **AIC（航空情報サーキュラー）の日本語一覧ページ**を追加しました。

👉 **[https://notam.heli-coblog.com/aic.html](https://notam.heli-coblog.com/aic.html)**

---

## なぜ作ったか

国土交通省 SWIM が発行する AIC（Aeronautical Information Circular）は、運航上知っておくべき注意喚起・運用変更などをまとめた重要な情報です。

ただ、AIS Japan / SWIM の AIP 閲覧サービスから見られる AIC は **すべて英語タイトル**。たとえばこんな具合です。

- `2020-007_9GHz AIRBORNE SYNTHETIC APERTURE RADAR NOTIFICATION.pdf`
- `2022-008_Exemption from equipping automatic ELT activated by impact.pdf`

英語で書かれているとパッと見て何のAICか分からず、毎回PDFを開いて中身を確認する必要がありました。

そこで、**現在発効中の AIC 41件すべて**に日本語タイトルを付けて、ブラウザで一覧表示できるようにしました。

---

## 主な機能

### 1. 日本語タイトル＋英語タイトル併記

各AICを、番号・日本語タイトル・英語タイトルのセットで表示します。

```
007/20  ← AICの番号
9GHz帯航空機搭載型合成開口レーダーシステムに関する注意喚起
9GHz AIRBORNE SYNTHETIC APERTURE RADAR NOTIFICATION
```

### 2. キーワード検索

タイトル・番号・概要から横断検索できます。

### 3. カテゴリ別フィルタ

- 試験電波
- 滑走路誤進入防止
- 経路変更
- チェックリスト
- 注意喚起
- その他

### 4. 年度別フィルタ

2009年〜2026年の全AICを年度ごとに絞り込み可能。

### 5. ワンクリックで原文PDF

各行をクリックすると、SWIM 上の原文 PDF が新規タブで開きます（SWIM へのログインが必要）。

---

## 使い方

1. [https://notam.heli-coblog.com/aic.html](https://notam.heli-coblog.com/aic.html) を開く
2. 検索バー / カテゴリ / 年度で絞り込み
3. 気になる AIC をクリック → 原文 PDF を SWIM で確認

NOTAM Map Japan のヘッダーにある「AIC」リンクからもアクセス可能です。

---

## 免責事項

本ページは参考情報です。**実際の運航判断には必ず原文 PDF と最新の NOTAM を確認してください。**

---

## 関連リンク

- [NOTAM Map Japan](https://notam.heli-coblog.com/) — 日本全国 NOTAM 地図
- [SWIM](https://web.swim.mlit.go.jp/) — 国土交通省 SWIM

---

### 関連記事

- [ヘリパイロットが毎日使うためにNOTAM地図サービスを作りました（無料・全国対応）](/blog/notam-map-service-2026/)
- [AIPの改訂が一目でわかる「AIS Review」——航空情報センターの広報誌を知っていますか](/blog/ais-review-aip-2026/)

---
title: 'FlightAwareの使い方——ADS-B Exchangeが「機体」を見る道具なら、こちらは「便」を見る道具'
description: '同じADS-Bを使っていても、FlightAwareはADS-B Exchangeとは設計が違います。27言語に日本語があり、ゲート出発・離陸・着陸・ゲート到着の4つの時刻まで出る一方、機体登録番号は月99.95ドルのプラン扱い。日本は「二次サービスエリア」で、受信機を立ててフィードすれば有料プランが無料になります。5つの入口、追跡ログの読み方、日本語表示だと列が1つ消えること、東京周辺のヘリコプターが実際どこまで映るかを、実機の画面で確かめました。'
pubDate: '2026-09-22'
category: '基礎知識'
tags: ['航空安全']
heroImage: '../../assets/posts/flightaware-guide-hero.jpg'
---

「ADS-B Exchangeのようなサイトを見つけた」という形で**FlightAware**を教えてもらいました。

たしかに同じADS-Bを見ています。ただ、実際に触ってみると**設計思想がかなり違う**ことが分かりました。ひとことで言うとこうです。

> [ADS-B Exchange](/blog/adsbexchange-guide-2026/)は<strong>「機体」を見る道具</strong>。FlightAwareは<strong>「便」を見る道具</strong>。

ADS-B Exchangeが得意なのは、IASや選択高度や風といった**その機体が今どう飛んでいるか**です。FlightAwareが得意なのは、ゲートを出た時刻・車輪が浮いた時刻・接地した時刻・ゲートに着いた時刻という**その便がどう運ばれたか**のほうでした。

以下、実際に操作しながら整理します。**ログインなしでどこまでできるか**を基準にしました。

---

## まず、日本語にする

FlightAwareは**27言語に対応していて、日本語があります**。ここは英語しかないADS-B Exchangeとの大きな違いです。

画面右上（または最下部）の言語メニューから「日本語」を選ぶか、最初から `ja.flightaware.com` を開けば日本語になります。

ただし、<strong>日本語にすると失うものもあります。</strong>これは後半で詳しく書きますが、先に結論だけ言っておきます。

> 日本語表示にすると、<strong>高度がメートル、速度がkm/hになり、追跡ログの列が1つ消えます。</strong>

読み物として使うなら日本語、**データとして読むなら English (USA)** ——という使い分けになります。

## 5つの入口

検索ボックスの左にあるプルダウンが、そのまま入口の種類です。「すべて／ルート／航空会社のフライト／プライベート便（機体登録番号）／空港」の5つ。

URLの形を覚えてしまうほうが速いので、並べておきます。

<div class="fa-entry-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 342" width="100%" role="img" aria-label="FlightAwareの5つの入口とURLの形">
<rect x="0" y="0" width="560" height="342" fill="#ffffff"/>
<text x="14" y="24" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">手元にある情報から、入口を選ぶ</text>
<text x="14" y="44" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">どれも ja.flightaware.com の後ろにつなげる。ログイン不要</text>
<rect x="14" y="64" width="150" height="40" rx="5" fill="#ffffff" stroke="#3a7ca5" stroke-width="1.4"/>
<text x="24" y="81" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#3a7ca5">便名がわかる</text>
<text x="24" y="96" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#4b5563">JAL905</text>
<path d="M168 84 L186 84" stroke="#d9d3c6" stroke-width="1.6"/>
<path d="M182 80 L188 84 L182 88 Z" fill="#d9d3c6"/>
<rect x="192" y="64" width="354" height="40" rx="5" fill="#fbfaf6" stroke="#e5e1d6" stroke-width="1"/>
<text x="202" y="89" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#1f2937">/live/flight/JAL905</text>
<rect x="14" y="116" width="150" height="40" rx="5" fill="#ffffff" stroke="#3a7ca5" stroke-width="1.4"/>
<text x="24" y="133" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#3a7ca5">機体記号がわかる</text>
<text x="24" y="148" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#4b5563">JA01MK</text>
<path d="M168 136 L186 136" stroke="#d9d3c6" stroke-width="1.6"/>
<path d="M182 132 L188 136 L182 140 Z" fill="#d9d3c6"/>
<rect x="192" y="116" width="354" height="40" rx="5" fill="#fbfaf6" stroke="#e5e1d6" stroke-width="1"/>
<text x="202" y="141" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#1f2937">/live/flight/JA01MK</text>
<rect x="14" y="168" width="150" height="40" rx="5" fill="#ffffff" stroke="#2a9d8f" stroke-width="1.4"/>
<text x="24" y="185" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#2a9d8f">空港を見たい</text>
<text x="24" y="200" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#4b5563">羽田</text>
<path d="M168 188 L186 188" stroke="#d9d3c6" stroke-width="1.6"/>
<path d="M182 184 L188 188 L182 192 Z" fill="#d9d3c6"/>
<rect x="192" y="168" width="354" height="40" rx="5" fill="#fbfaf6" stroke="#e5e1d6" stroke-width="1"/>
<text x="202" y="193" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#1f2937">/live/airport/RJTT</text>
<rect x="14" y="220" width="150" height="40" rx="5" fill="#ffffff" stroke="#2a9d8f" stroke-width="1.4"/>
<text x="24" y="237" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#2a9d8f">区間だけわかる</text>
<text x="24" y="252" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#4b5563">羽田→新千歳</text>
<path d="M168 240 L186 240" stroke="#d9d3c6" stroke-width="1.6"/>
<path d="M182 236 L188 240 L182 244 Z" fill="#d9d3c6"/>
<rect x="192" y="220" width="354" height="40" rx="5" fill="#fbfaf6" stroke="#e5e1d6" stroke-width="1"/>
<text x="202" y="245" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.6" fill="#1f2937">/live/findflight?origin=RJTT&amp;destination=RJCC</text>
<rect x="14" y="272" width="150" height="40" rx="5" fill="#ffffff" stroke="#a07000" stroke-width="1.4"/>
<text x="24" y="289" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#a07000">機種で探したい</text>
<text x="24" y="304" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#4b5563">EC145</text>
<path d="M168 292 L186 292" stroke="#d9d3c6" stroke-width="1.6"/>
<path d="M182 288 L188 292 L182 296 Z" fill="#d9d3c6"/>
<rect x="192" y="272" width="354" height="40" rx="5" fill="#fbfaf6" stroke="#e5e1d6" stroke-width="1"/>
<text x="202" y="297" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#1f2937">/live/aircrafttype/EC45</text>
</svg>
</div>

たとえば羽田を見たいなら `ja.flightaware.com/live/airport/RJTT` を直接開きます。**ICAOコード（RJTT）でもIATAコード（HND）でも通ります。**

空港ページは4つのブロックに分かれていて、これがよくできています。

| ブロック | 中身 |
|---|---|
| **到着** | もう着いた便 |
| **出発** | もう出た便 |
| **飛行中／到着予定** | 今こちらに向かっている便 |
| **出発予定** | これから出る便 |

羽田を開いた時点で、到着20件・出発20件がそれぞれ**JST表記**で並びます。時刻は自動で現地時間に直されるので、ここは楽です。

## フライトページで何が見えるか

便名で開いたページが、FlightAwareの本体です。JAL905（羽田→那覇）を例にすると、こう出ました。

| 項目 | 表示 |
|---|---|
| ゲート出発 | 08時06分 JST（予定 08時05分） |
| **離陸** | 08時22分 JST（予定 08時15分） |
| 地上走行時間 | **16分** |
| **着陸** | 10時36分 JST（予定 10時29分） |
| ゲート到着 | 10時40分 JST（予定 10時40分） |
| 地上走行時間 | 4分 |
| 平均遅延 | 10-20分 |

**この4つの時刻が、FlightAwareのいちばんの持ち味です。**

ADS-B Exchangeにこれはありません。ADS-Bは「今どこにいるか」しか送っていないので、**ゲートを離れた時刻**は航空会社側のデータがないと分からない。FlightAwareは50を超える政府系の航空管制機関と、航空会社からのデータを取り込んでいるので、ここが埋まります。

ついでに使える導線が3つあります。

- **追跡ログを表示する**——後述。ここが本命
- **インバウンド便を追跡する**——この便に使う機材が、今どこから飛んできているか
- **HND-OKA間のすべての便**——同じ区間の他社便が一覧で出る

さらに下にスクロールすると、**過去の便が2週間分**並びます。「いつもは何分遅れているのか」を見るには十分です。

## ただし、機体登録番号は出ない

同じページの「航空機情報」には、こう書いてありました。

> 登録番号　**アカウントをアップグレードして機体番号を見る**

ここがFlightAwareの、いちばん驚いた点です。料金表を確認すると、**「表示されている機体登録番号」はEnterprise以上の機能**でした。

| | Basic | Premium + | Enterprise | Enterprise WX |
|---|---|---|---|---|
| 料金 | **無料** | $44.95/**月** | $99.95/**月** | $149.95/**月** |
| 機体登録番号 | — | — | ✓ | ✓ |
| ATCコールサイン | — | — | ✓ | ✓ |
| 過去のフライト履歴 | 3か月 | 5か月 | 8か月 | 8か月 |
| 保存できる航空機 | 5 | 無制限 | 無制限 | 無制限 |
| 広告なしの地図 | — | — | ✓ | ✓ |
| 航空チャート | — | ✓ | ✓ | ✓ |

**年額ではなく月額です。**[Flightradar24とADS-B Exchangeを比べた記事](/blog/adsbx-vs-fr24-2026/)では、Flightradar24のGoldが年34.99ドル、ADS-B Exchangeの広告非表示が年29.95ドルでした。桁がひとつ違います。

FlightAwareは**個人の趣味ユーザーではなく、運航会社やFBOを本来の客にしている**——料金表はそう言っています。

## 受信機を立てると、Enterpriseが無料になる

ただし、抜け道と言っていいものが公式に用意されています。ADS-Bのページにこう書いてありました。

> FlightAwareでデータを共有してくださっているユーザーは<strong>自動的にエンタープライズアカウントへの無料アップグレード条件を満たします。</strong>

Raspberry PiにUSBのADS-B受信機を挿して**PiAware**を動かし、データをFlightAwareに送る。それだけで、月99.95ドルのプランが無料になるという設計です。費用は「100米ドル／80ユーロ以下」と書かれています。

つまりFlightAwareの有料プランは、**お金で買うか、受信機で払うか**の二択になっています。これはこれで筋が通っていると思いました。

2026年9月22日時点の同社の受信網は、こう表示されていました。

- **45,362** サイト
- **38,631** 人の参加者
- **197** か国
- 330,802,484 位置／時間

Flightradar24が5万台超、ADS-B Exchangeが2.5万台超でしたから、ちょうど中間です。

## 追跡ログの読み方——ここが本命

フライトページの「追跡ログを表示する」を押すと、<strong>位置の生データが全部出ます。</strong>無料で、ログインも不要です。

列はこうなっています。

> 時間／緯度／経度／進路／ノット／km/h／メートル／レート

神戸→羽田のANA412（A321）で、実際に出た行を引きます。

```
月 18時28分:24	34.6224	135.1830	↙ 235°	173	320	518	614
月 18時46分:30	34.8488	136.6807	→ 95°	482	893	8,237	76
月 19時23分:23	35.5427	139.7813	↖ 329°	105	195	53	-86
```

離陸直後・巡航・接地直前です。1本の便で**135行**ありました。

### つまずくのはここ

ページ上部に、しれっとこう書いてあります。

> All times are in **EDT** time to prevent confusion due to time zone crossing.

<strong>時刻がすべて米国東部時間（EDT）です。</strong>フライトページはJSTで表示されるのに、追跡ログだけEDTに切り替わります。時差13時間。「18時28分」は日本時間の翌朝7時28分です。

各行の右端にJSTが併記される場面もありますが、**表の時刻そのものはEDT**なので、ここは意識しておかないと必ず混乱します。FlightAwareの説明では、無料アカウントを作れば自分のタイムゾーンを設定できるとのことでした。

## 言語を変えると、列が1つ増える

ここが今回いちばんの発見でした。**同じ追跡ログを English (USA) で開き直すと、表示が変わります。**

<div class="fa-locale-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 278" width="100%" role="img" aria-label="追跡ログの同じ１行を日本語表示と英語表示で比べた図">
<rect x="0" y="0" width="560" height="278" fill="#ffffff"/>
<text x="14" y="24" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">追跡ログの「同じ１行」を、言語を変えて見る</text>
<text x="14" y="44" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">ANA412　神戸→羽田　２０２６年９月２２日 18:46:30 EDT の行</text>
<rect x="192" y="60" width="164" height="26" rx="4" fill="#f1f5f8" stroke="#e5e1d6"/>
<text x="274" y="77" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#4b5563">日本語表示</text>
<rect x="360" y="60" width="186" height="26" rx="4" fill="#f7efe9" stroke="#b65a3b" stroke-width="1.2"/>
<text x="453" y="77" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#b65a3b">English (USA) 表示</text>
<line x1="14" y1="92" x2="546" y2="92" stroke="#e5e1d6" stroke-width="1"/>
<text x="18" y="116" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#14304a">高度</text>
<text x="196" y="116" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" fill="#1f2937">8,237 メートル</text>
<text x="364" y="116" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" font-weight="400" fill="#1f2937">27,025 feet</text>
<line x1="14" y1="130" x2="546" y2="130" stroke="#e5e1d6" stroke-width="1"/>
<text x="18" y="154" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#14304a">速度</text>
<text x="196" y="154" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" fill="#1f2937">482 ノット / 893 km/h</text>
<text x="364" y="154" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" font-weight="400" fill="#1f2937">482 kts / 555 mph</text>
<line x1="14" y1="168" x2="546" y2="168" stroke="#e5e1d6" stroke-width="1"/>
<text x="18" y="192" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#14304a">上昇率</text>
<text x="196" y="192" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" fill="#1f2937">76（m/min）</text>
<text x="364" y="192" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" font-weight="400" fill="#1f2937">250（ft/min）</text>
<line x1="14" y1="206" x2="546" y2="206" stroke="#e5e1d6" stroke-width="1"/>
<text x="18" y="230" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#14304a">受信した施設</text>
<text x="196" y="230" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" fill="#4b5563">列がない</text>
<text x="364" y="230" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" font-weight="700" fill="#b65a3b">FlightAware ADS-B (ITM / RJOO)</text>
<line x1="14" y1="244" x2="546" y2="244" stroke="#e5e1d6" stroke-width="1"/>
<text x="14" y="266" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#b65a3b">※ 英語表示にすると、列が１つ増える。どの受信機が拾った位置かが行ごとに分かる</text>
</svg>
</div>

高度がフィートになるのは想像がつきます。問題は**最後の行**です。

日本語表示には**存在しない列**が、英語表示では出てきます。**Reporting Facility**——その位置を**どの受信機が拾ったか**です。

```
Mon 06:46:00 PM  ...  26,750  1,075   FlightAware ADS-B (ITM / RJOO)
Mon 06:47:00 PM  ...  27,000    -25   FlightAware ADS-B (RJTS)
Mon 06:48:30 PM  ...  27,000          FlightAware ADS-B (NGO / RJGG)
```

ついでに、**メートル表示では気づけないこと**もあります。巡航に入りきったあたりの高度は、日本語表示だと「8,230メートル」と出ます。英語にすると**27,000 feet**。**FL270のきれいな数字**だったわけです。メートルに丸められると、高度指示との対応が読めなくなります。

### 受信機の分布が見える

この便（神戸→羽田、約1時間）の135行に出てきた受信施設を拾うと、**26か所**ありました。

> RJOY・RJOO・RJBB・RJBE・RJOS・RJBD・RJOT・RJNA・RJGG・RJTS・RJNH・RJNG・RJNS・RJTT・RJTF・RJAA・RJTY・RJTC・RJTI・RJTJ・RJTA・RJTK・RJTO・RJAH・RJTL・RJTR

阪神から東海、そして関東へ——**飛行に沿って受信機が入れ替わっていく様子**がそのまま見えます。

ただし読み方には注意が必要です。<strong>この括弧内は「その空港に受信機がある」という意味ではありません。</strong>FlightAwareは受信機の位置を「最寄りの場所」でしか表示しない方針を明記していて、統計ページにもこうあります。

> セキュリティおよびプライバシー保護の理由から、正確な位置は表示しておりません。

つまり `(RJTI)` は「東京ヘリポートに受信機がある」ではなく、<strong>「東京ヘリポートがいちばん近い場所にある誰かの受信機」</strong>です。横田・立川・入間・厚木・木更津・下総といった飛行場のコードが並んでいますが、**基地の設備ではなく、近所の個人宅である可能性のほうが高い**と考えるのが自然です。

## ライブマップ

`/live/map` を開くと世界地図が出ます。ただし、<strong>最初は必ず米国が中心で開きます。</strong>日本まで自分でドラッグするか、素直に空港ページから入るほうが速いです。

地図の左下にフィルタが4つあります。

| フィルタ | 中身 |
|---|---|
| **高度** | 0〜20,000（日本語表示だとメートル） |
| **速度** | km/h |
| **フライトタイプ** | 一般航空／ビジネス航空／商業航空／貨物航空会社／**MEDEVAC** |
| **機種** | ICAOの型式コードから選択（EC-175やAW189など回転翼もある） |

**MEDEVACだけを残せる**のは、この手のサイトでは珍しい部類です。ドクターヘリや救急搬送の動きを見たい人には効きます。

なお、引いた縮尺では「6069 flights decluttered (zoom in to see more)」と出て、<strong>機体が間引かれます。</strong>全部見たければズームインが必要です。

## 日本では、何がどこまで映るのか

ここからが正直な話です。<strong>FlightAwareにとって、日本は「二次サービスエリア」です。</strong>同社のFAQに、はっきりそう書いてあります。

> FlightAware's **primary service area** includes airspace operated by the United States (including Alaska, Hawaii, Puerto Rico, and Guam), portions of Central America, Canada, Australia, and New Zealand.
>
> FlightAware's **secondary service** covers scheduled major airline operations at any airport in the world.

羽田の空港ページにも、そのまま出ます。

> This airport is in FlightAware's **secondary service area.**

二次エリアで保証されているのは**定期便の出発・到着情報**までです。リアルタイムの位置は「ADS-Bのカバー範囲にいれば出るかもしれない」という扱いになります。

### 実際に試してみた

2026年9月22日の朝8時台、東京周辺（半径150海里）で**ADS-Bを出しているJA登録のヘリコプターが6機**いました。公開されているADS-Bの生フィードで確認した数字です。この6機をFlightAwareで1機ずつ引いてみました。

| 結果 | 機数 |
|---|---|
| **飛行中と表示された**（Position-Only Flight） | 2機 |
| **追跡データが見つからない** | 1機 |
| **ブロックされていた** | 3機 |

ブロックされていた機体は、こう表示されます。

> この航空機は、**所有者/運航者の要望により、公共における追跡ができません。**

同じ瞬間に、ADS-B Exchange側では高度も速度もそのまま出ていました。**[以前の記事](/blog/adsbx-vs-fr24-2026/)で書いた「フィルタするかどうか」の違いが、日本のヘリコプターでそのまま再現された**ことになります。

なお、なぜブロックされているのかは外からは分かりません。**本当に運航者が申請したのか、それとも既定でそうなっているのか**は、この画面からは判別できませんでした。ここは「そう表示された」以上のことは書けません。

### 「Position-Only Flight」という表示

映った2機には、**Position-Only Flight**という札がついていました。FAQの定義はこうです。

> A position-only flight is a flight for which FlightAware has not received a filed flight plan (for example an airline flight that doesn't report its flight schedule to FlightAware or **a VFR flight**).

**飛行計画が届いていない飛行**、という意味です。出発地も目的地も表示されず、代わりに「○○付近」と最寄りの地名が出ます。日本のVFRのヘリコプターは、ほぼ全部これになります。

逆に言えば、**ADS-Bさえ出していれば、飛行計画がなくても位置は出る**ということでもあります。

### 機種で引くと、もっとはっきりする

`/live/aircrafttype/EC45` で、いま飛んでいるEC145／BK117 C-2を一覧できます。日本が真っ昼間の時間帯に開いた結果がこれでした。

- 表示された機体は**全機がN登録**（米国）
- 出発地は `Indiana University Health West Hospital` `Wayne County` など、**米国のHEMS基地ばかり**
- `/live/aircrafttype/BK17` は **「該当便なし」**

米国のドクターヘリの動きを眺める用途なら、FlightAwareは相当に強い。<strong>日本のヘリコプターを追う用途には、そもそも向いていない。</strong>画面がそう言っています。

## 結局、どう使い分けるか

3つのサイトを並べるとこうなります。

| 見たいもの | 向いているサイト |
|---|---|
| 定期便の**遅れ・機材繰り・ゲート時刻** | **FlightAware** |
| 米国の**ヘリコプター・GA** | **FlightAware** |
| 日本の**ヘリコプター・自衛隊機・要人機** | **ADS-B Exchange** |
| IAS・TAS・風・外気温・**選択高度** | **ADS-B Exchange** |
| とりあえず**きれいな地図**で眺めたい | Flightradar24 |
| **位置の生データを行で読みたい** | FlightAware（追跡ログ） |

FlightAwareを「ADS-B Exchangeの代わり」として開くと、たぶん物足りません。**登録番号が有料で、日本のヘリはブロックされ、地図は米国で開く**——そこだけ見れば、日本のパイロットには向いていないサイトに見えます。

ただ、**追跡ログだけは別格**でした。1便あたり135行の位置・速度・高度・上昇率が、ログインなしで、CSVに貼れる形で出てきます。しかも**どの受信機が拾ったか**まで付いてくる。これはADS-B Exchangeの無料版にはない機能です。

自分の乗った便の降下プロファイルを後から確かめる、といった使い方なら、**English (USA) に切り替えたFlightAwareが、いちばん手っ取り早い**と思います。

---

### 関連記事

- [ADS-B Exchangeの使い方](/blog/adsbexchange-guide-2026/)
- [Flightradar24で年35ドルの機能が、ADS-B Exchangeでは無料](/blog/adsbx-vs-fr24-2026/)
- [Flightradar24はなぜ機体を映せるのか——ADS-BとMLATの仕組み](/blog/flight-tracking-mlat-2026/)
- [ADS-Bとは何か](/blog/adsb-basics-2026/)

### 出典

- FlightAware「よくある質問と回答」（サービスエリア、position-only flight、VFRの扱い、データ遅延）
- FlightAware「FlightAwareサブスクリプションの選択」（料金・機能比較）
- FlightAware「ADS-Bフライト追跡」および「FlightAware ADS-Bの統計」（受信網の規模、フィード提供者への無料アップグレード、受信機位置の非開示方針）
- 各画面は2026年9月22日に筆者が実際に開いて確認

ヒーロー画像：「Departures Board, Tokyo Haneda Airport (HND)」by Charles from Port Chester, New York（[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Departures_Board,_Tokyo_Haneda_Airport_(HND)_(34432949583).jpg) / CC BY 2.0）。本記事への掲載にあたり、切り抜きとリサイズを行いました。

---
title: 'Yahoo!天気の雨雲レーダーは何を見ているのか——1時間先で「別の製品」に切り替わる'
description: 'Yahoo!天気の雨雲レーダーは、Yahooが自前で観測しているわけではありません。気象庁が全国20か所に設置した気象レーダーのデータです。そしてスライダーを動かすと、1時間先を境に高解像度降水ナウキャストから降水短時間予報へ、見ているものが静かに入れ替わります。刻みが5分から1時間に変わるのがその境目。元データの正体、レーダーが見落とすもの、そして同じタイルを直接見る方法まで整理しました。'
pubDate: '2026-09-21'
category: '基礎知識'
tags: ['気象']
heroImage: '../../assets/posts/yahoo-rain-radar-hero.jpg'
---

いちばん多くの人が使っている雨雲の地図は、たぶんYahoo!天気の**雨雲レーダー**だと思います。

このブログでは[XRAIN](/blog/xrain-radar-2026/)や[SCW](/blog/scw-weather-2026/)、[キキクル](/blog/kikikuru-2026/)を扱ってきましたが、いちばん身近なこれを扱っていませんでした。**あれは何をもとに作られているのか。**

結論から書きます。<strong>気象庁のデータです。</strong>Yahooが自前でレーダーを回しているわけではありません。

そしてもうひとつ。実際に画面を触って気づいたのですが、<strong>スライダーは1時間先を境に、見ているものが別の製品に入れ替わります。</strong>画面上は連続して見えますが、境目があります。

---

## 観測しているのはYahooではない

Yahoo自身の「雨雲レーダーの仕組み」ページに明記されています。

> **気象庁が全国に設置した気象レーダー**のデータを利用

レーダーの所在地も列挙されています。**全国20か所**です。

| 地方 | 設置場所 |
|---|---|
| 北海道 | 釧路・札幌・函館 |
| 東北 | 秋田・仙台 |
| 関東甲信・北陸 | 東京・新潟・長野・福井 |
| 東海 | 静岡・名古屋 |
| 近畿・中国 | 大阪・松江・広島 |
| 四国・九州 | 室戸岬・福岡 |
| 南西諸島 | 種子島・名瀬・沖縄・石垣島 |

運営会社のLINEヤフーも、元データの正体をはっきり書いています。

> 気象庁の気象レーダーと**国土交通省のXバンドMPレーダー**を合成した**高解像度ナウキャスト**を気象庁が配信

国交省のXバンドMPレーダー——これは[XRAINの記事](/blog/xrain-radar-2026/)で扱ったあのレーダーです。**気象庁のCバンドとXRAINが合成されたもの**を、Yahooは受け取って表示している、という構造になります。

## スライダーの「刻み」を見ると、境目が分かる

ここからが、実際に画面を触って気づいたところです。

2026年9月20日19時45分の時点で、Web版のタイムラインに並んでいたコマを全部書き出すとこうなりました。

> 18:45 / 18:50 / 18:55 / 19:00 / 19:05 / 19:10 / 19:15 / 19:20 / 19:25 / 19:30 / 19:35 / 19:40 / <strong>現在（19:45）</strong> / 19:50 / 19:55 / 20:00 / 20:05 / 20:10 / 20:15 / 20:20 / 20:25 / 20:30 / 20:35 / 20:40 / <strong>20:45</strong> / **21:00** / **22:00** / **23:00** / **0:00** / **1:00**

気づきますか。<strong>20:45までは5分刻み、そこから急に1時間刻みになります。</strong>

<div class="yahoo-timeline-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="Yahoo雨雲レーダーのタイムライン図。現在から1時間先までは5分刻みの高解像度降水ナウキャスト、その先は1時間刻みの降水短時間予報に切り替わることを示す">
  <text x="280" y="26" text-anchor="middle" fill="#14304a" font-size="15" font-weight="bold">スライダーは、1時間先で「別の製品」に切り替わる</text>
  <text x="280" y="46" text-anchor="middle" fill="#4b5563" font-size="11.5">2026年9月20日19時45分時点、Yahoo!天気（Web版）で確認したコマの並び</text>
  <line x1="30" y1="132" x2="530" y2="132" stroke="#d9d3c6" stroke-width="2"/>
  <rect x="30" y="102" width="170" height="30" fill="#4b5563" fill-opacity="0.10"/>
  <rect x="200" y="102" width="130" height="30" fill="#3a7ca5" fill-opacity="0.16"/>
  <rect x="330" y="102" width="200" height="30" fill="#b65a3b" fill-opacity="0.14"/>
  <line x1="30.0" y1="126" x2="30.0" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="44.2" y1="126" x2="44.2" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="58.3" y1="126" x2="58.3" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="72.5" y1="126" x2="72.5" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="86.7" y1="126" x2="86.7" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="100.8" y1="126" x2="100.8" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="115.0" y1="126" x2="115.0" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="129.2" y1="126" x2="129.2" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="143.3" y1="126" x2="143.3" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="157.5" y1="126" x2="157.5" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="171.7" y1="126" x2="171.7" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="185.8" y1="126" x2="185.8" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="200.0" y1="126" x2="200.0" y2="138" stroke="#4b5563" stroke-width="1"/>
  <line x1="210.8" y1="126" x2="210.8" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="221.7" y1="126" x2="221.7" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="232.5" y1="126" x2="232.5" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="243.3" y1="126" x2="243.3" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="254.2" y1="126" x2="254.2" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="265.0" y1="126" x2="265.0" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="275.8" y1="126" x2="275.8" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="286.7" y1="126" x2="286.7" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="297.5" y1="126" x2="297.5" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="308.3" y1="126" x2="308.3" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="319.2" y1="126" x2="319.2" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="330.0" y1="126" x2="330.0" y2="138" stroke="#3a7ca5" stroke-width="1"/>
  <line x1="370.0" y1="123" x2="370.0" y2="141" stroke="#b65a3b" stroke-width="2"/>
  <line x1="410.0" y1="123" x2="410.0" y2="141" stroke="#b65a3b" stroke-width="2"/>
  <line x1="450.0" y1="123" x2="450.0" y2="141" stroke="#b65a3b" stroke-width="2"/>
  <line x1="490.0" y1="123" x2="490.0" y2="141" stroke="#b65a3b" stroke-width="2"/>
  <line x1="530.0" y1="123" x2="530.0" y2="141" stroke="#b65a3b" stroke-width="2"/>
  <line x1="200" y1="90" x2="200" y2="154" stroke="#14304a" stroke-width="2.5"/>
  <text x="200" y="84" text-anchor="middle" fill="#14304a" font-size="12" font-weight="bold">現在 19:45</text>
  <line x1="330" y1="90" x2="330" y2="154" stroke="#b65a3b" stroke-width="2.5" stroke-dasharray="5,3"/>
  <text x="330" y="84" text-anchor="middle" fill="#b65a3b" font-size="12" font-weight="bold">+1時間 20:45</text>
  <text x="115" y="170" text-anchor="middle" fill="#4b5563" font-size="11" font-weight="bold">過去1時間</text>
  <text x="115" y="185" text-anchor="middle" fill="#4b5563" font-size="10.5">5分刻み・12コマ（実況）</text>
  <text x="265" y="170" text-anchor="middle" fill="#3a7ca5" font-size="11" font-weight="bold">5分刻み</text>
  <text x="265" y="185" text-anchor="middle" fill="#3a7ca5" font-size="10.5">12コマ</text>
  <text x="430" y="170" text-anchor="middle" fill="#b65a3b" font-size="11" font-weight="bold">1時間刻み</text>
  <text x="430" y="185" text-anchor="middle" fill="#b65a3b" font-size="10.5">21:00 / 22:00 / 23:00 / 0:00 / 1:00</text>
  <rect x="200" y="204" width="130" height="64" rx="7" fill="#3a7ca5" fill-opacity="0.12" stroke="#3a7ca5" stroke-width="1.4"/>
  <text x="265" y="221" text-anchor="middle" fill="#3a7ca5" font-size="10.5" font-weight="bold">高解像度降水</text><text x="265" y="234" text-anchor="middle" fill="#3a7ca5" font-size="10.5" font-weight="bold">ナウキャスト</text>
  <text x="265" y="249" text-anchor="middle" fill="#3a7ca5" font-size="9.5">250m（〜30分）</text>
  <text x="265" y="261" text-anchor="middle" fill="#3a7ca5" font-size="9.5">1km（35〜60分）</text>
  <rect x="330" y="204" width="200" height="64" rx="7" fill="#b65a3b" fill-opacity="0.10" stroke="#b65a3b" stroke-width="1.4"/>
  <text x="430" y="226" text-anchor="middle" fill="#b65a3b" font-size="11.5" font-weight="bold">降水短時間予報</text>
  <text x="430" y="245" text-anchor="middle" fill="#b65a3b" font-size="10">1kmメッシュ・1時間降水量</text>
  <text x="430" y="260" text-anchor="middle" fill="#b65a3b" font-size="10">6時間先まで</text>
  <text x="280" y="320" text-anchor="middle" fill="#4b5563" font-size="10.5">※製品名はコマの刻みと先読み時間からの対応づけ。Yahooの画面に製品名の表示はありません。</text>
</svg>
</div>

この切り替わりは、UIの都合ではありません。**気象庁側の製品が変わっている**からです。

| | <strong>高解像度降水ナウキャスト</strong> | <strong>降水短時間予報</strong> |
|---|---|---|
| 先読み | **60分先まで** | **6時間先まで** |
| 解像度 | <strong>250mメッシュ（30分先まで）</strong><br>1kmメッシュ（35〜60分先） | 1kmメッシュ |
| 予測する量 | 降水強度 | **1時間降水量** |
| 手法 | 降水域を**3次元的に解析して追跡**→先になるほど**対流予測モデル**（気温・水蒸気から雨粒の発生・落下を計算）へ移行 | <strong>数値予報モデル（MSM・LFM）</strong>との合成 |
| 発表 | 5分ごと | 毎正時と30分 |

さらにその先、**7〜15時間先**は<strong>降水15時間予報</strong>（約5kmメッシュ、1時間間隔）という別製品になります。

### 何が違うのか、という話

<strong>ナウキャストは「いまある雨雲がどう動くか」を見ています。</strong>実際に観測されたエコーを3次元で追いかけて外挿する。だから直近は強い。

<strong>降水短時間予報は「これから雨雲がどこにできるか」を数値予報から持ってきています。</strong>いま何もないところに、あとから雨域が現れることがある。

**同じスライダーの上に並んでいますが、当たり方の性質が違います。**「1時間以内の雨雲の動き」と「3時間後に雨が降るか」は、別の問いに対する別の答えだ、と思っておいたほうがよさそうです。

## レーダーが見落とすもの——飛ぶ側に効く3つ

Yahooのページには、限界も正直に書かれています。ここが実は、我々にとっていちばん重要な部分でした。

**① 遠いほど、低いところが見えない**

> **距離が遠くなるにつれて低い高度の降水粒子を観測できなくなる**

レーダーは仰角を持って回るので、遠方では<strong>ビームが上空を通過してしまいます。</strong>地表付近だけで降っている雨は、遠ければ映りません。

<strong>低高度を飛ぶヘリにとって、これは決定的です。</strong>レーダー20か所から遠い山間部や離島で、**画面が白いのに実際は降っている**という状況は普通に起こり得ます。

[キキクルの記事](/blog/kikikuru-2026/)で「人家のない場所には色がつかない」と書きましたが、構造は似ています。<strong>白は「安全」ではなく「情報がない」</strong>かもしれない。

**② 山などの障害物**

> 山などの障害物の影響を受けることがある

電波が山に遮られれば、その裏側は見えません。**日本の地形でヘリが飛ぶ場所と、レーダーの死角は、かなり重なります。**

**③ 実際と違うエコーが出ることがある**

> 実際には降水がない場所でエコーが観測されたり、**実際の降水よりも強い降水を示すエコーが観測されたりする**

[キキクルの記事](/blog/kikikuru-2026/)でも触れた、レーダーの誤反射です。**狭い範囲だけ突出して濃い**ときは、これを疑う余地があります。

## 雨雲以外に重ねているもの

画面下の著作権表記を見ると、**雨雲以外のデータの出どころ**が分かります。

| 表記 | 何のデータか |
|---|---|
| © Weather Map Co., Ltd. | **天気予報のテキスト**（ウェザーマップ社） |
| © Franklin Japan Corporation | <strong>落雷</strong>（フランクリン・ジャパン社） |
| © LY Corporation | 地図・アプリ本体 |
| © Mapbox / © OpenStreetMap | ベース地図 |

つまり<strong>「雷」レイヤだけは気象庁ではなく民間の観測網</strong>です。フランクリン・ジャパンは全国に落雷位置標定システムを展開している会社で、気象庁の雷ナウキャストとは別系統のデータになります。

このほか、画面には**線状降水帯**のレイヤと、降水量の凡例（0〜1／1〜2／2〜4／4〜8／8〜12／12〜16／16〜24／24〜32／32〜40／40〜48／48〜56／56〜64／64〜80／80〜 mm/h）が用意されていました。**14段階**と、気象庁の標準的な配色より細かく刻まれています。

## 同じものを、直接見る方法

元が気象庁の配信タイルなので、**間に何も挟まずに見ることもできます。**

気象庁のタイルURLはこうです。

```
https://www.jma.go.jp/bosai/jmatile/data/nowc/{basetime}/none/{validtime}/surf/hrpns/{z}/{x}/{y}.png
```

`hrpns` は **H**igh **R**esolution **P**recipitation **N**owca**s**t——高解像度降水ナウキャストそのものです。時刻の一覧は `targetTimes_N1.json` / `targetTimes_N2.json` から取れて、`basetime` と `validtime` を比べれば実況か予測かも判別できます。

じつは筆者が作っている[NOTAM地図サービス](/blog/notam-map-service-2026/)の雨雲オーバーレイも、<strong>このタイルを直接叩いています。</strong>つまり<strong>Yahooと同じ元データを、間に何も挟まずに見ている</strong>ことになります。

違うのは**見せ方**だけです。

| | Yahoo!天気 | 気象庁タイルを直接 |
|---|---|---|
| 元データ（1時間以内） | **同じ** | **同じ** |
| 拡大 | 補間して滑らか | <strong>z10が配信上限</strong>。それ以上は粗くなる |
| 重ねられるもの | 落雷・線状降水帯・避難情報など | 自分で決められる |
| 先読み | 1時間先（5分刻み）＋6時間先（1時間刻み） | ナウキャストの範囲 |

<strong>「Yahooのほうが当たる／当たらない」ということは、1時間以内に限れば原理的にありません。</strong>見ているものが同一だからです。

## で、どう使い分けるか

飛ぶ側の整理として、こう考えています。

| 知りたいこと | 見るもの |
|---|---|
| **いま雨雲がどこにあり、30分後どこへ行くか** | Yahooでも気象庁でも同じ。**250mメッシュが効く範囲** |
| **午後に降り出すか** | スライダーの1時間刻みの側。ただし**別製品**だと意識して |
| **低高度の雨・山陰の雨** | レーダーだけで判断しない。[XRAIN](/blog/xrain-radar-2026/)や現地の[アメダス](/blog/amedas-2026/)、実測のMETARで補う |
| **面と時系列で前線を追う** | [下層悪天予想図](/blog/lowlevel-sigwx-2026/)、[SCW](/blog/scw-weather-2026/) |
| **災害の危険度** | 雨雲ではなく[キキクル](/blog/kikikuru-2026/) |

Yahooの雨雲レーダーは、**「いま・ここ」の雨雲を一番手早く見る道具**としては優秀です。ただしそれは**気象庁のタイルが優秀**なのであって、Yahooの予測が優秀なのではない——という理解をしておくと、限界の見積もりを間違えにくいと思います。

## まとめ

- Yahoo!天気の雨雲レーダーは、<strong>気象庁が全国20か所に設置した気象レーダーのデータ</strong>を使っている。**Yahooは観測していない。**
- 元データは、気象庁のレーダーと<strong>国土交通省のXバンドMPレーダー（XRAIN）を合成した高解像度降水ナウキャスト</strong>。
- <strong>スライダーは1時間先を境に、別の製品に切り替わる。</strong>5分刻み（〜1時間先）が**高解像度降水ナウキャスト**、1時間刻み（〜6時間先）が**降水短時間予報**。
- 両者は性質が違う。**ナウキャストは「いまある雨雲がどう動くか」、降水短時間予報は数値予報由来で「これからどこにできるか」。**
- 解像度は<strong>250mメッシュが30分先まで</strong>、35〜60分先は1kmメッシュ。さらに7〜15時間先は**降水15時間予報**（約5kmメッシュ）。
- レーダーの限界が3つ。<strong>①距離が遠くなるほど低い高度の降水粒子が見えない</strong>／②**山などの障害物**／③**実際にない・実際より強いエコー**が出ることがある。**低高度を飛ぶ側には①が効く。**
- 雨雲以外のレイヤは出どころが違う。<strong>落雷はフランクリン・ジャパン</strong>、天気予報テキストはウェザーマップ。
- 同じタイルは<strong>`.../surf/hrpns/{z}/{x}/{y}.png`</strong> で直接取得できる。筆者の[NOTAM地図](/blog/notam-map-service-2026/)も同じものを見ている。**配信上限はz10。**
- <strong>1時間以内に限れば、どのサービスで見ても中身は同じ。</strong>違うのは見せ方と、重ねられるものだけ。

---

### 関連記事

- [XRAIN（Xバンド気象レーダー）とは——250m・1分で「局所的な雨」を捉える防災の目](/blog/xrain-radar-2026/)
- [キキクルの「赤」と「紫」は、同じ基準を見ている——違うのは何時間先を見ているかだけ](/blog/kikikuru-2026/)
- [SCW（SUPERC WEATHER）の使い方——プロが使う天気予報ビジュアライザを徹底解説](/blog/scw-weather-2026/)
- [アメダスの「中身」を知る——全国1,300か所で測られているもの・測り方・意外な変化](/blog/amedas-2026/)
- [ヘリパイロットが毎日使うためにNOTAM地図サービスを作りました（無料・全国対応）](/blog/notam-map-service-2026/)

---

*本記事のタイムラインの内容は、2026年9月20日19時45分時点でYahoo!天気（Web版）の画面を筆者が確認したものです。<strong>製品名の対応づけは、コマの刻みと先読み時間からの推定であり、Yahooの画面に製品名の表示はありません。</strong>仕様は変更されることがあります。*

*ヒーロー画像はイメージです（航空機の窓に付いた雨滴）。"Rain drops on an aeroplane's window glass pane" by Chinmayee Mishra / [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Rain_drops_on_an_aeroplane%27s_window_glass_pane.jpg) / CC BY-SA 4.0（本記事への掲載にあたりリサイズを行いました）*

---

**出典**

- Yahoo!天気・災害「[雨雲レーダーの仕組み](https://weather.yahoo.co.jp/weather/promo/explanation.html)」
- Yahoo!天気・災害「[雨雲レーダー](https://weather.yahoo.co.jp/weather/zoomradar/)」（2026年9月20日確認）
- LINEヤフー株式会社「[なぜ雨雲の動きが分かる？「雨雲レーダー」の仕組み](https://www.lycorp.co.jp/ja/story/20240312/radar.html)」
- 気象庁「[高解像度降水ナウキャスト](https://www.jma.go.jp/jma/kishou/know/kurashi/highres_nowcast.html)」
- 気象庁「[今後の雨（降水短時間予報）](https://www.jma.go.jp/bosai/kaikotan/)」
- 気象業務支援センター「[解析雨量・降水短時間予報・降水15時間予報](https://www.jmbsc.or.jp/jp/online/file/f-online30400.html)」

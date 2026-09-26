---
title: 'MSMとGSM——モデルの出力は、そのままでは予報になっていない'
description: 'SCWやWindyで見ている「MSM」「GSM」とは何なのか。気象庁の現行仕様（GSM約13km・264時間、MSM 5km・78時間、LFMは1kmになりました）を整理したうえで、その先にある「ガイダンス」という一段を解説します。同じ5km格子の中で最大20.0mmと平均2.8mmが7倍違う話、発雷確率が実は60km四方の確率である話、降雪量が地上気温2℃以上で0cmになる話まで。気象庁の講習会資料と令和6年度の解説資料集で確認しました。'
pubDate: '2026-09-26'
category: '基礎知識'
tags: ['気象', '航空安全']
heroImage: '../../assets/posts/msm-gsm-guidance-hero.jpg'
---

SCWやWindyを開くと、画面のどこかに **MSM** とか **GSM** という文字があります。切り替えると絵が変わる。なんとなく「MSMのほうが細かい」くらいは分かる。

では、**あの数字はどこから来ているのか。**

気象庁の講習会資料を読んでいて、いちばん効いたのがここでした。

> 数値予報モデルの出力は、<strong>そのままでは予報になっていない。</strong>間に「ガイダンス」という一段がある。

しかもその一段には、知らないと読み違える仕掛けがいくつも入っていました。**同じ格子の中で「最大」と「平均」が7倍違う**とか、**「発雷確率30%」は実は60km四方の話**だとか。

気象庁の[講習会資料（令和元年10月）](https://www.jma.go.jp/jma/kishou/minkan/koushu191010/shiryou2.pdf)と、最新の**令和6年度 数値予報解説資料集**で確認しながら整理しました。

---

## まず、MSMとGSMとは何か

気象庁が回している数値予報モデルは、いまこうなっています。

| 略称 | 予報領域と格子間隔 | 予報期間 | 実行回数（初期値） |
|---|---|---|---|
| **LFM**（局地モデル） | 日本周辺 **1km** | 10時間 | 1日16回（下記以外の正時） |
| | | 18時間 | 1日8回（00,03,06,09,12,15,18,21UTC） |
| **MSM**（メソモデル） | 日本周辺 **5km** | 39時間 | 1日6回（03,06,09,15,18,21UTC） |
| | | **78時間** | 1日2回（00,12UTC） |
| **GSM**（全球モデル） | **地球全体 約13km** | 5.5日間（132時間） | 1日2回（06,18UTC） |
| | | **11日間（264時間）** | 1日2回（00,12UTC） |

<div class="nwp-model-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 282" width="100%" role="img" aria-label="LFM・MSM・GSMの予報期間と更新頃度の比較">
<rect x="0" y="0" width="560" height="282" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">3つのモデルは、射程と更新の速さが違う</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">気象庁の現行仕様。モデルごとに予報期間が2通りある</text>
<line x1="118" y1="58" x2="500" y2="58" stroke="#e5e1d6"/>
<line x1="118.0" y1="54" x2="118.0" y2="58" stroke="#d9d3c6"/>
<text x="118.0" y="50" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">0</text>
<line x1="194.4" y1="54" x2="194.4" y2="58" stroke="#d9d3c6"/>
<text x="194.4" y="50" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">24</text>
<line x1="270.8" y1="54" x2="270.8" y2="58" stroke="#d9d3c6"/>
<text x="270.8" y="50" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">48</text>
<line x1="347.2" y1="54" x2="347.2" y2="58" stroke="#d9d3c6"/>
<text x="347.2" y="50" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">72</text>
<line x1="423.6" y1="54" x2="423.6" y2="58" stroke="#d9d3c6"/>
<text x="423.6" y="50" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">96</text>
<line x1="500.0" y1="54" x2="500.0" y2="58" stroke="#d9d3c6"/>
<text x="500.0" y="50" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">120</text>
<text x="508" y="50" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#4b5563">時間先</text>
<text x="14" y="84" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="12" font-weight="700" fill="#a07000">LFM</text>
<text x="56" y="84" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#4b5563">1km</text>
<rect x="118.0" y="72" width="31.8" height="8" rx="2" fill="#a07000" opacity="0.9"/>
<rect x="118.0" y="83" width="57.3" height="8" rx="2" fill="#a07000" opacity="0.5"/>
<text x="118" y="108" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">10h × 1日16回 / 18h × 1日8回</text>
<text x="14" y="138" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="12" font-weight="700" fill="#3a7ca5">MSM</text>
<text x="56" y="138" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#4b5563">5km</text>
<rect x="118.0" y="126" width="124.2" height="8" rx="2" fill="#3a7ca5" opacity="0.9"/>
<rect x="118.0" y="137" width="248.3" height="8" rx="2" fill="#3a7ca5" opacity="0.5"/>
<text x="118" y="162" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">39h × 1日6回 / 78h × 1日2回</text>
<text x="14" y="192" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="12" font-weight="700" fill="#2a9d8f">GSM</text>
<text x="56" y="192" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#4b5563">約13km</text>
<rect x="118.0" y="180" width="382.0" height="8" rx="2" fill="#2a9d8f" opacity="0.9"/>
<path d="M500 184 l8 0" stroke="#2a9d8f" stroke-width="1.4" stroke-dasharray="3 2"/>
<text x="511" y="188" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" fill="#2a9d8f">264時間</text>
<text x="118" y="216" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">132h × 1日2回 / 264h × 1日2回</text>
<text x="14" y="270" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">※ GSMは最大264時間（11日）先まで。軸は120時間で切ってある</text>
</svg>
</div>

**いちばん大きな違いは、解像度ではなく「どこを計算しているか」です。**

- **GSM は地球全体**を計算します。だから長く先まで出せる。地球には外側がないので、境界から誤差が入ってこない
- **MSM と LFM は日本周辺だけ**を計算します。細かく計算できるかわりに、**領域の縁の値を外からもらう必要がある**。その外側をくれているのがGSMです

つまり <strong>MSM は GSM の上に乗っています。</strong>GSMが大きく外すと、MSMもつられます。この関係は、あとで出てくる「MSMを優先。ただし例外あり」という話に直結します。

そしてもうひとつ。<strong>航空気象情報には、LFM・MSM・GSM・MEPS（メソアンサンブル）の4つが全部使われています。</strong>気象庁の仕様表に、そのまま「航空気象情報」と書いてあります。

> 関連記事：[SCW（SUPERC WEATHER）の使い方](/blog/scw-weather-2026/)／[Windyの「Forecast Model」を使い分けよう](/blog/windy-forecast-models-2026/)

### ここは更新されています

以前ブログで「LFMは2km」「GSMは20kmメッシュ」と書いていましたが、**いまは違います。**

- **LFMは1km**になりました
- **MSMは00/12UTC初期値だけ78時間先**まで延びています（以前は39時間、その後51時間）
- **GSMモデル本体は約13km**です。「20km」は配信されるデータの格子であって、モデルの解像度ではありませんでした

## 「モデルの格子」と「配信される格子」は別物

ここがややこしいところです。**気象庁の中で計算している格子と、外に出てくるデータの格子は違います。**

| | モデル本体 | 配信されるGPV |
|---|---|---|
| **GSM** | 約13km | **全球域**：地上〜100hPa 0.5°×0.5°（720×361）／70〜10hPa 1.0°×1.0° |
| | | **日本域**：0.1°×0.125°（301×241） |
| **MSM** | 5km | **地上**：0.05°×0.0625°（505×481）・**1時間間隔** |
| | | **気圧面**：0.1°×0.125°（253×241）・**3時間間隔** |

日本域GSMの **0.1°×0.125°** はおよそ11km四方。**以前の 0.2°×0.25°（約20km）は、2024年9月17日18UTC初期値をもって配信終了**しています。「GSMは20km」という説明が古くなったのは、ここです。

MSMで押さえておきたいのは、**地上は1時間ごと、気圧面は3時間ごと**という差です。風や気温を上空で見たいとき、**MSMでも3時間刻みしか出てこない**のはこれが理由です。

## 本題——「ガイダンス」とは何か

気象庁の資料には、脚注でこう定義されています。

> ガイダンスは、数値予報の地上気温や降水量などの予測値を<strong>補正してその誤差を軽減</strong>したり、数値予報が<strong>直接は予測しない天気や発雷確率などを作成</strong>することによって予報作業を支援するプロダクト。

役割は2つです。

1. **モデルのクセを直す**——このモデルはこの地点で気温を1度低く出しがち、といった系統的なズレを統計で補正する
2. **モデルが出さないものを作る**——「天気（晴れ・曇り・雨）」も「発雷確率」も、モデルが直接計算しているわけではありません

**私たちが天気予報として目にしている数字のほとんどは、モデルの生の出力ではなく、このガイダンスを経たものです。**

### 現行のラインナップ

令和6年度の解説資料集に載っている一覧を、手法と逐次学習の有無で整理するとこうなります。

| ガイダンス | 作成対象 | 手法 | 逐次学習 |
|---|---|---|---|
| 平均降水量 | GSM 20km／MSM 5km格子 | **カルマンフィルタ** | あり |
| 降水確率 | 同上 | **カルマンフィルタ** | あり |
| 最大降水量 | 同上 | ニューラルネット（1・3時間）／線形重回帰（24時間） | **なし** |
| 大雨発生確率 | MSM 5km格子 | ロジスティック回帰 | **なし** |
| 降雪量 | 5km格子 | 平均降水量×雪水比 | なし |
| 時系列気温／最高・最低気温 | アメダス | **カルマンフィルタ** | あり |
| 定時風／最大風速 | アメダス | **カルマンフィルタ**＋頻度バイアス補正 | あり |
| 天気 | GSM 20km／MSM 5km格子 | 降水量＋日照率＋降水種別で判別 | — |
| 発雷確率 | **20km格子** | ロジスティック回帰 | **なし** |
| 最小湿度 | 気象官署 | ニューラルネット | あり |
| 視程 | GSM 20km／MSM 5km格子 | **消散係数による診断手法** | **なし** |

<strong>「逐次学習あり」の列が、そのままカルマンフィルタの列になっています。</strong>気温・風・降水量のように予測と実測の関係が素直な要素は、実況を使って係数を直し続けられる。一方、最大降水量・発雷・視程のように関係が素直でない要素は、**固定の式**です。使い込んでも賢くはなりません。

> 関連記事：[カルマンフィルタとは？——予報ガイダンスとGPSに共通する「予測と実測を混ぜる」技術](/blog/kalman-filter-2026/)

## 「最大」と「平均」は、7倍違う

ここが、今回いちばん驚いた話です。

降水量ガイダンスには **平均降水量** と **最大降水量** の2種類があります。名前が似ているので同じようなものだと思っていたのですが、**まったく別物**でした。

<div class="nwp-grid-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 326" width="100%" role="img" aria-label="5km格子の中の最大降水量と平均降水量の違い">
<rect x="0" y="0" width="560" height="326" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">同じ格子の中で、「最大」と「平均」は7倍違う</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">1つの5km格子の中にある、25個の約1km格子（数字は降水量 mm）</text>
<text x="14" y="58" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10" fill="#4b5563">※ 気象庁資料の例に合わせて筆者が作図した模式図</text>
<rect x="30" y="76" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="68" y="76" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="106" y="76" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="125.0" y="99.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="144" y="76" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="182" y="76" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="30" y="114" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="68" y="114" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="87.0" y="137.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="106" y="114" width="38" height="38" fill="#9dc0d6" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="125.0" y="137.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">5</text>
<rect x="144" y="114" width="38" height="38" fill="#9dc0d6" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="163.0" y="137.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">5</text>
<rect x="182" y="114" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="201.0" y="137.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="30" y="152" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="49.0" y="175.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="68" y="152" width="38" height="38" fill="#9dc0d6" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="87.0" y="175.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">5</text>
<rect x="106" y="152" width="38" height="38" fill="#14304a" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="125.0" y="175.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="700" fill="#ffffff">20</text>
<rect x="144" y="152" width="38" height="38" fill="#4f8fb5" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="163.0" y="175.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#ffffff">10</text>
<rect x="182" y="152" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="201.0" y="175.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="30" y="190" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="49.0" y="213.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="68" y="190" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="87.0" y="213.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="106" y="190" width="38" height="38" fill="#4f8fb5" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="125.0" y="213.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#ffffff">10</text>
<rect x="144" y="190" width="38" height="38" fill="#9dc0d6" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="163.0" y="213.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">5</text>
<rect x="182" y="190" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="201.0" y="213.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="30" y="228" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="68" y="228" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="87.0" y="251.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="106" y="228" width="38" height="38" fill="#dbe7ef" stroke="#d9d3c6" stroke-width="0.8"/>
<text x="125.0" y="251.0" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11" font-weight="400" fill="#1f2937">1</text>
<rect x="144" y="228" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="182" y="228" width="38" height="38" fill="#ffffff" stroke="#d9d3c6" stroke-width="0.8"/>
<rect x="30" y="76" width="190" height="190" fill="none" stroke="#14304a" stroke-width="2"/>
<text x="125.0" y="284" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10" fill="#14304a">1つの5km格子</text>
<rect x="254" y="82" width="196" height="58" rx="5" fill="#f7efe9" stroke="#b65a3b" stroke-width="1.3"/>
<text x="266" y="104" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#b65a3b">最大降水量</text>
<text x="266" y="128" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="20" font-weight="700" fill="#b65a3b">20.0 mm</text>
<rect x="254" y="156" width="196" height="58" rx="5" fill="#f1f5f8" stroke="#3a7ca5" stroke-width="1.3"/>
<text x="266" y="178" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#3a7ca5">平均降水量</text>
<text x="266" y="202" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="20" font-weight="700" fill="#3a7ca5">2.8 mm</text>
<text x="254" y="234" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" fill="#4b5563">70 ÷ 25 = 2.8</text>
</svg>
</div>

ひとつの5km格子の中には、約1km四方の格子が25個入っています。気象庁の資料が挙げている例だと、

- **最大降水量**＝25個の中でいちばん多い格子の値 ＝ **20.0mm**
- **平均降水量**＝25個の合計 ÷ 25 ＝ 70 ÷ 25 ＝ **2.8mm**

**同じ場所、同じ時間の話で、7倍違います。**

「3mm程度の雨」と読んで出かけたら、その5kmのどこかでは20mm降っている——そういう関係です。GSMなら、これが20km格子の中の話になります。

だから気象庁も、最大降水量ガイダンスの存在意義をこう書いています。

> 最大降水量ガイダンスは、平均降水量ガイダンスでは予測できない<strong>強雨を予測できる場合がある。</strong>

### ただし、最新版では定義が少し変わっています

令和6年度の資料を見ると、<strong>MSMの1時間・3時間最大降水量ガイダンスの目的変数は「5km格子を中心とする20km格子内の最大値」</strong>になっていました。2019年の資料の説明（5km格子の中の最大値）から広げられています。

作り方も具体的で、**ニューラルネットワークで「最大÷平均の比率」を予測し、それを平均降水量ガイダンスに掛ける**という構造です。24時間最大のほうは線形重回帰。

つまり——**平均降水量ガイダンスが外れていれば、最大降水量ガイダンスも一緒に外れます。**

## パイロットが引っかかりやすい4つ

<div class="nwp-which-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 326" width="100%" role="img" aria-label="項目ごとにMSMとGSMのどちらが精度が高いかを示す表">
<rect x="0" y="0" width="560" height="326" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">「とりあえずMSM」でいい。ただし例外がある</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">気象庁の統計検証（2018年の降水・風、冬季2か年分の降雪）による</text>
<line x1="14" y1="60" x2="546" y2="60" stroke="#e5e1d6"/>
<text x="18" y="82" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#1f2937">1時間・3時間最大降水量</text>
<rect x="300" y="68" width="52" height="20" rx="4" fill="#3a7ca5"/>
<text x="326" y="82" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#ffffff">MSM</text>
<text x="364" y="82" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">半日程度先までは特に高い</text>
<line x1="14" y1="106" x2="546" y2="106" stroke="#e5e1d6"/>
<text x="18" y="128" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#1f2937">24時間最大降水量　400mm/24h</text>
<rect x="300" y="114" width="52" height="20" rx="4" fill="#2a9d8f"/>
<text x="326" y="128" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#ffffff">GSM</text>
<text x="364" y="128" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">他のしきい値ではMSMが高い</text>
<line x1="14" y1="152" x2="546" y2="152" stroke="#e5e1d6"/>
<text x="18" y="174" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#1f2937">降雪量</text>
<rect x="300" y="160" width="52" height="20" rx="4" fill="#3a7ca5"/>
<text x="326" y="174" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#ffffff">MSM</text>
<text x="364" y="174" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">いずれの時間幅でも</text>
<line x1="14" y1="198" x2="546" y2="198" stroke="#e5e1d6"/>
<text x="18" y="220" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#1f2937">最大風速　～20m/s</text>
<rect x="300" y="206" width="52" height="20" rx="4" fill="#3a7ca5"/>
<text x="326" y="220" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#ffffff">MSM</text>
<text x="364" y="220" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">RMSEもMSMが小さい</text>
<line x1="14" y1="244" x2="546" y2="244" stroke="#e5e1d6"/>
<text x="18" y="266" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#1f2937">最大風速　25m/s～</text>
<rect x="300" y="252" width="52" height="20" rx="4" fill="#2a9d8f"/>
<text x="326" y="266" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#ffffff">GSM</text>
<text x="364" y="266" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">MSMは予測頻度が過小になりやすい</text>
<line x1="14" y1="290" x2="546" y2="290" stroke="#e5e1d6"/>
</svg>
</div>

実務で使う前に、定義を知らないと必ず読み違えるものを4つ挙げます。

### ① 発雷確率は「その場所」の確率ではない

発雷確率ガイダンスの目的変数は、こう書かれています。

> 対象とする20km格子を含む<strong>周囲9格子（60km四方）</strong>における前3時間の発雷の有無。

<strong>「発雷確率30%」は、その20km格子で雷が鳴る確率ではありません。</strong>60km四方のどこかで、3時間のうちに1回でも雷が観測される確率です。

しかも格子は **20km格子だけ**。MSMから作ったものでも20kmです。**雷の予測に5kmの細かさはない**、と思っておいたほうが安全です。

### ② 視程ガイダンスは「学習しない」

視程ガイダンスは**消散係数による診断手法**で、**逐次学習なし**。モデルの相対湿度・雲水量・降水量・風速から、決まった式で視程を計算しています。

目的変数は**前3時間の最小視程**。つまり「この3時間のうち、いちばん悪いとき」です。3時間ずっとその視程という意味ではありません。

GSMの視程ガイダンスは20km格子で、<strong>赤道〜65°N・東経100〜180°</strong>という広い範囲をカバーしています。洋上区間を含む計画では効きます。

### ③ 降雪量は、地上気温2℃で切られる

降雪量ガイダンスは「平均降水量ガイダンス × 雪水比」で作られますが、備考にこう書いてあります。

> 天気ガイダンス（降水種別）が「雨」の場合**または格子形式気温ガイダンスの地上気温が2℃以上の場合には降雪量を0cmとする。**

<strong>気温ガイダンスが2℃を超えていれば、機械的に0cmになります。</strong>気温ガイダンスが1℃ずれれば、降雪量の予測はゼロか否かで切り替わる。気象庁も「雪水の変換比率は0℃付近で大きく変化するため、**南岸低気圧事例など0℃付近で降雪が予測される事例では予測誤差が大きくなりやすい**」と明記しています。

### ④ 最大風速の「最大」は、10分値の最大

最大風速ガイダンスの目的変数は、

> <strong>前3時間の最大風速時（10分毎の観測から算出）</strong>の風速の東西・南北成分

です。<strong>突風（ガスト）ではありません。</strong>10分平均の風速の、3時間内でのいちばん強い時刻の値。定時風ガイダンス（毎正時の風）とは別物で、資料も「最大風速ガイダンスでは、定時風ガイダンスでは予測できない強風・暴風を予測できる場合がある」としています。

なお、頻度バイアス補正に使っている閾値は、定時風が **2.5 / 5.5 / 9.5 / 13.0 m/s**、最大風速が **3.0 / 7.0 / 11.0 / 15.0 m/s**。**このあたりの値の前後で、補正のかかり方が変わります。**

## 精度——MSMとGSM、どちらが当たるのか

気象庁が公表している統計検証を要約すると、**基本はMSMですが、きれいに例外があります。**

| 対象 | 精度が高いほう | 補足 |
|---|---|---|
| 1時間・3時間最大降水量 | **MSM** | 半日程度先までは特に高い |
| 24時間最大降水量（400mm/24h） | **GSM** | 他の閾値ではMSMが高い |
| 降雪量 | **MSM** | いずれの時間幅でも |
| 最大風速（〜20m/s） | **MSM** | RMSEもMSMのほうが小さい |
| 最大風速（25m/s〜） | **GSM** | MSMは予測頻度が過小になりやすい |

頻度のクセも公表されています。

- **1時間最大降水量は、80mm/h以上で観測より高い頻度で予測する傾向**（空振りに注意）
- 一方で1時間・3時間最大は全体としては**予測頻度が低め**（見逃しに注意）
- 24時間最大は、**大雨の予測頻度はおおむね適切**
- 降雪は、**6時間降雪量が全国的に過小**、**12時間・24時間は日本海側で過大**
- 最大風速は、**GSMが負バイアス、MSMが正バイアス**

## 使うときの落とし穴

気象庁自身が挙げている留意点が、そのまま実務のチェックリストになります。

### 「MSMを優先。ただし例外がある」

> MSMガイダンスの予報時間内ではGSMガイダンスよりもMSMガイダンスの利用を優先することを推奨。
> — MSMが予測する気象場と実況の比較や、MSMとGSMの予測を比較して、**MSMやMSMガイダンスの利用を控えるべきと判断した場合を除く**
> — 例）**MSMが予測する低気圧の過発達**

つまり、**MSMとGSMを見比べて、MSMだけが妙に荒れていたら疑え**ということです。細かいモデルほど、小さいものを大きく育ててしまうことがある。

### 夏の不安定性降水は苦手

> GSM・MSMガイダンスともに、<strong>夏季の不安定性の降水の予測は苦手。</strong>予測が実況に比べて過少になったり見逃すことが多い。<strong>予測をピンポイントで的中させることも難しい。</strong>利用時には降水予測の位置ずれも考慮する必要。

**夏の夕立を格子単位で信じてはいけない**、ということです。ヘリの運航でいちばん効くのはここだと思います。

### 台風の本体は、逆に過剰になる

> ガイダンスでは気象現象に応じた統計関係の場合分けは行っておらず、通常とは異なる気象場に対しては適切な予測ができない場合がある。
> — **台風本体による降水は、過剰な降水予測となる場合があるため留意**

### 記録を超える数字は、信じる対象が違う

これがいちばん重要な注意書きだと思いました。

> **過去の観測記録を超える、または大きく超える予測は、統計手法で適切に補正された予測ではない可能性が高く信頼性に欠ける。**
> — 大雨の可能性を示す**定性的な資料**として取り扱う必要

統計補正というのは、**過去にあった範囲を直す**技術です。範囲の外に出た数字は、補正が効いていない。「600mm/24hと出ている」を量として読むのではなく、**「とんでもないことになる兆候が出ている」という信号として読む**——そういう使い方をしろ、と書いてあります。

### 事例①：令和元年台風15号

- 9月6日9時初期値のGSMは、**東海地方への上陸**を予測。実際は**関東地方**に上陸
- 24時間最大降水量ガイダンスは**関東北部を中心に大雨**を予測。実際の大雨は**伊豆半島から千葉県**

<strong>モデルが台風の進路を外せば、ガイダンスも同じだけ外れます。</strong>気象庁は、24時間より先の雨量予測は幅を持って表現し、48時間より先では条件付きで——たとえば「**前線が南岸に停滞する場合には、24時間雨量は300〜500ミリ**」——という出し方をすると書いています。

### 事例②：2019年1月15日・宗谷岬

北海道北部を低気圧が通過し、宗谷岬で**32.2m/s**（観測史上1位）を観測した日。

- **GSM最大風速ガイダンス**：時間はずれたが、**32m/s程度を予測**
- **MSM最大風速ガイダンス**：**ピークの時間は合った**が、**27m/s程度と過小**

「どちらが当たったか」が<strong>値と時刻で割れています。</strong>強風のときは両方見る、というのはこういうことです。

## ヘリの運航で、どう効くか

整理するとこうなります。

<strong>前日〜当日朝の計画は、MSM（5km・1時間ごと）。</strong>ただし39時間先までで、00/12UTC初期値だけ78時間。3日先を見たいならGSMしかありません。

<strong>当日の細かい判断はLFM（1km）ですが、10〜18時間先まで。</strong>ブリーフィング時点では、もうLFMの守備範囲に入っていることが多いはずです。

**そして、数字の定義を思い出すこと。**

- 「降水量3mm」は**格子の平均**かもしれない。**最大は20mm**かもしれない
- 「発雷確率」は**60km四方**の話
- 「視程」は**前3時間の最小値**
- 「最大風速」は**10分平均の最大**で、ガストではない

どれも、資料の備考欄に小さく書いてあることです。でも、**その1行を知っているかどうかで、同じ数字の読み方が変わります。**

いちばん持ち帰りたいのは、気象庁自身の言葉です。

> 過去の観測記録を超える予測は、**統計手法で適切に補正された予測ではない可能性が高く信頼性に欠ける**——大雨の可能性を示す**定性的な資料**として取り扱う必要がある。

<strong>数字が大きいほど、数字として信じてはいけない。</strong>数値予報の読み方として、これはかなり効く一行だと思いました。

---

### 関連記事

- [飛行場時系列予報はどう作られる？——数値予報・ガイダンス・予報官の関係を解説](/blog/awfo-taf-timeseries-2026/)
- [カルマンフィルタとは？——予報ガイダンスとGPSに共通する「予測と実測を混ぜる」技術](/blog/kalman-filter-2026/)
- [SCW（SUPERC WEATHER）の使い方](/blog/scw-weather-2026/)
- [Windyの「Forecast Model」を使い分けよう](/blog/windy-forecast-models-2026/)
- [下層悪天予想図とは——SFC〜FL150を網羅する小型機・ヘリ運航者の必須資料](/blog/lowlevel-sigwx-2026/)

### 出典

- 気象庁予報部数値予報課「[GSM/MSMガイダンス（最大降水量、降雪量、最大風速ガイダンス）について](https://www.jma.go.jp/jma/kishou/minkan/koushu191010/shiryou2.pdf)」（気象・地震等の情報を扱う事業者等を対象とした講習会 第8回・令和元年10月10日）——ガイダンスの定義、最大／平均の例、統計検証、事例、利用上の留意点
- 気象庁「[令和6年度 数値予報解説資料集](https://www.jma.go.jp/jma/kishou/books/nwpkaisetu/R6/4_2.pdf)」第4.2節「ガイダンスの概要一覧表」——現行の各ガイダンスの作成対象・手法・予報期間・目的変数・備考
- 気象庁「[数値予報モデルの種類](https://www.jma.go.jp/jma/kishou/know/whitep/1-3-4.html)」——現行の予報領域・格子間隔・予報期間・実行回数
- 気象業務支援センター「[全球数値予報モデルGPV](https://www.jmbsc.or.jp/jp/online/file/f-online10100.html)」「[メソ数値予報モデルGPV](https://www.jmbsc.or.jp/jp/online/file/f-online10200.html)」——配信されるGPVの格子間隔・予報時間・初期時刻
- 数値予報課報告・別冊第64号「ガイダンスの解説」（平成30年3月）

*本記事は2026年9月26日時点の公開情報に基づきます。ガイダンスの仕様は毎年更新されるため、実務で使う際は最新の解説資料集をご確認ください。*

ヒーロー画像：「Discover Supercomputer 4」by NASA Goddard Space Flight Center（[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Discover_Supercomputer_4_(4641912697).jpg) / パブリックドメイン）。数値予報のイメージであり、気象庁の計算機ではありません。掲載にあたり切り抜きとリサイズを行いました。

---
title: 'Flightradar24で年35ドルの機能が、ADS-B Exchangeでは無料——2つの航空機追跡サービスを比較する'
description: '同じADS-Bを見ているのに、性格がまるで違う2つのサービス。受信機は5万台対2.5万台、Flightradar24は衛星ADS-Bやレーダーまで取り込む一方で、機体を非表示にする仕組みを持っています。IAS・TAS・風・外気温といったExtended Mode SはFR24ではGold（年34.99ドル）以上の機能ですが、ADS-B Exchangeでは無料。しかもQNHやFMSの選択高度、バンク角まで出ます。データソース、フィルタリング方針、料金、履歴、APIを並べて整理しました。'
pubDate: '2026-09-14'
category: '基礎知識'
tags: ['航空安全']
heroImage: '../../assets/posts/adsbx-vs-fr24-hero.jpg'
---

以前、[ADS-B Exchangeの使い方](/blog/adsbexchange-guide-2026/)と[Flightradar24がなぜ機体を映せるのか](/blog/flight-tracking-mlat-2026/)を、それぞれ別の記事で書きました。

「で、結局どっちを見ればいいのか」を書いていなかったので、今回は正面から比べます。

調べてみて、いちばん驚いたのはここでした。<strong>Flightradar24で年34.99ドル（Goldプラン）を払うと見えるようになる項目が、ADS-B Exchangeでは無料で見えます。</strong>しかも、ADS-B Exchangeのほうが項目数は多い。

---

## 先に結論——早見表

| | **Flightradar24** | **ADS-B Exchange** |
|---|---|---|
| 運営 | Flightradar24 AB（スウェーデン） | JETNET傘下（2023年1月買収） |
| 受信機数 | <strong>50,000台以上</strong> | 25,000台以上 |
| データ源 | ADS-B＋MLAT＋**衛星ADS-B**＋**レーダー**＋FLARM＋UAT＋ADS-C | ADS-B＋Mode S＋MLAT（UAT／ADS-R／TIS-B／ADS-Cも区別表示） |
| 機体の非表示 | <strong>あり</strong>（FAA LADD／運航者の申請） | <strong>なし</strong>（無検閲を掲げる） |
| 更新間隔 | — | <strong>500ミリ秒</strong> |
| 無料で見える情報 | 基本項目のみ | <strong>ほぼ全項目</strong> |
| IAS／TAS／風／OAT | **Gold（年34.99ドル）以上** | <strong>無料</strong> |
| QNH／FMS選択高度／バンク角 | 機能説明に記載なし | <strong>無料で表示</strong> |
| 有料プラン | Silver $14.99／Gold $34.99／Business $499.99（年額） | 広告非表示 $29.95/年（$2.99/月） |
| 履歴 | 7日／90日／365日／3年（プラン別） | **2020年3月以降**のリプレイ |
| 路線・便名・スケジュール | <strong>強い</strong>（150万機超のデータベース） | 弱い |
| 日本語 | **あり** | なし（英語のみ） |
| API | 別売（従量課金） | $10/月・10,000リクエスト（非商用） |

ざっくり言うと、こうなります。

- <strong>Flightradar24は「航空機を調べる」ためのサービス</strong>——どこから来て、どこへ行き、何という便なのか
- <strong>ADS-B Exchangeは「電波を見る」ためのサービス</strong>——その機体が実際に何を放送しているのか

## ① データソース——片方は雑食、片方は受信したものだけ

Flightradar24は、自社の説明によると**7大陸と宇宙に50,000台以上の受信機**を持ち、そこにいろいろなものを足し込んでいます。

- **ADS-B**（主力）
- **MLAT**（Mode Sしか積んでいない機体の位置を計算で出す）
- **衛星ADS-B**（地上局のない海上・極地）
- **レーダーデータ**（<strong>北米とオーストラリアのみ</strong>）
- **FLARM／Open Glider Network**（グライダー）
- **UAT**（主に米国の小型機、18,000ft未満）
- **ADS-C**（洋上などの衛星経由）

さらに、**150万機を超える機体データベース**と商用のフライトプラン・スケジュールデータを突き合わせています。「JL123便」と出てくるのは、この突き合わせの結果です。

ADS-B Exchangeは対照的に、**受信機が拾ったものを、拾ったまま**出すのが基本です。ADS-BとMode S、そしてMLAT。地図上では**ADS-B／UAT・ADS-R／MLAT／TIS-B／ADS-C／その他**を区別して表示・絞り込みできるようになっています。

**位置がどうやって得られたかが、機体ごとに明示される**わけです。[MLATで割り出した推定位置](/blog/flight-tracking-mlat-2026/)なのか、機体自身が放送したADS-Bなのかで、信頼度は当然違います。そこを曖昧にしない設計です。

ここが最初の性格の違いです。**Flightradar24は「空の全体像」を作りにいき、ADS-B Exchangeは「受信できた事実」を出す。**

## ② 見えない機体——フィルタリング方針

これが2つのサービスのいちばん有名な違いです。

<strong>Flightradar24には、機体を非表示にする仕組みがあります。</strong>同社が挙げている「機体が表示されない理由」は4つです。

1. ADS-Bトランスポンダを積んでいない
2. Mode Sはあるが、MLATのカバー範囲外
3. ADS-Bのカバー範囲外
4. <strong>所有者または運航者によってブロックされている</strong>

4番目がポイントです。米国ではFAAの**LADD**（Limiting Aircraft Data Displayed）という制度があり、機体の所有者が申請すると、データを受け取る事業者はその機体を公開表示できなくなります。

ADS-B Exchangeは、この方針を取りません。同社の説明はこうです。

> ADS-B Exchangeは、世界中の航空機の動きを、**検閲やフィルタリングなしに**透明な形で表示するグローバルプラットフォームです。

> 他の多くの追跡サービスと異なり、ADS-B Exchangeは「**上空に何がいるのか**」というシンプルな問いに答えることに集中しています。

軍用機も、要人輸送機も、そのまま出ます。ジャーナリズムや紛争監視、政府の説明責任の追跡といった用途でADS-B Exchangeが使われるのは、この一点によります。

<strong>「Flightradar24には映らないのに、実際には飛んでいる」という機体を確かめたいときは、ADS-B Exchangeを開く</strong>——これが最も実用的な使い分けです。

なお、2023年1月にADS-B ExchangeはJETNET（ビジネス航空のデータ企業）に買収されました。**方針が変わるのではないか**と当時ずいぶん言われましたが、2026年9月時点の公式サイトは依然として「検閲やフィルタリングなし」を掲げています。

## ③ 料金——ここが本題

### Flightradar24

年額での価格です（月払いだと割高になります）。

| プラン | 年額 | 主な内容 |
|---|---|---|
| **Free** | 0 | 広告あり、履歴**7日**、ブックマーク1、保存フィルタ1、3Dビュー3回、<strong>30分でタイムアウト</strong> |
| **Silver** | **$14.99** | 広告なし、履歴**90日**、ブックマーク10、フィルタ10、3Dビュー無制限、タイムアウトなし |
| **Gold** | **$34.99** | 履歴**365日**、ブックマーク25、<strong>ATC境界（FIR/UIR）</strong>、<strong>リスト表示</strong>、<strong>雲レイヤー</strong>、<strong>Extended Mode S</strong> |
| **Business** | **$499.99** | 履歴**3年**、滑走路データ、フリート表示、<strong>商用利用可</strong> |

無料版で地味に効くのが<strong>「30分でタイムアウト」</strong>です。Webの地図を開きっぱなしにして監視する、という使い方は無料版ではできません。

そして**商用利用はBusinessプランでのみ許可**されています。業務で使うなら年499.99ドル、という線引きです。

### ADS-B Exchange

こちらはシンプルです。

| | 内容 |
|---|---|
| **無料** | 地図・機体詳細・MLAT・フィルタなど、<strong>機能はほぼ全部使える</strong>。広告あり |
| **広告非表示** | <strong>$29.95/年</strong>（または$2.99/月）。広告が消え、**衛星を含むプレミアム地図レイヤー**と<strong>気象レーダー（米国・ドイツ）</strong>が付く |

<strong>有料にしても、見える情報は基本的に増えません。</strong>増えるのは地図の見やすさです。**情報へのアクセスと課金が切り離されている**——ここがFlightradar24との設計思想の違いです。

## ④ 情報の深さ——年34.99ドルの境目

ここが今回いちばん調べ甲斐のあったところです。

### Flightradar24の「Extended Mode S」はGold以上

機体がMode Sで放送する**拡張データ**（Extended Mode S、BDSレジスタ）を、Flightradar24も取り込んでいます。ただし表示は有料です。同社の説明はこうです。

> **GoldおよびBusinessプラン**の加入者は、Extended Mode Sデータと、FIR/UIRの位置を含む追加の機体情報に**独占的にアクセス**できます。

Goldで解放される項目は、

| 分類 | 項目 |
|---|---|
| **Speed** | Indicated Airspeed（IAS）／True Airspeed（TAS）／Mach |
| **Altitude** | GPS Altitude |
| **Weather** | Wind（風向・風速）／Outside Air Temperature（OAT） |
| そのほか | FIR／UIR |

これが<strong>年34.99ドル</strong>の側にあります。

### ADS-B Exchangeは、同じものが無料で、しかも多い

[以前の記事](/blog/adsbexchange-guide-2026/)で1機クリックして出た項目を整理しましたが、改めて並べると差がはっきりします。

| ADS-B Exchangeの表示項目 | Flightradar24 |
|---|---|
| Groundspeed／Baro. altitude／WGS84 altitude／Vert. Rate／Track | 無料で表示 |
| **IAS／TAS／Mach** | **Gold以上** |
| **風向・風速／TAT・OAT** | **Gold以上** |
| **GPS（幾何）高度** | **Gold以上** |
| <strong>QNH（機体が設定している高度計規正値）</strong> | 機能説明に記載なし |
| <strong>Sel. Alt.／Sel. Head.（FMSの選択高度・選択方位）</strong> | 機能説明に記載なし |
| <strong>True Heading／Magnetic Heading／Magnetic Decl.</strong> | 機能説明に記載なし |
| <strong>Roll（バンク角）／Track Rate</strong> | 機能説明に記載なし |
| <strong>NACp／SIL／NACv／NICbaro／RC（精度・完全性指標）</strong> | 機能説明に記載なし |
| <strong>Source（ADS-B/MLATの別）／RSSI／Msg. Rate／Receivers／Last Seen</strong> | データソース表示のみ |

いちばん実用的に効くのは、おそらく<strong>Sel. Alt.（選択高度）</strong>です。**その機体がオートパイロットに何ftをセットしているか**が見えるので、「いま降下中のこの機は、あとどこまで降りるつもりか」が読めます。**次に何をするつもりかが分かる**、という意味では、他のどの項目とも性質が違います。

**QNH**も同様で、その機体が設定している高度計規正値がそのまま出ます。

### ただし、出ないときは出ない

公平のために書いておくと、これらは<strong>機体が実際に放送していなければ表示されません</strong>。Flightradar24のフォーラムでも「IAS/TAS/Mach/風/気温がいつもN/A」という質問が繰り返し出ていて、モデレーターの回答は「**MLATや推定位置、衛星経由の機体ではExtended Mode Sは得られない**」というものでした。

これはADS-B Exchangeでも同じです。**受信機が拾えていない情報は、どちらのサービスでも出ません。**

## ⑤ 履歴と再生

| | Flightradar24 | ADS-B Exchange |
|---|---|---|
| 無料 | **7日** | **2020年3月以降**のリプレイ |
| 有料 | Silver 90日／Gold 365日／Business 3年 | （有料でも変わらず） |
| API | **2016年5月11日**まで遡れる（別料金） | 企業向けの日次データ製品 |

<strong>無料での遡りは、ADS-B Exchangeが圧倒的です。</strong>2020年3月まで戻れます。一方でFlightradar24は、**Businessプラン（年499.99ドル）で3年、APIなら2016年まで**という商用グレードの厚みがあります。

事故・インシデントの経路を後から検証したい、という用途では、この差が効いてきます。

## ⑥ API

| | Flightradar24 | ADS-B Exchange |
|---|---|---|
| 個人向け | **なし**（プランに含まれない） | <strong>$10/月・10,000リクエスト</strong>（RapidAPI経由、**非商用**） |
| 商用 | 従量課金（pay-as-you-go） | Enterprise 4製品（Live positions／Live operations／Daily positions／Daily operations） |
| 履歴 | 2016年5月11日以降 | 日次データ製品 |

Flightradar24のAPIは、**Silver/Gold/Businessのどのプランにも含まれません**（公式FAQに明記）。完全に別売りです。

個人が趣味で何か作るなら、<strong>ADS-B Exchangeの月10ドル・10,000リクエスト</strong>のほうが入りやすいと思います。

## ⑦ 受信機を立てると、どうなるか

どちらも、自分でADS-B受信機を設置してデータを提供する（フィーダーになる）と特典があります。

| | Flightradar24 | ADS-B Exchange |
|---|---|---|
| 特典 | <strong>Businessプラン（年499.99ドル相当）が無料</strong>＋招待制のContributorプラン | <strong>広告非表示の地図が無料</strong>（登録不要、`adsbexchange.com/myip`で有効化） |
| 機材 | 毎週30〜50セットの受信機一式を**無償配布** | 自前で用意（キットの販売あり） |

Flightradar24の特典は、金額だけ見ればかなり大きい。**年499.99ドルのBusinessプランが無料**になります。

とはいえ、どちらか一方にしか送れないわけではありません。**同じ受信機から複数のサービスへ同時に送る**のが一般的です。

## ⑧ 日本で使うとき

日本固有の事情として、いくつか。

<strong>日本語UIはFlightradar24にしかありません。</strong>ADS-B Exchangeは英語のみです。[以前の記事](/blog/adsbexchange-guide-2026/)で操作手順を書いたのは、まさにここが入口の壁になるからでした。

**便名・スケジュールの照合はFlightradar24が圧倒的に強い**です。150万機超のデータベースと商用スケジュールデータを持っているので、「この便はどこ発か」「遅れているか」という問いには向いています。ADS-B Exchangeにこの用途を求めても噛み合いません。

一方で、<strong>ADS-B Outを積んでいない機体は、どちらでも映りません。</strong>日本の回転翼機には非装備の機体も多く、その場合は[MLAT](/blog/flight-tracking-mlat-2026/)頼みになります。MLATは受信機が複数台届いている場所でしか成立しないので、**山間部や低高度では、両方とも消えます**。

<strong>受信機の密度も効きます。</strong>Flightradar24は50,000台、ADS-B Exchangeは25,000台。単純な台数では倍の差があるので、**「片方で見えて、片方で見えない」は、フィルタリング以前に受信網の問題であることもある**という点は頭に置いておきたいところです。

## で、どちらを使うか

用途で切り分けると、こうなると思います。

| やりたいこと | 向いているほう |
|---|---|
| 便名・出発地・到着地・遅延を調べる | **Flightradar24** |
| 空港の発着履歴を見る | **Flightradar24**（Silver以上） |
| スマホで手軽に、日本語で | **Flightradar24** |
| 「映らない機体」が本当に飛んでいるか確かめる | <strong>ADS-B Exchange</strong> |
| IAS・TAS・風・OATを無料で見る | <strong>ADS-B Exchange</strong> |
| QNH・選択高度・バンク角まで見る | <strong>ADS-B Exchange</strong> |
| その位置がADS-BかMLATかを確かめる | <strong>ADS-B Exchange</strong> |
| 2020年以降の経路を無料で遡る | <strong>ADS-B Exchange</strong> |
| 3年分の履歴／商用利用 | **Flightradar24 Business** |
| 個人で何か作る（API） | <strong>ADS-B Exchange</strong> |

**両方入れておけばいい**、というのが現実的な答えだと思います。どちらも無料で始められますし、片方で見えないものを片方で確かめる、という使い方が一番効きます。

ただ、<strong>パイロットが「教材」として見るなら、ADS-B Exchangeのほうが得るものは多い</strong>と感じています。IASとTASとGSが同時に並び、機首方位と対地針路の差がそのまま偏流として読め、精度指標まで数字で出る。**教科書で習った量が、実機の値として同時に表示される**という体験は、他ではなかなかできません。

## まとめ

- Flightradar24は**受信機50,000台以上**＋**衛星ADS-B・レーダー（北米豪州）・FLARM・UAT・ADS-C**まで取り込む。**150万機超のデータベース**で便名・路線と突き合わせる。
- ADS-B Exchangeは**受信機25,000台以上**、**500ミリ秒更新**。**受信したものを、受信したまま**出す。位置の取得元（ADS-B／MLAT／TIS-B等）を機体ごとに明示。
- <strong>Flightradar24には機体の非表示がある</strong>（FAA LADD／運航者の申請）。ADS-B Exchangeは<strong>「検閲やフィルタリングなし」</strong>を掲げる。2023年1月のJETNET買収後も、この方針は維持されている。
- 料金は、FR24が年額<strong>Silver $14.99／Gold $34.99／Business $499.99</strong>。**商用利用はBusinessのみ**。無料版は**30分でタイムアウト**し、履歴は7日。
- ADS-B Exchangeは<strong>$29.95/年で広告非表示＋地図レイヤー</strong>のみ。**有料にしても見える情報は増えない。**
- <strong>最大の差はここ。IAS／TAS／Mach／GPS高度／風／OATは、FR24ではGold（年34.99ドル）以上、ADS-B Exchangeでは無料。</strong>
- さらにADS-B Exchangeは、<strong>QNH・FMS選択高度／選択方位・真方位／磁方位・バンク角・NACp／SILまで無料表示</strong>。FR24の公開機能説明にこれらは出てこない。
- ただし**機体が放送していなければ、どちらでも出ない**。MLATや推定位置ではExtended Mode Sは得られない。
- 履歴は、**無料ならADS-B Exchange（2020年3月以降）**、**商用グレードならFR24（Business 3年、APIは2016年5月11日以降）**。
- APIは、個人なら<strong>ADS-B Exchangeの$10/月・10,000リクエスト</strong>。FR24のAPIは**どのプランにも含まれず別売**。
- 受信機を立てると、FR24は<strong>Businessプランが無料</strong>、ADS-B Exchangeは**広告非表示が無料**。受信機は**同時に複数サービスへ送れる**。
- 日本で使うなら、**日本語UIと便名照合はFR24一択**。**ADS-B Out非装備機はどちらにも映らない**ので、山間部・低高度では両方消えることに注意。

---

### 関連記事

- [ADS-B Exchangeの使い方——空港コードで飛べば、日本の空もすぐ見える](/blog/adsbexchange-guide-2026/)
- [Flightradar24はなぜ機体を映せるのか——ADS-Bとマルチラテレーション（MLAT）の仕組みを解説](/blog/flight-tracking-mlat-2026/)
- [ADS-Bとは何か——「放送型自動位置情報」の仕組み・メリット・課題](/blog/adsb-basics-2026/)

---

*本記事の価格・機能は2026年9月14日時点で各社が公開している情報に基づきます。**プラン内容や価格は予告なく変更されることがあります**（Flightradar24自身も「事前告知なく変更する権利を留保する」と明記しています）。最新の内容は各公式サイトでご確認ください。価格はいずれも米ドル・税別です。*

*ヒーロー画像はイメージです（自作の1090MHz ADS-Bダイポールアンテナ）。両サービスとも、こうしたアンテナを立てた世界中の個人・組織からのデータで成り立っています。"Homemade 1090 MHz ADS-B dipole antenna" by Happy-marmotte / [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Homemade_1090_MHz_ADS-B_dipole_antenna.jpg) / CC BY-SA 3.0（本記事への掲載にあたりリサイズを行いました）*

---

**出典**

- Flightradar24「[Subscription plans](https://www.flightradar24.com/premium)」
- Flightradar24「[How Flightradar24 works](https://www.flightradar24.com/how-it-works)」
- Flightradar24「[Understanding Extended Mode S Data in Flightradar24](https://www.flightradar24.com/blog/inside-flightradar24/understanding-extended-mode-s-data-in-flightradar24/)」
- Flightradar24「[Share your ADS-B data](https://www.flightradar24.com/share-your-data)」
- Flightradar24「[Flightradar24 API](https://fr24api.flightradar24.com/)」
- FAA「[Limiting Aircraft Data Displayed (LADD)](https://www.faa.gov/pilots/ladd)」
- ADS-B Exchange「[About](https://www.adsbexchange.com/about/)」
- ADS-B Exchange「[Community / Developer Hub](https://www.adsbexchange.com/community/developer-hub/)」
- ADS-B Exchange Store「[Annual Ad-free ADSBexchange Subscription](https://store.adsbexchange.com/products/annual-ad-free-adsbexchange-subscription)」
- JETNET「[JETNET Acquires ADS-B Exchange](https://www.jetnet.com/resources/press-releases/jetnet-acquires-ads-b-exchange)」

---
title: 'AIPの方位は真方位か、磁方位か——航空路・VOR・風・空域の境界線を原本で確かめる'
description: '天気図やMETARの風向は真方位、ATISの風向は磁方位。では、AIPに載っている航空路の方位はどちらなのか。AIP Japan（2026年10月1日版）のENRとGENを確かめると、航空路の方位は磁方位が基本で、RNAV経路には真方位が併記されていました。一方で、航空路の保護空域の境界線は真方位で書かれ、VORには「いつの偏差で調整したか」が載っています。風向、飛行計画、略語まで、真方位と磁方位の使い分けを整理しました。'
pubDate: '2026-10-29'
category: '基礎知識'
tags: ['IFR', '法規']
heroImage: '../../assets/posts/aip-true-magnetic-hero.jpg'
---

天気図やMETARの風向は<strong>真方位</strong>で、ATISや管制塔の風向は<strong>磁方位</strong>です。では、AIPに載っている<strong>航空路の方位</strong>はどちらなのでしょうか。

「たぶん磁方位」で済ませがちなところを、手元のAIP Japan（2026年10月1日版のENRとGEN）で一つずつ確かめました。

先に結論です。

- <strong>航空路の方位は磁方位</strong>が基本。RNAV経路（ENR 3.3）には<strong>真方位が［ ］で併記</strong>されている
- ただし、航空路の<strong>保護空域の境界線</strong>（ENR 3.1）は<strong>真方位（°T）</strong>で書かれている
- VOR（ENR 4.1）には、<strong>どの年の偏差で調整したか</strong>（例：9°W/2022）が載っている
- 風向は、<strong>離着陸のための風は磁方位、それ以外は真方位</strong>（GEN 2.1）

---

## 航空路——ENR 3.1（通常の航空路）

ENR 3.1「LOWER ATS ROUTES」の表は、2列目の見出しが「<strong>Track MAG (GEO) / VOR RDL</strong>」です。磁方位（MAG）が基本で、括弧で地理上の方位（GEO、つまり真方位）を示す形になっています。

実際の値を見ると、通常の航空路の方位は<strong>磁方位の2方向</strong>で書かれていて、今回見た範囲では括弧付きの真方位は記載されていませんでした。

| 航空路 | 区間（例） | 方位（MAG） |
|---|---|---|
| A1 | 串本VORTAC（KEC）〜清水VORTAC（SUC） | 262／080 |
| A590 | PASRO〜PUGAL付近 | 239／056 |
| R220 | NOGAL付近 | 238／055 |
| V17 | 大島VORTAC（XAC）〜ITTOH | 282／102 |

<small>出典：AIP Japan ENR 3.1（2026年10月1日版）。方位は往復の2方向。</small>

### 保護空域の境界線は「°T」

同じENR 3.1の「Lateral limits（側方の範囲）」の欄には、航空路の保護空域の境界線が書かれています。ここは<strong>真方位</strong>です。

> 例（A1）：「Lines extending on 258°34'T and 248°34'T FM KEC」
> （串本VORTACから、真方位258°34'と248°34'に延びる線）

数字の後ろの「<strong>T</strong>」は真方位（True）の印です。空域の境界は地図上に固定された線なので、年々動く磁北ではなく、真北を基準に定めていると考えられます。

## 航空路——ENR 3.3（RNAV経路）

ENR 3.3「RNAV ROUTES」の表は、見出しが「<strong>MAG TRACK ［TRUE TRACK］</strong>」で、<strong>磁方位と真方位の両方</strong>が載っています。

| 経路 | 区間 | MAG TRACK | ［TRUE TRACK］ | 差 |
|---|---|---|---|---|
| Y10 | 稚内（WKE）→ YOROI | <strong>194</strong> | ［183.8］ | 約10° |
| Y10 | YOROI → 稚内 | <strong>014</strong> | ［003.8］ | 約10° |
| Y10 | YOROI → RUMOI | <strong>193</strong> | ［182.0］ | 約11° |
| Y10 | RUMOI → 千歳（CHE） | <strong>192</strong> | ［181.8］ | 約10° |

<small>出典：AIP Japan ENR 3.3（2026年10月1日版）。</small>

差の約10°が、北海道北部の偏差（西偏）です。日本は西偏なので、<strong>磁方位＝真方位＋偏差</strong>になります。

RNAVは、GNSSなどで緯度経度から経路を計算するので、内部では真方位で考えるのが自然です。一方、パイロットは磁方位で飛ぶので、両方を載せているのだと考えられます。

## VOR——ENR 4.1には「偏差の年」が載っている

ENR 4.1「RADIO NAVIGATION AIDS - EN-ROUTE」の表では、局名の下に「<strong>VOR declination</strong>」として、偏差と年が書かれています。

| VOR | 表記 |
|---|---|
| 青森（MRE） | decl.: 9°W/2022 |
| 旭川（AWE） | decl.: 9°W/2018 |
| 庄内（YSE） | decl.: 9°W/2023 |
| 雄和（UWE） | decl.: 8°W/2013 |
| 南紀（NKE） | decl.: 7°W/2012 |
| 南大東（MDE） | decl.: 5°W/2014 |

<small>出典：AIP Japan ENR 4.1（2026年10月1日版）から抜粋。</small>

ENR 1.5の用語の定義では、station declination（局の偏差）は「<strong>VORの360°ラジアルと真北との角度</strong>」とされています。

つまり、VORのラジアルは「<strong>その年の偏差で調整した磁方位</strong>」です。地磁気は少しずつ動くので、2012年に調整したVORと、今の実際の偏差とでは、わずかにずれている可能性があります。航空路の磁方位はVORのラジアルに合わせて作られているので、計器で飛ぶうえでは問題ありません。ただ、<strong>GNSSが最新の偏差モデルで計算した磁方位と、VORのラジアルが1〜2°違う</strong>ことがあるのは、このためです。

## 風向——GEN 2.1の測定単位の表

GEN 2.1の「測定単位」の表には、風向についてはっきり書かれています。

| 項目 | 単位 |
|---|---|
| <strong>離着陸時の風向</strong> | <strong>磁方位</strong>による度数 |
| <strong>離着陸時以外の風向</strong> | <strong>真方位</strong>による度数 |

<small>出典：AIP Japan GEN 2.1（2026年10月1日版）。</small>

さらにGEN 1.7（ICAOの基準との相違点）の気象の部分には、「<strong>場内報において、風向は磁方位で通報する</strong>」とあります。空港内で使う気象の通報では、滑走路との関係が分かりやすいよう磁方位を使う、ということです。

これを整理すると、次のようになります。

| 情報 | 方位 |
|---|---|
| 天気図、数値予報、METAR、TAF、上空の風 | <strong>真方位</strong> |
| ATIS、管制塔から伝えられる離着陸のための地上風 | <strong>磁方位</strong> |

METARの風とATISの風の数字が数度ずれているのは、これが理由です。

## 飛行計画——ENR 1.10

飛行計画の経路欄で、地点を「ある地点からの方位と距離」で書く場合も、真方位と磁方位が分かれます。

| 書き方 | 方位 |
|---|---|
| AIPなどで公示されている地点（VORなど）からの方位と距離 | <strong>磁方位</strong> |
| VFRで、著名な都市・湖沼・山岳などからの方位と距離 | <strong>真方位</strong> |

<small>出典：AIP Japan ENR 1.10（2026年10月1日版）。</small>

VFRの「著名な地点からの方位」は真方位、というのは見落としやすいところです。地図の上で方位を測るなら真方位、という考え方だと理解すると覚えやすいと思います。

## 略語——GEN 2.2

GEN 2.2の略語表にも、真方位・磁方位を表す略語がそろっています。

| 略語 | 意味 |
|---|---|
| MAG | 磁方位 |
| GEO | 地理上の、または真方位 |
| T（…T） | 真方位 |
| VAR | 磁気偏差 |
| QDM | 磁針路（無風時） |
| QDR | 磁方位 |
| QTE | 真方位 |
| QFU | 磁方位による滑走路の方位、または番号 |

<small>出典：AIP Japan GEN 2.2（2026年10月1日版）。</small>

## なぜ使い分けるのか

- <strong>飛ぶための方位は磁方位</strong>——パイロットは磁気コンパスで飛び、VORも磁方位でラジアルを出します。滑走路番号も磁方位です。だから、航空路の方位、VORのラジアル、離着陸のための風は磁方位になります。
- <strong>地図に固定するものは真方位</strong>——空域の境界線や、地図上で測る方位、地球全体で扱う気象は、年々動く磁北ではなく真北を基準にします。
- <strong>RNAVは両方</strong>——緯度経度で計算するRNAVは真方位と相性がよく、パイロットに見せるのは磁方位なので、AIPでは両方を載せています。

## まとめ

- AIPの<strong>航空路の方位は磁方位</strong>が基本。ENR 3.1は「Track MAG (GEO)」で、通常の航空路は磁方位の2方向が載っている。ENR 3.3のRNAV経路は「<strong>MAG TRACK ［TRUE TRACK］</strong>」で真方位も併記（例：Y10 稚内→YOROI 194［183.8］）。
- 航空路の<strong>保護空域の境界線は真方位（°T）</strong>で書かれている。
- ENR 4.1のVORには<strong>偏差と調整した年</strong>（例：9°W/2022）が載っている。VORのラジアルは、その時点の偏差を基準にした磁方位。
- 風向は、<strong>離着陸のための風は磁方位、それ以外は真方位</strong>（GEN 2.1）。場内報の風は磁方位（GEN 1.7）。
- 飛行計画で、<strong>公示地点からの方位は磁方位</strong>、<strong>VFRで著名な地点からの方位は真方位</strong>（ENR 1.10）。

---

### 出典

- 国土交通省航空局「AIP Japan」ENR 1.5、ENR 1.10、ENR 3.1、ENR 3.3、ENR 4.1（2026年10月1日版）
- 国土交通省航空局「AIP Japan」GEN 1.7、GEN 2.1、GEN 2.2（2026年10月1日版）

*本記事は2026年10月1日版のAIPにもとづきます。実際の運航では最新のAIPを確認してください。*

ヒーロー画像：「Magnetkompass in einer Cessna C172」by Bin im Garten（[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Magnetkompass_in_einer_Cessna_C172_1262.JPG) / CC BY-SA 3.0）。セスナ172の磁気コンパス。掲載にあたり切り抜きとリサイズを行いました。

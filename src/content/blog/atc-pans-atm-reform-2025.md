---
title: '令和7年8月7日適用——管制業務処理規程改正のATC用語変更まとめ（PANS-ATM統一）'
description: '2025年8月7日、航空保安業務処理規程第５管制業務処理規程が改正された。SID/STARの承認と速度の関係の明確化と、ICAO PANS-ATMに準拠したトランスポンダー用語への変更が柱。パイロット視点で変更点を整理する。'
pubDate: '2025-08-07'
category: '最近の変更点'
heroImage: '../../assets/posts/atc-pans-atm-reform-2025-hero.jpg'
---

令和7年8月7日、**航空保安業務処理規程第５管制業務処理規程**が改正された。

今回の改正は大きく2本柱に分かれる。①SID/STARを経由した飛行中の高度・速度制限の扱いを明確にする規定の整備、②ICAO PANS-ATMに規定された用語への統一——だ。

特に②は、これまで使い慣れてきたスコーク用語が複数変わるため、パイロットとして把握しておきたい。

---

## 1. SID/STAR 経由飛行における高度・速度の扱い

### 新設フレーズ：CLIMB VIA SID / DESCEND VIA STAR

飛行中に管制官が高度を指定する場合であって、SID・STARに公示された高度制限または速度制限に従って飛行させたい場面で使う新用語が整備された。

| 場面 | 用語 |
|---|---|
| SID の制限に従って上昇させる場合 | **CLIMB VIA SID TO [altitude]** |
| STAR の制限に従って降下させる場合 | **DESCEND VIA STAR TO [altitude]** |

**例文：**
- `Recleared direct TAURA, climb via SID to 13,000.`
- `Cleared via DAIYA arrival, descend via STAR to altitude 2,000.`

### この指示を受けたときの航空機の義務

注意点として、以下の動作が規定されている。

- 注1：(a)または(b)の指示後は、その後の**経路変更の有無にかかわらず**、航空機は当該指示に係るSID/STAR に公示された速度に従って飛行する（レーダー誘導で通過しないフィックスに係るものを除く）。
- 注2：速度調整を行っている航空機に(a)(b)を指示した場合、改めて速度指示をしない限り、速度調整は**自動的に終了**し、SID/STARに公示された速度に従って飛行する。
- 注3：航空機に(b)を指示した場合、降下のタイミングはパイロットに任せる。

### STAR経由の進入許可

STARを経由して進入機に進入許可を発出する場合の用語も新設された。

★ **CLEARED FOR [type] APPROACH VIA [STAR name].**  
例：`[STAR name] via ([type] approach の種類) 進入を許可します。`

この許可を受けた航空機は、IAF・RNAV5経路・進入経路の最低経路高度と、**STARに公示された高度・速度に従って降下しながら進入**する。

ただし RNAV1 として指定された STAR を承認する場合は、レーダーと航法援助が提供できる場合に限る。

---

## 2. トランスポンダー用語の PANS-ATM 統一

今回の改正で最もパイロットに影響するのが、**スコーク関連用語の変更**だ。いずれも「PANS-ATMに規定された用語への改正」として整理されており、国際標準フレーズへの統一が目的。

### 位置確認のIDENT指示

| 現行 | 改正後 |
|---|---|
| IDENT FOR POSITION CONFIRMATION | **SQUAWK IDENT FOR POSITION CONFIRMATION** |
| SQUAWK [code] AND IDENT | **SQUAWK [code] (AND) IDENT** |
| IDENT | **SQUAWK IDENT** |

「IDENT」だけだったフレーズが「SQUAWK IDENT」に統一される。コードと組み合わせる場合も AND の扱いが明記される形となる。

### コードのリセット・確認

| 現行 | 改正後 |
|---|---|
| RECYCLE [code] | **RESET SQUAWK [code]** |
| CONFIRM YOU ARE SQUAWKING [code] | **CONFIRM SQUAWK [code]** |

コードのリセット要求は「RECYCLE」から「RESET SQUAWK」へ。確認要求は「CONFIRM YOU ARE SQUAWKING」から「CONFIRM SQUAWK」へ変更される。

### Mode C（高度スクォーク）

| 現行 | 改正後 |
|---|---|
| SQUAWK ALTITUDE | **SQUAWK CHARLIE** |
| STOP ALTITUDE SQUAWK | **STOP SQUAWK CHARLIE WRONG INDICATION** |

「ALTITUDE」という機能名称による呼称から、「CHARLIE」（Mode Cを指す音声変換文字）を使ったPANS-ATM標準表現への変更。

### ハイジャックコード（7500）確認

| 現行 | 改正後 |
|---|---|
| CONFIRM YOU ARE SQUAWKING 7500 | **CONFIRM SQUAWK 7500** |

コード確認の統一形式に合わせた変更。

---

## 3. そのほかの修正

DAIYA ARRIVAL・Y108・LAKES ARRIVALなどのSTAR・経路が廃止されているため、規程内の**例文が差し替え**られた。

---

## ヘリパイロットとして思うこと

「IDENT」「SQUAWK ALTITUDE」「RECYCLE」は長年の慣れがあるだけに、切り替えには少し意識が必要だ。

特に「SQUAWK ALTITUDE」→「SQUAWK CHARLIE」は、チャーリーがMode Cを表すという知識が改めて求められる。PANS-ATMの標準フレーズとして世界的に使われているものへの統一という意味では合理的な方向性だ。

SID/STARの「CLIMB VIA」「DESCEND VIA」フレーズは、高高度を飛ぶ固定翼で特に関係が深い変更だが、ヘリコプターもSTARを飛ぶ場面があれば同様に適用される。**経路変更後も速度制限が継続する**という点（注1）は特に押さえておきたい。

---

## まとめ

| 変更箇所 | 現行フレーズ | 改正後フレーズ |
|---|---|---|
| SID上昇（制限に従う） | — | CLIMB VIA SID TO [alt] |
| STAR降下（制限に従う） | — | DESCEND VIA STAR TO [alt] |
| STAR経由進入許可 | — | CLEARED FOR ... APPROACH VIA [STAR] |
| IDENT指示 | IDENT | **SQUAWK IDENT** |
| Mode C起動 | SQUAWK ALTITUDE | **SQUAWK CHARLIE** |
| Mode C停止（誤表示） | STOP ALTITUDE SQUAWK | **STOP SQUAWK CHARLIE WRONG INDICATION** |
| コードリセット | RECYCLE [code] | **RESET SQUAWK [code]** |
| コード確認 | CONFIRM YOU ARE SQUAWKING [code] | **CONFIRM SQUAWK [code]** |
| 7500確認 | CONFIRM YOU ARE SQUAWKING 7500 | **CONFIRM SQUAWK 7500** |

いずれも「PANS-ATM に規定された用語への改正」という位置づけで、日本の管制用語をICAO国際標準に揃える流れの一環だ。受信側のパイロットとして、新フレーズに耳を慣らしておきたい。

---

*出典：[【航空局】「R7.8.7適用_航空保安業務処理規程の一部(SID/STARの承認と速度の関係に係る規定等)改正」について（公益社団法人日本航空機操縦士協会）](https://www.japa.or.jp/11013)*

*ヒーロー画像：「Ssr coelpin」by Charly Whisky / [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ssr_coelpin.jpg) / CC BY-SA 3.0*

---

### 関連記事

- [【令和8年3月19日施行】滑走路占有監視支援機能に「警報」が追加——羽田事故から続く対策強化を解説](/blog/runway-occupancy-awareness-2026/)
- [第５管制業務処理規程に新設された用語——新旧対照表から読む令和8年3月改正](/blog/runway-occupancy-5th-regulation-terms-2026/)

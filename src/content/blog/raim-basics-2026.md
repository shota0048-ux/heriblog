---
title: 'RAIMとは何か——衛星の異常が直るまで最大2時間、その空白を埋める仕組み'
description: 'GPS航法の話に必ず出てくるRAIM（Receiver Autonomous Integrity Monitoring＝受信機による完全性の自律的監視）。位置の「精度」ではなく「完全性」を見張る機能で、5個の衛星（または4個＋気圧高度）が要ります。なぜ受信機が自分で監視しなければならないのか、FDEとの違い、警報が出たら何をするのか、そしてスプーフィングには半分しか効かないという限界まで整理します。'
pubDate: '2026-08-22'
updatedDate: '2026-08-22'
category: '基礎知識'
tags: ['IFR', '航空安全', '法規']
heroImage: '../../assets/posts/raim-basics-hero.jpg'
---

[サーキュラー5-005](/blog/gps-ifr-circular-2026/)、[AC 20-138D](/blog/ac20-138-2026/)、[RNAV航行の許可](/blog/rnav-approval-2026/)と読んできて、**どの文書にも必ず出てくる言葉**がありました。

<strong>RAIM。</strong>「5分を超えて継続して失われることが予測される場合」「RAIM警報が発出された場合」——条文はRAIMを前提に書かれています。

読みは<strong>「レイム」</strong>。綴りは<strong>Receiver Autonomous Integrity Monitoring</strong>で、日本の通達はこれを<strong>「受信機による完全性の自律的監視」</strong>と訳しています。

<strong>Receiver（受信機が）／Autonomous（自律的に）／Integrity（完全性を）／Monitoring（監視する）</strong>——4語がそのまま機能の説明になっている、珍しく素直な略語です。**誰が・どうやって・何を**が名前に全部入っている。

では、<strong>RAIMとは何なのか。</strong>今回はそれ自体を扱います。

## 条文の定義

日本の通達には、2つの書き方があります。

**サーキュラー5-005（1-2-9）**

> <strong>「受信機による完全性の自律的監視（RAIM）機能」</strong>とは、衛星航法装置が**GPS航法信号の完全性を自ら監視及び判断する機能**をいう。

**サーキュラー5-017（1.2 h）**——こちらのほうが技術的です。

> <strong>「受信機による完全性の自律的監視（RAIM）」</strong>とは、**ABASの一形態**であって、それによって、**GPS信号又は気圧高度により補強されたGPS信号のみを使用し**、GNSS受信機の処理プログラムが**GNSS航法信号の完全性を判断する**ものをいう。

そして5-017は、ABASの定義に注記を付けています。

> **注：ABASの最も一般的な形態は、受信機による完全性の自律的監視（RAIM）である。**

**補強（augmentation）には3種類あります。**[SBAS（衛星ベース）](/blog/tso-c146-2026/)、GBAS（地上ベース）、そして**ABAS（航空機ベース）**。RAIMは3つ目、**機上で完結する補強**です。

### この記事に出てくる略語

条文と英文資料を行き来するので、先に並べておきます。

| 略語 | 綴り | 日本の通達での訳 |
|---|---|---|
| **GNSS** | Global Navigation Satellite System | 全地球的航法衛星システム |
| **RAIM** | **Receiver Autonomous Integrity Monitoring** | **受信機による完全性の自律的監視** |
| **FDE** | **Fault Detection and Exclusion** | **故障探知及び排除** |
| **ABAS** | Aircraft-Based Augmentation System | 航空機ベースの補強システム |
| **SBAS** | Satellite-Based Augmentation System | 衛星ベースの補強システム |
| **GBAS** | Ground-Based Augmentation System | 地上ベースの補強システム |

<strong>補強システムの3つは、頭文字が「どこに置くか」を表しています。</strong>A＝航空機、S＝衛星、G＝地上。RAIMだけは補強の**方式の名前**で、置き場所はABASと同じ機上です。

なお、この表に<strong>「FD」は入れていません。</strong>理由は後半の[RAIMとFDE](#raimとfde見つけると追い出す)で触れます。

## 「精度」ではなく「完全性」

ここを取り違えると、話が全部ずれます。

- **精度（accuracy）**：位置がどれだけ真値に近いか
- **完全性（integrity）**：<strong>その位置を信じてよいかどうか、信じられないときに知らせてくれるか</strong>

<strong>RAIMが見張っているのは後者です。</strong>FAAのAIMは、こう言い切っています。

> **Without RAIM, the pilot has no assurance of the GPS position integrity.**
> （RAIMがなければ、パイロットはGPS位置の完全性について何の保証も得られない。）

GPSは常に位置を出します。<strong>間違っていても、出します。</strong>その「間違っているかもしれない」を教えてくれるものがなければ、画面の数字はただの数字です。

## なぜ受信機が自分で見張るのか——2時間の空白

いちばん腑に落ちたのが、AIMのこの説明でした。

> **RAIM provides immediate feedback to the pilot.** This fault detection is critical for performance-based navigation (PBN), because **delays of up to two hours can occur before an erroneous satellite transmission is detected and corrected by the satellite control segment.**
> （RAIMはパイロットに**即座のフィードバック**を提供する。この故障探知はPBNにとって決定的である。なぜなら、**誤った衛星の送信が管制セグメントによって検知され修正されるまでに、最大2時間の遅れが生じうる**からだ。）

<strong>衛星がおかしくなっても、地上が気づいて直すまで最大2時間かかる。</strong>

VORなら、施設が異常になれば地上のモニターが落として電波が止まります。<strong>GPSにはその即時性がない。</strong>だから<strong>機体側で、自分で見張るしかない</strong>——これがRAIMの存在理由です。

[5-005の1-3](/blog/gps-ifr-circular-2026/)が「**GPSは、単独で航法に使用するために必要なレベルの性能要件を完全には充足していない**」と書く、その中身の一つがこれだと思っています。

## どうやって見張るのか——「余分な1個」

位置を出すだけなら、衛星は**4個**あれば足ります（緯度・経度・高度・時刻の4つを解くため）。

RAIMがやるのは、**そこに1個足して、答え合わせをすること**です。

> In order for RAIM to determine if a satellite is providing corrupted information, **at least one satellite, in addition to those required for navigation, must be in view**.
> **RAIM requires a minimum of 5 satellites, or 4 satellites and barometric altimeter input (baro-aiding), to detect an integrity anomaly.**

余分な観測があれば、**全部の組み合わせが同じ答えを指すはず**です。指さないものがあれば、どれかが嘘をついている。**それが分かる。**

**ただし「誰が嘘つきか」までは、5個では分かりません。**

## RAIMとFDE——「見つける」と「追い出す」

Garminの資料が、この違いを端的に書いています。

> FDE consists of two distinct parts: **fault detection and fault exclusion**. **Fault detection (RAIM)** detects the presence of an unacceptably large pseudorange error（略）**Fault detection is synonymous with RAIM.** Upon the detection of a fault, **fault exclusion follows and excludes the source** of the unacceptably large pseudorange error, thereby allowing navigation to **return to normal performance without an interruption in service**.

<strong>探知（detection）＝RAIM、排除（exclusion）まで行くのがFDE。</strong>

そして、排除するには**もう1個要ります**。

> GPS receivers capable of FDE require **6 satellites or 5 satellites with baro-aiding**.

まとめると、こうなります。

| やること | 必要な衛星 | 気圧高度補強を使う場合 |
|---|---|---|
| **測位するだけ** | **4個** | — |
| **異常を見つける（RAIM）** | **5個** | **4個＋気圧高度** |
| **異常を排除する（FDE）** | **6個** | **5個＋気圧高度** |

Garminは、この関係をひとことで言っています。

> **More satellites are needed to provide FDE availability than are needed for RAIM. More satellites are needed to provide RAIM availability than are needed for basic GPS availability.**

<strong>階段になっている。</strong>だから「GPSは出ているのにRAIMがない」「RAIMはあるのにFDEがない」という状態が、ふつうに起こります。

**5-005が洋上・遠隔地域でだけFDE予測プログラムを要求する**のも、この階段のいちばん上を使うからです。洋上には代わりの航法手段がない——**排除して航法を続けられること**が、そこでは要件になります。

### 「FD」とは呼ばない——Flight Directorと衝突する

ここで一つ、用語の注意です。

**探知だけの機能を fault detection（FD）、排除まで行くものを FDE** と対で呼ぶ書き方は、GNSSの技術文献では一般的です。AC 20-138D自身も、受信機をこう区別しています。

> TSO-C129(AR) equipment may have either a <strong>fault detection-only algorithm</strong> or an **FDE algorithm**.

<strong>「探知のみ」対「FDE」。</strong>概念としては、確かにFDとFDEは対になっています。

<strong>しかし航空の文書では、「FD」という略号はすでに埋まっています。</strong>AC 20-138Dの略語表（Appendix 9）を引くと、こうです。

| 略語 | AC 20-138Dでの定義 |
|---|---|
| **FD** | <strong>Flight Director</strong> |
| **FDE** | Fault Detection and Exclusion |

念のためAC 20-138D全文で単独の「FD」を数えると**43件**ありますが、<strong>すべてFlight Director（又はA/FD＝Airport/Facility Directory）</strong>で、fault detectionの意味で使われている箇所は**ありません**。

> For all rotorcraft enroute RNP 0.3 operations, the use of an **autopilot and/or FD** is an acceptable means of complying with the FTE assumption

FAAのAIMでも同様で、日本の5-005・5-017も<strong>「故障探知及び排除（FDE）」</strong>しか略語を置かず、探知だけを指すときは<strong>「故障探知の適正レベル」</strong>と漢字で書き下しています。

<strong>技術の議論としては通じるが、運航の文脈で「FD」と言えばFlight Director。</strong>ここは分けておいたほうが安全です。

### ややこしい点——RAIMとFDEの上下関係は、資料で逆になる

もう一つ、混乱しやすいところがあります。

**Garminの書き方**は、<strong>RAIMが部品でFDEが全体</strong>です。

> **FDE consists of two distinct parts**: fault detection and fault exclusion. Fault detection **(RAIM)**…

ところが**AC 20-138Dの定義**は、<strong>FDEがRAIMの一種</strong>という書き方をしています。

> **Fault Detection and Exclusion (FDE).** <strong>A receiver autonomous integrity monitoring algorithm</strong> that can automatically detect and exclude a faulty satellite from the position solution…

<strong>包含関係が逆に見えます。</strong>どちらも誤りではなく、<strong>「RAIM」を狭く（＝探知機能そのもの）取るか、広く（＝機上で完全性を検証する手法の総称）取るか</strong>の違いです。ACの定義は明確に広いほうを採っています。

> **Receiver Autonomous Integrity Monitoring (RAIM).** <strong>Any algorithm that verifies the integrity of the position output using redundant GPS measurements, or using GPS measurements and barometric aiding, is considered a RAIM algorithm.</strong> An algorithm that uses additional information (e.g., multi-sensor system with inertial reference system) to verify the integrity of the position output may be acceptable as a <strong>RAIM-equivalent</strong>.

<strong>冗長な観測、または観測＋気圧高度で完全性を検証するものは、すべてRAIMアルゴリズムとみなす。</strong>この定義なら、FDEもRAIMの中に収まります。

そして最後の一文、<strong>RAIM-equivalent（RAIMと同等）</strong>。5-005が繰り返す<strong>「RAIM機能又はこれと同等な機能」</strong>という言い回しは、ここに対応しています。**慣性基準装置を組み合わせたマルチセンサーのように、別の情報を使って完全性を検証する方式**も、同等と認められうる——条文があの書き方をしている理由が、ACの定義側にありました。

## 気圧高度補強（baro-aiding）の落とし穴

「4個＋気圧高度」でRAIMが成立する、というのが**baro-aiding**です。5個目の衛星の代わりに、**高度という既知の情報**を1つ入れる。

AIMは、使い方に念を押しています。

> To ensure that baro-aiding is available, **enter the current altimeter setting into the receiver** as described in the operating manual. <strong>Do not use the GPS derived altitude</strong> due to the large GPS vertical errors that will make the integrity monitoring function invalid.

<strong>高度計規正値を、受信機に入れること。GPSが出した高度を使ってはならない。</strong>

理由が本質的です。**GPSの垂直誤差は大きい**ので、それを使うと<strong>完全性監視そのものが無効になる</strong>。

[5-005の2-2-2](/blog/gps-ifr-circular-2026/)が「**衛星航法装置により得られる垂直面の位置情報は（略）これを高度情報として使用しないこと**」と定めているのと、根っこは同じ話です。**GPSの高さは、GPSの見張り役には使えない。**

## 飛行フェーズで、厳しさが変わる

RAIMは「あるか・ないか」の2択ではありません。<strong>飛行フェーズごとに要求される完全性が違う</strong>ためです。

AIMの定義がそこを含んでいます。

> RAIM is the capability of a GPS receiver to perform integrity monitoring on itself by ensuring available satellite signals **meet the integrity requirements for a given phase of flight**.

エンルートで許される横方向の誤差と、最終進入で許される誤差はまったく違う。**同じ衛星配置でも、エンルートならRAIMがあり、進入ではない**ということが起こります。

Garminのマニュアルも、はっきり書いています。

> FAA's TSO requirements for **non-precision approaches specify significantly greater satellite coverage** than is required during other phases of flight. As a result, **RAIM may not be available for all approaches.**
> **Near 100% availability in Oceanic, En route, and Terminal phases of flight.**

<strong>洋上・エンルート・ターミナルではほぼ100％。落ちるとしたら進入。</strong>だから[5-005の5分ルール](/blog/gps-ifr-circular-2026/)も、[5-017のRAIM確認](/blog/rnav-approval-2026/)も、**進入について書かれている**わけです。

## 警報には2種類ある

これも知っておくと、画面の意味が変わります。AIMより。

**① 監視できません（衛星が足りない）**

> The first type of message indicates that **there are not enough satellites available to provide RAIM integrity monitoring**. **The GPS navigation solution may be acceptable, but the integrity of the solution cannot be determined.**

**位置は出ている。しかし、それが正しいかどうかは分からない。**——いちばん扱いに困る状態です。「表示があるから大丈夫」ではありません。

**② 異常を検知しました**

> The second type indicates that **the RAIM integrity monitor has detected a potential error** and that there is **an inconsistency in the navigation solution** for the given phase of flight.

## 落ちたら、何をするか

ここは日米で同じことを言っています。

**飛行中（AIM）**

> Active monitoring of alternative navigation equipment is **not required when RAIM is available** for integrity monitoring. <strong>Active monitoring of an alternate means of navigation is required when the GPS RAIM capability is lost.</strong>

<strong>サーキュラー5-005（4-2-2-3）</strong>も同じ構造です。

> **RAIM機能又はこれと同等な機能により完全性の監視が行われている場合に限り**、独立型衛星航法装置以外の航法装置の監視は行わなくてもよい。RAIM機能（略）が喪失した場合には、**独立型衛星航法装置以外の航法装置を常時監視**することにより、自機の位置のクロスチェックを行い（略）**それができない場合又はRAIM警報が発出された場合には、管制機関に連絡し、GPSに依存しない航法による経路に移行**しなければならない。

<strong>「他を見なくていい」のは、RAIMが効いている間だけ。</strong>

<strong>進入中（5-017 附属書5）</strong>は、もっと明確です。**完全性警報が発出された場合**、**FAFを通過するより前に完全性警報機能が利用できないと表示された場合**——いずれも**方式の飛行を継続してはならない**。

**飛行前に予測で落ちると分かったら（AIM）**

> In situations where RAIM is predicted to be unavailable, the flight must **rely on other approved navigation equipment, re-route to where RAIM is available, delay departure, or cancel the flight.**

5-005の三択（**①GPS以外の進入方式を計画 ②到着予定時間を変更 ③飛行を中止**）と、ほぼ同じことを言っています。

## SBASがあるとき、RAIMはどうなるのか

[SBAS（日本ではMSAS）](/blog/tso-c146-2026/)は、**完全性の情報を衛星から送ってくれます**。だからSBASの覆域内では、受信機はSBASの完全性を使い、**RAIM予測は基本的に不要**になります。Garminも「WAAS環境では予測は必要ない」と明記しています。

しかし**覆域を出たら**——AC 20-138Dが、その挙動を説明しています。

> When outside of a GPS/SBAS service provider's coverage area **the receivers can revert to using FDE for integrity**. The receiver will use **GPS/SBAS integrity or FDE; whichever provides the best protection level**.

<strong>SBASの外に出たら、FDEに戻る。</strong>そして受信機は、**そのときどきで保護レベルの良いほうを使う**。

だから[5-017 附属書5](/blog/rnav-approval-2026/)は、SBAS機を積んでいる運航者にもこう求めます。

> **SBAS受信機（全てのE/TSO-C145/C146）で航行する航空機については、運航者は、SBAS信号の利用できない空域におけるGPS RAIMの利用可能性が適切かどうかを確認すべきである。**

<strong>SBASを積んでいれば安心、ではない。</strong>どこまでがSBASの中なのかを知っておく必要があります。

## RAIMの限界——「嘘のつき方」による

最後に、押さえておくべき限界があります。**AIMが、GPS再放射装置（re-radiator）の不具合について書いている箇所**です。

> Since **Receiver Autonomous Integrity Monitoring (RAIM) is only partially effective against this type of disruption (effectively a "signal spoofing")**, **the pilot may not be aware of any erroneous navigation indications**; **ATC may be the only means available to identify these disruptions**.

<strong>RAIMは、スプーフィング（なりすまし）に対しては部分的にしか効かない。</strong>

理屈を考えると納得できます。RAIMは<strong>「観測どうしが矛盾していないか」</strong>を見る仕組みです。<strong>もし全部の観測が同じ方向に、整合的に嘘をついていたら、矛盾は出ません。</strong>1個だけおかしい故障には強く、**全体が揃って騙されている状況には弱い。**

そしてAIMは、**そのとき頼りになるのはATC**だと書いています。近年GPS妨害・偽装の報告は世界的に増えていますから、ここは覚えておく価値があります。

## パイロットとして思うこと

RAIMを調べて、いちばん印象に残ったのは<strong>「余分な1個」という発想</strong>でした。

位置を出すだけなら4個でいい。<strong>5個目は、答えを出すためではなく、答えを疑うためにある。</strong>そして疑うだけでなく犯人を追い出すには、6個目が要る。

これは航法の話にとどまらないと思いました。**確認とは、余分を持つこと**です。計器を1つ増やす、クロスチェックする人をもう1人乗せる——[群馬の報告書](/blog/gunma-haruna-lessons-2026/)が「操縦士2名体制が望ましい」と書いたのも、構造としては同じ話に見えます。**代われる人がいるかどうかではなく、答え合わせができるかどうか。**

もう一つ、<strong>「位置は出ているが、正しいかどうかは分からない」</strong>という状態が制度上きちんと定義されていることも、覚えておきたいところです。画面に線が出ていれば飛べる気になります。しかし<strong>RAIMがないとき、その線は「検算されていない答え」</strong>でしかない。

ヘリの実務で言えば、[TSO-C146](/blog/tso-c146-2026/)のSBAS機でMSASの中を飛んでいる限り、RAIMを意識する場面はほとんどありません。**意識すべきなのは、SBASの外に出るとき、そしてVFRでGPSを見ているとき**です。[VFRのGPS](/blog/gps-vfr-circular-2026/)には完全性の要件がそもそもありません。**「補助的に使用し」と書かれている意味は、ここにもある**のだと思います。

次回は、この**RAIM予測を実際にどうやるのか**——機上機能の操作、メーカーの予測プログラム、NOTAMの見方——を書く予定です。

## まとめ

- <strong>RAIM＝Receiver Autonomous Integrity Monitoring</strong>（受信機による完全性の自律的監視）。**Receiver／Autonomous／Integrity／Monitoring**の4語が、そのまま機能の説明になっている。5-017の定義では<strong>ABASの一形態</strong>で、**GPS信号又は気圧高度により補強されたGPS信号のみを使用**して、受信機の処理プログラムが**航法信号の完全性を判断する**もの。**ABASの最も一般的な形態がRAIM**。
- 見張っているのは**精度ではなく完全性**。<strong>「RAIMがなければ、パイロットはGPS位置の完全性について何の保証も得られない」</strong>（FAA AIM）。
- 必要な理由は<strong>「誤った衛星の送信が管制セグメントに検知され修正されるまで、最大2時間の遅れが生じうる」</strong>から。地上が気づくのを待てないので、**機上で即座に見張る**。
- 仕組みは**余分な観測による答え合わせ**。<strong>測位だけなら4個、RAIM（探知）に5個、FDE（排除）に6個</strong>。**気圧高度補強を使えばそれぞれ4個・5個**。
- <strong>探知＝RAIM、排除まで行くのがFDE（Fault Detection and Exclusion＝故障探知及び排除）</strong>。ただし<strong>航空文書で「FD」はFlight Director</strong>であり、探知だけを指す略号としては使われない（AC 20-138Dの略語表、及び同AC中の単独FD 43件はすべてFlight Director／A/FD）。日本の通達も略語は**FDEのみ**で、探知だけは「故障探知」と書き下す。
- <strong>RAIMとFDEの包含関係は、資料によって逆に書かれる。</strong>Garminは「FDEは探知と排除の2部からなり、探知がRAIM」、AC 20-138Dは「**FDEはRAIMアルゴリズムの一種**」。**RAIMを狭く（探知機能）取るか広く（機上で完全性を検証する手法の総称）取るか**の違いで、ACは広いほうを採る。ACの<strong>RAIM-equivalent</strong>（慣性等の別情報を使う方式も同等と認めうる）が、5-005の<strong>「RAIM機能又はこれと同等な機能」</strong>に対応している。必要衛星数は**FDE ＞ RAIM ＞ 基本GPS**の階段になっており、「GPSは出ているがRAIMがない」状態が起こりうる。**5-005が洋上・遠隔でFDE予測を求める**のはこのため。
- **baro-aidingでは高度計規正値を受信機に入れる。**<strong>GPSが出した高度を使ってはならない</strong>——垂直誤差が大きく、**完全性監視そのものが無効になる**（5-005 2-2-2の思想と同じ）。
- RAIMの可用性は**飛行フェーズで変わる**。<strong>洋上・エンルート・ターミナルはほぼ100％、落ちるとしたら進入</strong>（非精密進入のTSO要件が他のフェーズより格段に厳しいため）。
- 警報は2種類。<strong>①衛星が足りず監視できない（位置は出ているが完全性が判定できない） ②異常を検知した</strong>。
- 落ちたときの行動は日米で同じ構造。**RAIMが効いている間だけ他装置の監視を省略でき**、**喪失したら常時監視**、**できないか警報が出たら管制に連絡してGPSに依存しない経路へ**。進入中に完全性警報、又はFAF通過前に警報機能が使えない表示が出たら**継続してはならない**。飛行前に不可用と予測されたら**他装置に頼る／RAIMのある経路へ変更／出発を遅らせる／飛行を中止**。
- **SBAS覆域内ではRAIM予測は基本的に不要**。ただし**覆域外に出ると受信機はFDEに戻り**、**SBASの完全性とFDEのうち保護レベルの良いほうを使う**。だから**SBAS機でもSBAS非提供空域のRAIM可用性は確認すべき**（5-017）。
- 限界として、<strong>RAIMはスプーフィングに対しては部分的にしか効かない</strong>。**パイロットが誤表示に気づけない可能性があり、ATCが唯一の発見手段になりうる**（FAA AIM）。RAIMは**観測どうしの矛盾**を見る仕組みなので、**全体が整合的に騙される状況には弱い**。

### 関連記事

- [TSO-C146とは何か——GPSに「SBAS」を足すと、何ができるようになるのか](/blog/tso-c146-2026/)
- [IFRでGPSを使う基準（5-005）——RAIMが5分途切れると予測されたら、飛行を中止する](/blog/gps-ifr-circular-2026/)
- [AC 20-138Dを読む——日本の基準が一行で参照している261ページに、ヘリ専用の章があった](/blog/ac20-138-2026/)
- [RNAV航行の許可はどう取るのか——5-017の附属書10本と、最終進入でFTE 0.15NMという目標](/blog/rnav-approval-2026/)

---

*本記事は、国土交通省航空局のサーキュラー、FAAのAeronautical Information Manual及びAdvisory Circular、装備品製造者の公開資料に基づき、現役ヘリコプターパイロットの視点から整理したものです。英文の訳出は筆者によるものです。実際の運航にあたっては、必ず当該機の飛行規程と装備品のマニュアルをご確認ください。考察部分には筆者の私見を含みます。*

---

**出典**

- 国土交通省航空局 サーキュラー No.5-005「GPSを計器飛行方式に使用する運航の実施基準」（令和7年3月13日最終改正） [https://asims.cab.mlit.go.jp/fsdb/a_circular.nsf/bc2af3923a3cb575492574fd002dd5df/7f822a92532d0ee5492578c400431cc6/$FILE/5-005.pdf](https://asims.cab.mlit.go.jp/fsdb/a_circular.nsf/bc2af3923a3cb575492574fd002dd5df/7f822a92532d0ee5492578c400431cc6/$FILE/5-005.pdf)
- 国土交通省航空局 サーキュラー No.5-017「RNAV航行の許可基準及び審査要領」（令和6年3月29日最終改正。RAIM・ABAS・FDEの定義、附属書5） [https://asims.cab.mlit.go.jp/fsdb/a_circular.nsf/bc2af3923a3cb575492574fd002dd5df/ae4895bdcb4b04d449258998000508e6/$FILE/5-017.pdf](https://asims.cab.mlit.go.jp/fsdb/a_circular.nsf/bc2af3923a3cb575492574fd002dd5df/ae4895bdcb4b04d449258998000508e6/$FILE/5-017.pdf)
- FAA Aeronautical Information Manual, Chapter 1 Section 1（1-1-13 NAVAID/GPS異常の報告、1-1-17 Global Positioning System (GPS)） [https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap1_section_1.html](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap1_section_1.html)
- FAA Advisory Circular AC 20-138D（Change 2を含む。5-3.2 Sensor and Sensor/Navigation Computer Configuration ほか） [https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-138D_with_Change_1__2.pdf](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-138D_with_Change_1__2.pdf)
- Garmin「WAAS RAIM/FDE Prediction Program Instructions」（190-00643-01 Rev. E） [https://static.garmin.com/pumac/190-00643-01_E.pdf](https://static.garmin.com/pumac/190-00643-01_E.pdf)
- Garmin「GTN Xi Series Pilot's Guide」（190-02327-03 Rev. G。RAIM Prediction） [https://static.garmin.com/pumac/190-02327-03_g.pdf](https://static.garmin.com/pumac/190-02327-03_g.pdf)

**画像出典**：Wikimedia Commons "GPS Block IIIA (cropped)" by U.S. Air Force（Public domain）。イメージ画像（GPS Block IIIA衛星の想像図）。

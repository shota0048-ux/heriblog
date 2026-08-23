---
title: 'LOI、APPROACH DOWNGRADE、ABORT APPROACH——完全性が足りないとき、GTNは何を表示するか'
description: '保護レベルが警報限界を超えると警報が出る、と条文は書きます。ではコックピットには実際に何が出るのか。Garminの操作マニュアルとFAA承認のAFMSから、GPSステータスのLOI、飛行フェーズの黄色表示、LPVからLNAVへのダウングレード、そしてABORT APPROACHまで、実際の文言と処置を並べます。'
pubDate: '2026-08-23'
category: '基礎知識'
tags: ['IFR', '航空安全']
heroImage: '../../assets/posts/gtn-integrity-hero.jpg'
---

[前回のRAIMの記事](/blog/raim-basics-2026/)で、SBASの世界では判定が<strong>VPL（垂直保護レベル）とVAL（垂直警報限界）の比較</strong>に替わる、と書きました。

では——**その限界を超えたとき、コックピットには実際に何が出るのか。**

条文は「警報を提供しなければならない」で終わります。**その先を、機器メーカーの資料で見てみます。**

## 確認した資料

| 資料 | 番号 | 性格 |
|---|---|---|
| **GTN Xi Series Pilot's Guide** | 190-02327-03 Rev. G | 操作マニュアル |
| <strong>AFMS（飛行規程補足）Garmin GTN Xi GPS/SBAS System</strong> | 190-01007-C2 Rev. 5 | <strong>FAA承認</strong> |

いずれも<strong>GTN Xi系（650Xi／750Xi）</strong>の資料です。無印のGTN 750も考え方は同じですが、以下の文言は**Xiの資料で確認したもの**であることをお断りしておきます。

<strong>Pilot's Guideは「こう表示されます」、AFMSは「こうしなさい」。</strong>両方あると、表示と処置がつながります。

## ① 常時出ている「GPSステータス」

まず、平常時から出ている表示です。

| 表示 | 意味 |
|---|---|
| **Acquiring** | 最後の既知位置と衛星軌道データから、どの衛星が見えるはずかを判断中 |
| **3D Nav** | 3次元航法モード。衛星データから高度を計算 |
| <strong>3D Diff Nav</strong> | 3次元航法モード。<strong>SBASプロバイダからの差分補正を使用中</strong> |
| <strong>LOI</strong> | <strong>衛星のカバレッジが、内蔵の完全性監視テストを通すのに不十分</strong> |

<strong>MSAS圏内で普段見ているのは「3D Diff Nav」</strong>です。SBASプロバイダの一覧には<strong>「MSAS — Japan only」</strong>という行があります。

そしてマニュアルに、見逃せない注記があります。

> Operating with SBAS active outside of the service area may cause elevated EPU values to display on the status page. **Regardless of the EPU value displayed, the LOI annunciation is the controlling indication for determining the integrity of the GPS navigation solution.**

<strong>EPUの数値がどうであれ、完全性の判定を支配するのはLOI表示。</strong>推定位置誤差の数字を見て自分で判断するな、ということです。

**数字ではなく、旗を見る。**[RAIMの記事](/blog/raim-basics-2026/)で「精度と完全性は別」と書きましたが、その区別が操作マニュアルの注記に現れています。

## ② 飛行フェーズ表示——黄色は「予告」

アナンシエーター・バーには `ENR` `TERM` `LNAV` `LNAV+V` `LPV` `LP` `DPRT` `DR` などが出ます。ここに、実務でいちばん効く仕掛けがあります。

> Under normal conditions, these annunciations are **green**. They turn **yellow** when cautionary conditions exist.
>
> A caution alerts you when the **GPS/WAAS accuracy required for the displayed service level has not been met within the last 30 seconds**. This means that **an approach downgrade or failure may occur**.

<strong>黄色は「もう落ちた」ではなく「落ちるかもしれない」。</strong>直近30秒で、表示中のサービスレベルに必要な精度が満たせていない、という予告です。

マニュアルはこう続けます。

> **Always monitor flight phase annunciations and system messages for any change in status.**

**進入中にこの色の変化に気づけるかどうか**が、その先の展開を分けます。

## ③ 限界を超えたとき——LPV進入の実際の流れ

Pilot's GuideのLPVシーケンスが、そのまま答えになっています。

**正常なら、こう進みます。**

| タイミング | 起きること |
|---|---|
| 目的地の**31NM以内** | ENR → **TERM**、CDIが2.0NM → 1.0NM |
| 初期進入フィックス接近 | ウェイポイント・メッセージ、Time to Turn（10秒カウントダウン） |
| FAF接近 | TERM → <strong>LPV</strong> |
| **FAFの2.0NM手前** | CDIが1NMから角度スケーリングへ |
| <strong>FAFの60秒前</strong> | <strong>システムがGPS位置の完全性が進入の限界内にあることを検証</strong> |

**そして限界を超えたら、2段階で落ちます。**

> **If GPS integrity exceeds the horizontal and/or vertical alarm limits:**
> ・Approach downgrades to non-precision
> ・<strong>"LNAV" annunciates on Map</strong>
> ・Advisory message: <strong>"GPS approach downgraded. Use LNAV minima."</strong>
> ・<strong>Glideslope indication disappears</strong>
> ・Pilot continues approach using LNAV non-precision minimums, if applicable

> **If GPS integrity does not meet the non-precision horizontal alarm limits:**
> ・Advisory message: <strong>"Abort Approach. GPS approach is no longer available."</strong>
> ・Pilot acknowledges message
> ・<strong>Unit reverts to terminal limits of 1 NM to support navigation to the missed approach</strong>

まとめると、こうなります。

| 状況 | 表示 | できること |
|---|---|---|
| 正常 | **LPV** | LPVミニマ |
| **垂直／水平のアラームリミット超過** | **LNAV**＋"GPS approach downgraded. Use LNAV minima."＋<strong>グライドスロープ消滅</strong> | <strong>LNAVミニマで継続可</strong> |
| **非精密の水平リミットも未達** | <strong>"Abort Approach. GPS approach is no longer available."</strong> | <strong>進入中止</strong>（装置はTERMの1NMへ復帰） |

<strong>垂直だけ落ちればLNAVで降りられる。横も落ちたら、進入そのものが終わる。</strong>この2段構えが要点です。

### LP+Vには例外がある

> If the approach indicates "LP+V," then **advisory vertical guidance may be removed without indication**（略）<strong>This does not constitute a downgrade.</strong> You may still fly the approach to LP minimums.

<strong>参考表示の垂直誘導は、予告なく消えることがある。</strong>しかし**ダウングレードではない**ので、LPミニマでそのまま飛べます。

[AC 20-138Dが「advisory vertical guidanceには性能基準がなく、運航上のクレジットを主張できない」と書いていた](/blog/ac20-138-2026/)ことの、現物での現れ方がこれです。**もともと当てにしてよい線ではないから、消えても降格にならない。**

## ④ メッセージの実文言

| メッセージ | 本文 | 条件 |
|---|---|---|
| **LOSS OF INTEGRITY (LOI)** | Verify GPS position with other navigation equipment. | GPSボードがLOIを報告。アンテナが遮蔽されている可能性 |
| **APPROACH DOWNGRADE** | GPS approach downgraded. Use LNAV minima. | LPV又はLNAV/VNAVからLNAVへ降格。**垂直誘導が利用不可に** |
| **ABORT APPROACH** | GPS approach is no longer available. | GPSが進入レベルのサービス（LPV, LNAV, LNAV+V, L/VNAV）を提供できない |
| <strong>APPROACH NOT ACTIVE</strong> | Approach guidance not available. | <strong>進入がアクティブに移行できない（例：LNAVに必要なHPL/VPLがないため、装置がTERMのまま）</strong> |
| **GPS NAVIGATION LOST** | Insufficient satellites. ／ Erroneous position. | 衛星不足、又は誤った位置 |

<strong>4つ目が、まさに「保護レベル」そのものです。</strong>

**「LNAVに必要なHPL/VPLを持っていないので、装置がTERMのまま」**——<strong>HPL／VPLという語が、パイロット向けのマニュアルにそのまま出てきます。</strong>保護レベルは理論上の概念ではなく、**進入がアクティブにならない理由として画面に出る**ものだ、ということです。

ABORT APPROACHの推奨処置も明確です。

> **Initiate a climb to the MSA or other published safe altitude, abort the approach, and execute a non-GPS based approach.**

<strong>MSA又は公示された安全高度へ上昇し、進入を中止し、GPS以外の進入を実施する。</strong>

## ⑤ FAF前後で、警報の名前が変わる

Pilot's Guideの「GPS Alerts」表が、これを分けています。**同じ「完全性が足りない」でも、FAFの前と後で扱いが違います。**

| 表示 | 種別 | 条件 |
|---|---|---|
| **黄色「LOI」** | **Loss of Integrity** | GPS位置の完全性が現在の飛行フェーズの要件を満たさない。<strong>FAFの手前で発生する</strong>（進入がアクティブな場合） |
| <strong>コースガイダンスが無効化される</strong>（表示は原因ごと） | <strong>Loss of Navigation</strong> | ・<strong>FAF通過後</strong>にGPS完全性が進入要件を満たさない<br>・位置計算に十分な衛星がない状態が**5秒**を超える<br>・<strong>time to alert 内に排除できない過大な位置誤差や故障</strong>をGPSセンサーが検知<br>・機上ハードウェアの故障 |
| **黄色「No GPS Position」**（自機シンボル消失） | Loss of Position | 位置解が求められない |

<strong>FAF前ならLOI、FAF後ならLoss of Navigation。</strong>そして後者は<strong>コースガイダンスそのものが無効化されます</strong>。

3つ目の条件に注目してください。<strong>「time to alert 内に排除できない」</strong>——[FDE（排除）](/blog/raim-basics-2026/)が間に合わなかった場合、という意味です。**探知・排除・警報という順番が、そのまま条件文になっています。**

## ⑥ FAA承認のAFMSは、何をしろと書いているか

Pilot's Guideは説明書ですが、**AFMSは飛行規程補足**——つまり**守るべき手順**です。

**3.2.1 LOSS OF GPS/SBAS NAVIGATION DATA**

> the GTN Xi will enter one of two modes: **Dead Reckoning mode (DR)** or **Loss Of Integrity mode (LOI)**. The mode is indicated on the GTN by an **amber "DR" and/or "LOI"**.
>
> If the LOI annunciation is displayed, **revert to an alternate means of navigation** appropriate to the route and phase of flight.

代替手段がない場合の処置が、さらに踏み込んでいます。

> **LOSS OF INTEGRITY (LOI) MODE (no DR annunciated):**
> Navigation ..... <strong>FLY TOWARDS KNOWN VISUAL CONDITIONS</strong>
>
> NOTE: **All information derived from GPS will be removed.**

<strong>「既知の有視界状態に向かって飛べ」。</strong>飛行規程に、この一行が書いてあります。

**3.2.2 GPS APPROACH DOWNGRADE**

> the GTN Xi will **downgrade the approach**. The downgrade will **remove vertical deviation indication from the VDI** and **change the approach annunciation to LNAV**. The approach may be continued using the LNAV only minimums.

**ABORT APPROACHのときの装置の挙動**（同じ節）

> the GTN Xi will **flag all CDI guidance** and display a system message "ABORT APPROACH-GPS approach no longer available". **Immediately upon viewing the message, the unit will revert to Terminal navigation mode alarm limits.** If the position integrity is within these limits **lateral guidance will be restored** and the GPS may be used to execute the missed approach, **otherwise alternate means of navigation must be utilized**.

<strong>いったん全部フラグが立ち、ターミナルの警報限界に戻して、そこに収まれば横ガイダンスだけ戻る。</strong>進入復行をGPSで飛べるかどうかが、そこで決まります。

**「進入は無理でも、進入復行の航法は残るかもしれない」**——この設計思想は、知っておく価値があると思います。

## ⑦ 外部アナンシエーターがある機体は「INTG」かもしれない

AFMSのパワーオン・セルフテストの項に、こうあります。

> Self-Test - GPS Remote Annunciator (if installed):
> VLOC ／ GPS ／ <strong>LOI or INTG</strong> ／ TERM ..... ILLUMINATED

<strong>機体によっては「LOI」ではなく「INTG」</strong>と書かれたランプが付いています。**同じものを指す別表記**です。自分の乗る機体でどちらなのか、確認しておくとよさそうです。

## 条文の「中止すべき事態」と、画面の対応

ここまで見た表示を、日本の条文と突き合わせてみます。[5-017 附属書5](/blog/rnav-approval-2026/)は、RNP APCHで**継続してはならない4つの事態**を挙げていました。

| 5-017 附属書5が挙げる事態 | GTNでの現れ方 |
|---|---|
| ナビゲーション・ディスプレイに**無効表示**が示された | **No GPS Position**／CDIガイダンスのフラグ |
| **完全性警報**が発出された | 黄色**LOI**／LOSS OF INTEGRITY メッセージ |
| **FAFを通過するより前に完全性警報機能が利用できない**と表示された | **LOI**／<strong>APPROACH NOT ACTIVE</strong>（HPL/VPL不足でTERMのまま） |
| **FTEが超過**した | （装置は判定しない。**操縦者がCDI偏位で判断**） |

そして[附属書10 LP/LPV](/blog/rnav-approval-2026/)は、**FAP通過後**の中止事由に<strong>「垂直方向のガイダンスの喪失（横方向のガイダンスが表示されている場合も含む）」</strong>を挙げていました。

<strong>これはまさに、APPROACH DOWNGRADEが起きた状態です。</strong>画面上は「LNAV」に変わり、横の針は生きている。**それでも、LPVとして降りるつもりだったなら中止**——条文と画面が、ここできれいに噛み合います。

もう一つ。[5-005 4-2-2-3](/blog/gps-ifr-circular-2026/)は、RAIMを失ったときの手順をこう定めていました。

> RAIM機能又はこれと同等な機能が喪失した場合には、**独立型衛星航法装置以外の航法装置を常時監視**することにより（略）**それができない場合又はRAIM警報が発出された場合には、管制機関に連絡し、GPSに依存しない航法による経路に移行**しなければならない。

<strong>AFMSの「revert to an alternate means of navigation」と、同じことを言っています。</strong>条文が求める行動が、機器メーカーの飛行規程補足にも書かれている——**日本の通達とGarminのAFMSが、同じ動作を指している**わけです。

## パイロットとして思うこと

一連の表示を並べてみて、いちばん感心したのは<strong>「落とし方」が丁寧に設計されている</strong>ことでした。

<strong>いきなり全部消えるのではありません。</strong>まず**黄色**で「30秒間、必要な精度に届いていない」と予告する。次に**垂直だけ落として**LNAVに降格させる。それも駄目なら**進入を中止**させ、しかし**ターミナルの限界に戻して横ガイダンスだけでも復活させ**、進入復行に使わせようとする。

<strong>使えるものを、最後まで使わせる。</strong>そういう設計です。

そして、パイロット側に求められていることも、はっきりしています。<strong>色と文字を見ること。</strong>EPUの数字ではなくLOIの旗を見る、緑が黄色になったら身構える、LPVがLNAVに変わったらグライドスロープを当てにしない。

[前回](/blog/raim-basics-2026/)、RAIMの限界としてスプーフィングの話を書きました。<strong>旗が出ない嘘には気づけない。</strong>だからこそ、**出た旗は確実に拾う**——できることは、そこまでです。

ヘリの現場でGTN系を積んでいる機体は多いはずです。<strong>自分の機体のアナンシエーターが「LOI」なのか「INTG」なのか。</strong>次に乗るときに見ておこうと思います。

## まとめ

- 確認資料は<strong>GTN Xi Series Pilot's Guide（190-02327-03 Rev. G）</strong>と<strong>FAA承認のAFMS（190-01007-C2 Rev. 5）</strong>。いずれも**GTN Xi系**（650Xi／750Xi）。
- GPSステータスは**Acquiring／3D Nav／3D Diff Nav／LOI**の4種。**MSAS圏内の平常時は「3D Diff Nav」**。SBASプロバイダ一覧に<strong>「MSAS — Japan only」</strong>。
- <strong>EPUの数値がどうであれ、完全性判定を支配するのはLOI表示</strong>とマニュアルが明記。**数字ではなく旗を見る**。
- 飛行フェーズ表示は**通常は緑、注意状態で黄色**。黄色の意味は<strong>「表示中のサービスレベルに必要なGPS/WAAS精度が直近30秒間で満たされていない」＝ダウングレード又は失敗が起こりうる予告</strong>。
- LPVは<strong>FAFの60秒前にシステムが完全性を検証</strong>する。**目的地31NMでENR→TERM、FAF接近でTERM→LPV、FAF2NM手前で角度スケーリング**。
- <strong>限界超過は2段階。</strong>①水平／垂直のアラームリミット超過→**LNAVへ降格、"GPS approach downgraded. Use LNAV minima."、グライドスロープ消滅**（LNAVミニマで継続可）②非精密の水平リミットも未達→<strong>"Abort Approach. GPS approach is no longer available."</strong>（TERMの1NMへ復帰）。
- **LP+Vの参考垂直誘導は予告なく消えることがあるが、ダウングレードではない**（LPミニマで継続可）。
- メッセージ<strong>APPROACH NOT ACTIVE</strong>の条件は<strong>「LNAVに必要なHPL/VPLがないため装置がTERMのまま」</strong>。**保護レベルは画面に出る概念**。
- 警報は**FAFの前後で名前が変わる**。前は**LOI（Loss of Integrity）**、後は<strong>Loss of Navigation</strong>で**コースガイダンスが無効化**される。後者の条件には<strong>「time to alert内に排除できない過大な位置誤差」</strong>＝**FDEが間に合わない場合**が含まれる。
- AFMSの処置は、**LOI表示なら代替航法手段へ移行**。代替がないLOIモードでは<strong>「FLY TOWARDS KNOWN VISUAL CONDITIONS」</strong>。
- ABORT APPROACH時、装置は**全CDIガイダンスにフラグを立てた後、ターミナルモードの警報限界に戻す**。その限界内なら**横ガイダンスが復活し、進入復行にGPSを使える**。
- 外部アナンシエーターは機体により<strong>「LOI」又は「INTG」</strong>。
- 条文との対応——<strong>5-017 附属書5の「継続してはならない4事態」</strong>は、<strong>No GPS Position／LOI／APPROACH NOT ACTIVE／（FTEは操縦者判断）</strong>に対応。**附属書10の「FAP通過後の垂直ガイダンス喪失」は、まさにAPPROACH DOWNGRADEが起きた状態**。<strong>5-005 4-2-2-3の「GPSに依存しない航法へ移行」</strong>は、AFMSの<strong>"revert to an alternate means of navigation"</strong>と同じ動作を指している。

### 関連記事

- [RAIMとは何か——GPSが「自分の嘘」を見張る仕組みと、その限界](/blog/raim-basics-2026/)
- [RNAV航行の許可はどう取るのか——5-017の附属書10本と、最終進入でFTE 0.15NMという目標](/blog/rnav-approval-2026/)
- [AC 20-138Dを読む——日本の基準が一行で参照している261ページに、ヘリ専用の章があった](/blog/ac20-138-2026/)
- [TSO-C146とは何か——GPSに「SBAS」を足すと、何ができるようになるのか](/blog/tso-c146-2026/)

---

*本記事は、Garminが公開しているGTN Xi Series Pilot's Guide及びAFMS（飛行規程補足）の記述に基づき、現役ヘリコプターパイロットの視点から整理したものです。表示や手順は機種・ソフトウェアバージョン・装備構成により異なります。実際の運航にあたっては、必ず当該機の飛行規程及び装備品のマニュアルをご確認ください。考察部分には筆者の私見を含みます。*

---

**出典**

- Garmin **GTN Xi Series Pilot's Guide**（190-02327-03 Rev. G。GPSステータス、飛行フェーズ表示、LPV/LP進入シーケンス、メッセージ一覧、GPS Alerts） [https://static.garmin.com/pumac/190-02327-03_g.pdf](https://static.garmin.com/pumac/190-02327-03_g.pdf)
- Garmin **AFMS, Garmin GTN Xi GPS/SBAS System**（190-01007-C2 Rev. 5、FAA APPROVED。異常時手順、失敗メッセージ、セルフテスト） [https://static.garmin.com/pumac/190-01007-c2_05.pdf](https://static.garmin.com/pumac/190-01007-c2_05.pdf)
- 国土交通省航空局 サーキュラー No.5-017「RNAV航行の許可基準及び審査要領」附属書5 RNP APCH／附属書10 LP/LPV（令和6年3月29日最終改正）
- 国土交通省航空局 サーキュラー No.5-005「GPSを計器飛行方式に使用する運航の実施基準」（令和7年3月13日最終改正）
- FAA Advisory Circular AC 20-138D（Change 2を含む）

**画像出典**：Wikimedia Commons "Mooney M20J Plane Flight Instrument Panel" by Tony Webster（CC BY-SA 4.0）。イメージ画像（GPSナビゲーターを備えた計器盤の例。本文で扱うGTN Xiとは機種が異なります）。

---
title: 'RAIM予測はどこで見るのか——国交省「MSAS/RAIM Prediction information of JAPAN」の使い方'
description: 'サーキュラー5-005は「RAIMが5分を超えて失われると予測される場合」の処置を定めていますが、その予測をどこで見るのかまでは書いていません。答えは国土交通省航空局のMSAS/RAIM予測情報サービスです。ログイン不要で見られるSummary画面の読み方、FDとFDEで結果がどれだけ変わるか、マスク角とBaro-Aidingの効き方、NANUの読み方までを、実際の画面で確かめました。'
pubDate: '2026-09-20'
category: '基礎知識'
tags: ['IFR', '航空安全']
heroImage: '../../assets/posts/msas-raim-hero.jpg'
---

[サーキュラー5-005の記事](/blog/gps-ifr-circular-2026/)で、こう書きました。

> 飛行計画の作成段階において、RAIM予測機能若しくはこれと同等な予測機能又はNOTAM等により、到着予定時間での目的地においてRAIM機能…が<strong>5分を超えて継続して失われることが予測される場合</strong>には、次のいずれかの処置を行うこと

条文は「予測される場合」と書きますが、<strong>その予測をどこで見るのかは書いていません。</strong>

答えのひとつが、国土交通省航空局が運用している<strong>MSAS/RAIM Prediction information of JAPAN</strong>です。実際に開いて、何がどこまで見えるのかを確かめました。

---

## まず、ログイン画面は通り抜ける

URLはこれです。

> `https://msas-raim.mlit.go.jp/gpm/summary.html`

開くと一瞬「Login」という画面が出ますが、<strong>何もしなくて大丈夫です。</strong>ページのソースを見ると、ユーザ名とパスワードに `default` が埋め込まれていて、<strong>読み込みと同時に自動でログインが実行されます。</strong>ブックマークして開けば、そのまま中身が出ます。

画面の構成はシンプルで、タブは2つだけです。

| タブ | 中身 |
|---|---|
| <strong>Summary</strong> | 衛星の状況と、アウテージ予測の一覧。<strong>実務で見るのはこちら</strong> |
| **Analysis Result** | MSAS性能評価報告書（年次PDF）。2022〜2024年分が和英で置かれている |

そして最初に押さえておきたいのが、**時刻の扱い**と**予測期間**です。

- 画面上の時刻は<strong>すべてUTC</strong>
- 予測期間は<strong>72時間</strong>。筆者が見た日は `2026/09/19 15:00:00 ... 2026/09/22 15:00:00`（UTC）でした

日本時間で考えるなら9時間足します。上の例なら<strong>9月20日0時から9月23日0時（JST）</strong>です。

## Summary画面・左半分——衛星の状況

### Constellation Status

見出しに<strong>「Max. 15 / Min. 8 Satellites」</strong>と出ます。予測期間中に見えるGPS衛星の最大・最小の数です。

その下が、軌道面（Plane A〜F）とスロット（1〜6）のマス目に、衛星番号（G01〜G32）を並べた表です。筆者が見た日はこうでした。

| Slot | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | G24 | G16 | G29 | G02 | G03 | G32 |
| 2 | G31 | G25 | G27 | G01 | G10 | G15 |
| 3 | G30 | G22 | G08 | **Not Exist** | G05 | G09 |
| 4 | G07 | G12 | G17 | G06 | **Not Exist** | G04 |
| 5 | G13 | G26 | G19 | G11 | G23 | G20 |
| 6 | G28 | G14 | **Not Exist** | G18 | G21 | **Not Exist** |

<strong>「Not Exist」は、そのスロットに衛星が入っていない</strong>という意味です。36マスのうち4つが空いていました。GPSは公称24機体制ですが、実際には30機前後が運用されていて、余剰機がスロット外に置かれることもあります。ここで見ているのは<strong>「今日の並び」</strong>です。

黄色く塗られたマスがあれば、それが**Maintenance**（整備中）です。

### Exclude Information（NANU）

その下の表が、**予測計算から除外される衛星**です。米国が発行する<strong>NANU（Notice Advisory to Navstar Users）</strong>——GPS版のNOTAMだと思えば近い——を取り込んでいます。

筆者が見た日の3行はこうでした。

| NANU | Type | Satellite | Start | Stop |
|---|---|---|---|---|
| 2026074 | FCSTSUMM | G13 | 2026/09/15 19:10 | 2026/09/16 01:49 |
| 2026075 | FCSTSUMM | G01 | 2026/09/18 03:09 | 2026/09/18 08:36 |
| **2026076** | **FCSTDV** | **G15** | **2026/09/24 23:45** | **2026/09/25 11:45** |

Typeの読み方だけ押さえておくと、表の意味が変わります。

| Type | 意味 |
|---|---|
| **FCSTDV** | Forecast Delta-V。<strong>軌道修正のための計画停止</strong>。終了後にアルマナックの更新が必要になることがある |
| **FCSTMX** | Forecast Maintenance。イオンポンプ運転やソフトウェア試験のための計画停止 |
| **FCSTSUMM** | Forecast Summary。<strong>整備が終わったあとに出る、実際の停止時刻の確定値</strong>。元のNANUを参照する |
| **UNUSUFN** | Unusable Until Further Notice。<strong>追って通知があるまで使用不可</strong> |

上の表を読み直すと、**上2行（FCSTSUMM）は終わった話**の記録で、<strong>これから効くのは3行目のFCSTDV（G15、9月24〜25日）だけ</strong>だと分かります。ただしこれは予測期間（〜9月22日）の外なので、この回の計算には効いていません。

**「Typeを見ないと、過去の話と未来の話が同じ表に並んで見える」**——ここが最初のつまずきどころだと思います。

### SBAS Status

MSASの状態です。こちらは<strong>NAQU</strong>という別系統の通報で、筆者が見た日は空でした。空なら、MSAS側に計画停止はないということです。

## Summary画面・右半分——アウテージ予測

ここからが本題です。凡例は3色。

| 色 | 意味 |
|---|---|
| **赤** | Predicted Outage Period（<strong>予測期間内にアウテージあり</strong>） |
| **緑** | No Outage Period（アウテージなし） |
| **灰** | No Result（結果なし） |

### Airport (JPN)

日本の空港のICAOコードが並びます。筆者が見た日は<strong>87地点が赤で表示</strong>されていました。RJAA（成田）からROYN（与那国）まで、ひととおり網羅されています。

ここで慌てないでほしいのですが、<strong>これは「今日は全国どこもGPS進入ができない」という意味ではありません。</strong>後で見るように、アウテージの有無は**RAIMの方式・マスク角・気圧高度補正の有無**といった条件の組み合わせで大きく変わります。この一覧は、**いずれかの条件で赤が出る空港**を集めたものと読むのが実態に近いです。

### Wide Area (JPN)——ここがいちばん情報量がある

日本全域を対象にした、<strong>RNP 0.3 / 1.0 / 2.0</strong> のタブ切り替えです。それぞれに4行×4列のマトリクスが入っています。

筆者が確認した日の値を、そのまま図にしました。

<div class="raim-matrix-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 694" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="MSAS/RAIM予測サービスのWide Areaマトリクス。RNP0.3・1.0・2.0ごとに、FD/FDEとマスク角、SA設定、Baro-Aidingの組合せでアウテージ予測の有無を示す">
  <text x="280" y="26" text-anchor="middle" fill="#14304a" font-size="15" font-weight="bold">Wide Area（日本全域）のアウテージ予測マトリクス</text>
  <text x="280" y="46" text-anchor="middle" fill="#4b5563" font-size="11.5">2026/09/19 15:00〜09/22 15:00 UTC の予測期間で筆者が確認した値</text>
  <text x="280" y="61" text-anchor="middle" fill="#4b5563" font-size="11"><tspan fill="#d24a3d" font-weight="bold">× ＝ アウテージ予測あり</tspan>　／　<tspan fill="#4a9d5f" font-weight="bold">○ ＝ アウテージなし</tspan></text>
  <text x="34" y="80" fill="#14304a" font-size="13" font-weight="bold">RNP 0.3</text>
  <rect x="154" y="88" width="180" height="22" fill="#eef1f5" stroke="#d9d3c6"/>
  <text x="244" y="103" text-anchor="middle" fill="#14304a" font-size="11" font-weight="bold">SA ON</text>
  <rect x="334" y="88" width="180" height="22" fill="#eef1f5" stroke="#d9d3c6"/>
  <text x="424" y="103" text-anchor="middle" fill="#14304a" font-size="11" font-weight="bold">SA Aware</text>
  <rect x="154" y="110" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="199" y="125" text-anchor="middle" fill="#4b5563" font-size="10.5">Baro</text>
  <rect x="244" y="110" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="289" y="125" text-anchor="middle" fill="#4b5563" font-size="10.5">w/o Baro</text>
  <rect x="334" y="110" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="379" y="125" text-anchor="middle" fill="#4b5563" font-size="10.5">Baro</text>
  <rect x="424" y="110" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="469" y="125" text-anchor="middle" fill="#4b5563" font-size="10.5">w/o Baro</text>
  <rect x="34" y="88" width="120" height="44" fill="#f6f4ee" stroke="#d9d3c6"/>
  <rect x="34" y="132" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="44" y="151" fill="#14304a" font-size="12" font-weight="bold">FD</text>
  <text x="144" y="151" text-anchor="end" fill="#4b5563" font-size="11">マスク 5.0°</text>
  <rect x="154" y="132" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="152" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="244" y="132" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="152" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="132" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="152" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="132" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="152" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="34" y="160" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="144" y="179" text-anchor="end" fill="#4b5563" font-size="11">マスク 2.0°</text>
  <rect x="154" y="160" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="180" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="160" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="180" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="334" y="160" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="180" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="160" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="180" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="34" y="188" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="44" y="207" fill="#14304a" font-size="12" font-weight="bold">FDE</text>
  <text x="144" y="207" text-anchor="end" fill="#4b5563" font-size="11">マスク 5.0°</text>
  <rect x="154" y="188" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="208" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="244" y="188" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="208" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="188" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="208" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="424" y="188" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="208" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="34" y="216" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="144" y="235" text-anchor="end" fill="#4b5563" font-size="11">マスク 2.0°</text>
  <rect x="154" y="216" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="236" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="244" y="216" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="236" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="216" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="236" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="424" y="216" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="236" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <text x="34" y="278" fill="#14304a" font-size="13" font-weight="bold">RNP 1.0</text>
  <rect x="154" y="286" width="180" height="22" fill="#eef1f5" stroke="#d9d3c6"/>
  <text x="244" y="301" text-anchor="middle" fill="#14304a" font-size="11" font-weight="bold">SA ON</text>
  <rect x="334" y="286" width="180" height="22" fill="#eef1f5" stroke="#d9d3c6"/>
  <text x="424" y="301" text-anchor="middle" fill="#14304a" font-size="11" font-weight="bold">SA Aware</text>
  <rect x="154" y="308" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="199" y="323" text-anchor="middle" fill="#4b5563" font-size="10.5">Baro</text>
  <rect x="244" y="308" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="289" y="323" text-anchor="middle" fill="#4b5563" font-size="10.5">w/o Baro</text>
  <rect x="334" y="308" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="379" y="323" text-anchor="middle" fill="#4b5563" font-size="10.5">Baro</text>
  <rect x="424" y="308" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="469" y="323" text-anchor="middle" fill="#4b5563" font-size="10.5">w/o Baro</text>
  <rect x="34" y="286" width="120" height="44" fill="#f6f4ee" stroke="#d9d3c6"/>
  <rect x="34" y="330" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="44" y="349" fill="#14304a" font-size="12" font-weight="bold">FD</text>
  <text x="144" y="349" text-anchor="end" fill="#4b5563" font-size="11">マスク 5.0°</text>
  <rect x="154" y="330" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="350" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="330" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="350" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="334" y="330" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="350" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="330" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="350" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="34" y="358" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="144" y="377" text-anchor="end" fill="#4b5563" font-size="11">マスク 2.0°</text>
  <rect x="154" y="358" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="378" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="358" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="378" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="334" y="358" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="378" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="358" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="378" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="34" y="386" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="44" y="405" fill="#14304a" font-size="12" font-weight="bold">FDE</text>
  <text x="144" y="405" text-anchor="end" fill="#4b5563" font-size="11">マスク 5.0°</text>
  <rect x="154" y="386" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="406" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="244" y="386" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="406" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="386" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="406" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="424" y="386" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="406" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="34" y="414" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="144" y="433" text-anchor="end" fill="#4b5563" font-size="11">マスク 2.0°</text>
  <rect x="154" y="414" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="434" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="414" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="434" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="414" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="434" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="414" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="434" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <text x="34" y="476" fill="#14304a" font-size="13" font-weight="bold">RNP 2.0</text>
  <rect x="154" y="484" width="180" height="22" fill="#eef1f5" stroke="#d9d3c6"/>
  <text x="244" y="499" text-anchor="middle" fill="#14304a" font-size="11" font-weight="bold">SA ON</text>
  <rect x="334" y="484" width="180" height="22" fill="#eef1f5" stroke="#d9d3c6"/>
  <text x="424" y="499" text-anchor="middle" fill="#14304a" font-size="11" font-weight="bold">SA Aware</text>
  <rect x="154" y="506" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="199" y="521" text-anchor="middle" fill="#4b5563" font-size="10.5">Baro</text>
  <rect x="244" y="506" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="289" y="521" text-anchor="middle" fill="#4b5563" font-size="10.5">w/o Baro</text>
  <rect x="334" y="506" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="379" y="521" text-anchor="middle" fill="#4b5563" font-size="10.5">Baro</text>
  <rect x="424" y="506" width="90" height="22" fill="#f6f4ee" stroke="#d9d3c6"/>
  <text x="469" y="521" text-anchor="middle" fill="#4b5563" font-size="10.5">w/o Baro</text>
  <rect x="34" y="484" width="120" height="44" fill="#f6f4ee" stroke="#d9d3c6"/>
  <rect x="34" y="528" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="44" y="547" fill="#14304a" font-size="12" font-weight="bold">FD</text>
  <text x="144" y="547" text-anchor="end" fill="#4b5563" font-size="11">マスク 5.0°</text>
  <rect x="154" y="528" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="548" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="528" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="548" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="334" y="528" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="548" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="528" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="548" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="34" y="556" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="144" y="575" text-anchor="end" fill="#4b5563" font-size="11">マスク 2.0°</text>
  <rect x="154" y="556" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="576" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="556" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="576" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="334" y="556" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="576" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="556" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="576" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="34" y="584" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="44" y="603" fill="#14304a" font-size="12" font-weight="bold">FDE</text>
  <text x="144" y="603" text-anchor="end" fill="#4b5563" font-size="11">マスク 5.0°</text>
  <rect x="154" y="584" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="604" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="584" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="604" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="584" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="604" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="584" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="604" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="34" y="612" width="120" height="28" fill="#ffffff" stroke="#d9d3c6"/>
  <text x="144" y="631" text-anchor="end" fill="#4b5563" font-size="11">マスク 2.0°</text>
  <rect x="154" y="612" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="199" y="632" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="244" y="612" width="90" height="28" fill="#d24a3d" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="289" y="632" text-anchor="middle" fill="#d24a3d" font-size="16" font-weight="bold">×</text>
  <rect x="334" y="612" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="379" y="632" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <rect x="424" y="612" width="90" height="28" fill="#4a9d5f" fill-opacity="0.16" stroke="#d9d3c6"/>
  <text x="469" y="632" text-anchor="middle" fill="#4a9d5f" font-size="16" font-weight="bold">○</text>
  <text x="280" y="682" text-anchor="middle" fill="#4b5563" font-size="10.5">※値は予測期間ごとに変わります。実際の運航では必ず当日の画面を確認してください。</text>
</svg>
</div>

読み取れることが4つあります。

**① FDとFDEでは、難易度がまるで違う**

<strong>FD（Fault Detection＝故障の検出）</strong>と<strong>FDE（Fault Detection and Exclusion＝検出して、その衛星を排除して航法を継続）</strong>。

図を見ると、**FDの行はほとんど緑**なのに、**FDEの行は赤だらけ**です。排除までやろうとすると、**壊れた1機を捨てたあとにも必要な幾何配置を保てる衛星数**が要るので、条件が一段厳しくなります。

5-005が[洋上ではFDEの予測を求めている](/blog/gps-ifr-circular-2026/)のは、代替手段が乏しい空域だからですが、**その予測が通るかどうかは、このくらいシビア**だということです。

**② RNPが厳しいほど、赤が増える**

RNP 2.0 → 1.0 → 0.3 と進むにつれて赤が増えます。当然といえば当然ですが、<strong>「RNP 0.3の進入を予定しているなら、RNP 1.0の結果を見ても意味がない」</strong>ということでもあります。

**③ マスク角は2.0°のほうが有利**

マスク角とは、<strong>「地平線から何度より上の衛星を使うか」</strong>という設定です。5.0°だと低い衛星を切り捨て、2.0°なら拾います。図では<strong>2.0°の行のほうが緑が多い</strong>——拾える衛星が増えるぶん、条件を満たしやすくなります。

**④ Baro-Aidingが効く場面がある**

<strong>Baro-Aiding＝気圧高度計の値を高度の「もう1つの測定値」として使う</strong>ことです。衛星1機ぶんの働きをしてくれるので、必要な衛星数が実質1つ減ります。

図のRNP 1.0・FDE・マスク2.0°の行を見てください。<strong>Baro-Aidingありは○、なしは×</strong>。RNP 2.0・FDE・マスク5.0°も同じです。**装備の差が、そのまま予測結果の差になっている**のが見える箇所です。

なお「SA ON / SA Aware」は、GPSの<strong>SA（Selective Availability：意図的な精度劣化）</strong>を想定するかどうかの区別です。SAは2000年に停波され、現行のGPS III衛星にはSA機能自体が実装されていません。**SA Awareのほうが実態に近い**設定になります。

## ログインなしで見られるのは、ここまで

ここまでが、**アカウントなしで誰でも見られる範囲**です。

一方、画面右上の「Sign in」を開くと、こう書かれています。

> このWebサイトの<strong>すべてのサービスを利用するには、ユーザ登録（無料）が必要です。</strong>まずメールアドレスを登録してください。ユーザ登録ページのURLがメールアドレスに送られます。

<strong>登録は無料。</strong>そして、[航空局の研究開発資料](https://www.mlit.go.jp/koku/carats/)が説明しているとおり、RAIM予測は本来<strong>「飛行計画（出発地・経路・各地点の通過予定時刻）と突き合わせて、その計画に対して使えるかを判定する」</strong>もので、そこまでやるには登録が要る、という構造です。

つまり、

| | 見られるもの |
|---|---|
| **登録なし** | 衛星の並び、NANU、**日本全域と空港のアウテージ有無** |
| **登録あり（無料）** | 上記＋<strong>自分の飛行計画に対する判定</strong> |

**実際に飛行計画と突き合わせるなら、登録してしまったほうが早い**と思います。（本記事では登録は行わず、公開されている範囲のみ確認しました。）

## 5-005と、どう結びつけるか

最後に、条文との対応を整理します。

| 5-005が求めていること | この画面のどこを見るか |
|---|---|
| 到着予定時刻の目的地でRAIMが**5分を超えて失われないか** | 登録して**飛行計画と突き合わせる**。Summaryだけでは「その時刻」まで絞れない |
| **洋上でのFDEの予測** | Wide AreaのFDEの行。**赤が出やすい**ので早めに確認 |
| 装備クラスと補強の有無による分岐 | **Baro-Aidingの有無**の列で、自機の条件に合う側を見る |
| 進入方式に応じた精度 | **RNP 0.3 / 1.0 / 2.0** のタブを、実施する方式に合わせる |

そして、この画面を見るうえでいちばん大事なのは、<strong>自機がどの条件に当てはまるかを先に決めておく</strong>ことだと思います。FDかFDEか、マスク角はいくつか、Baro-Aidingはあるか。**それが決まっていないと、16マスのどれを見ればいいのか分かりません。**

逆に言えば、一度決めてしまえば**見るべきマスは1つ**です。

## まとめ

- RAIM予測は、国土交通省航空局の<strong>MSAS/RAIM Prediction information of JAPAN</strong>（`msas-raim.mlit.go.jp/gpm/summary.html`）で確認できる。**Login画面は自動で通過**するので操作は不要。
- 時刻は<strong>すべてUTC</strong>、予測期間は<strong>72時間</strong>。
- 左半分は衛星の状況。**Constellation Status**（軌道面×スロット、Not Existは空きスロット）、**Exclude Information**（NANU）、**SBAS Status**（NAQU）。
- NANUの**Type**を見ないと、**終わった停止（FCSTSUMM）と、これからの停止（FCSTDV・FCSTMX）が同じ表に混ざって見える**。
- 右半分がアウテージ予測。**赤＝予測期間内にアウテージあり／緑＝なし／灰＝結果なし**。
- <strong>Wide Areaのマトリクスがいちばん情報量が多い</strong>。RNP 0.3/1.0/2.0 × FD/FDE × マスク角5.0°/2.0° × SA ON/SA Aware × Baro-Aidingの有無。
- 読みどころは4つ。<strong>①FDよりFDEが圧倒的に厳しい</strong>／②**RNPが厳しいほど赤が増える**／③**マスク角2.0°のほうが有利**／④<strong>Baro-Aidingの有無が結果を分ける場面がある</strong>。
- SAは2000年に停波済み。**SA Awareのほうが実態に近い**。
- <strong>登録なしで見られるのはここまで。</strong>飛行計画と突き合わせた判定には<strong>無料のユーザ登録</strong>が必要。
- [5-005](/blog/gps-ifr-circular-2026/)の「5分ルール」を満たすかは、**Summaryだけでは判断できない**。自機の条件（FD/FDE・マスク角・Baro-Aiding・RNP）を先に決めてから、該当するマスを見る。

---

### 関連記事

- [RAIMとは何か——衛星の異常が直るまで最大2時間、その空白を埋める仕組み](/blog/raim-basics-2026/)
- [IFRでGPSを使う基準（5-005）——RAIMが5分途切れると予測されたら、飛行を中止する](/blog/gps-ifr-circular-2026/)
- [VFRでGPSを使う基準——「補助的に使用し」と、貼らなければならない標識](/blog/gps-vfr-circular-2026/)
- [TSO-C146とは何か——GPSに「SBAS」を足すと、何ができるようになるのか](/blog/tso-c146-2026/)
- [LOI、APPROACH DOWNGRADE、ABORT APPROACH——完全性が足りないとき、GTNは何を表示するか](/blog/gtn-integrity-annunciations-2026/)

---

*本記事は2026年9月20日（UTC 9月19日）時点で、筆者が実際に画面を開いて確認した内容に基づきます。<strong>表示される値は予測期間ごとに変わります。</strong>画面構成や提供範囲も変更されることがあるため、実際の運航では必ず当日の画面と最新の公式情報でご確認ください。*

*ヒーロー画像はイメージです（2026年1月、バックリー宇宙軍基地でC-17に搭載されるGPS III 10号機）。"GPS III at Buckley Space Force Base" by Staff Sgt. Amanda Flower, U.S. Space Force / [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:GPS_III_at_Buckley_Space_Force_Base_(9470835).jpg) / パブリックドメイン（本記事への掲載にあたりリサイズを行いました）*

---

**出典**

- 国土交通省航空局「[MSAS/RAIM Prediction information of JAPAN](https://msas-raim.mlit.go.jp/gpm/summary.html)」（Summary画面／2026年9月20日確認）
- 国土交通省航空局 サーキュラー No.5-005「GPSを計器飛行方式に使用する運航の実施基準」
- 国土交通省「[CARATS（将来の航空交通システムに関する研究会）](https://www.mlit.go.jp/koku/carats/)」全飛行フェーズでの衛星航法サービスの提供（EN-7）RAIM予測最適化、GNSS性能監視
- U.S. Coast Guard Navigation Center「[NANU Abbreviations and Descriptions](https://navcen.uscg.gov/nanu-abbreviations-and-descriptions)」

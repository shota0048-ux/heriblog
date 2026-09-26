---
title: '台風の進路を、15のモデルで一度に見る——GPV Weather「各国モデルの台風進路予想」'
description: '気象庁の予報進路は1本ですが、その裏では各国の数値予報モデルが何十本もの進路を計算しています。それをまとめて1枚の地図に重ねているのがGPV Weatherの「各国モデルの台風進路予想」。凡例の15レイヤーを全部ほどいてみたら、半分が2025年に運用化されたばかりのAIモデルでした。線の太さの意味、束の広がりの読み方、自分の基地から500kmの円を描く方法まで整理しました。'
pubDate: '2026-09-26'
category: '基礎知識'
tags: ['気象', '航空安全']
heroImage: '../../assets/posts/typhoon-model-tracks-hero.jpg'
---

台風のとき、気象庁の進路予報を見ます。<strong>中心の点と、予報円と、暴風警戒域。</strong>あれは1本の進路です。

でもその裏では、世界中の数値予報モデルが**何十本もの進路**を計算しています。それをまとめて1枚の地図に重ねているサイトを教えてもらいました。

> **GPV Weather「各国モデルの台風進路予想」**
> `https://www.gpvweather.com/typmodels.php`

開くと、太平洋がスパゲッティのような線で埋まります。最初に見たときは、正直なところ**何を見ればいいのか分かりませんでした。**

そこで凡例を全部ほどいてみたところ、**15のレイヤーのうち、ほぼ半分が2025年に運用化されたばかりのAIモデル**でした。今回はその中身と、読み方を整理します。

---

## 何が重なっているのか

情報メニューを開くと、チェックボックスがずらりと並びます。中身はこうでした。

<div class="typ-legend-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 545" width="100%" role="img" aria-label="各国モデルの台風進路予想の凡例一覧">
<rect x="0" y="0" width="560" height="545" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">同じ地図に、15本の系統が重なっている</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">太い線＝決定論またはアンサンブル平均　細い線＝アンサンブルの1メンバー</text>
<rect x="14" y="56" width="532" height="20" rx="3" fill="#f3f1ea"/>
<text x="22" y="70" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#14304a">欧州 ECMWF</text>
<line x1="22" y1="93.5" x2="74" y2="93.5" stroke="magenta" stroke-width="3.0"/>
<text x="84" y="97.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">ECMWF_IFS_HRES</text>
<text x="290" y="97.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・決定論</text>
<text x="546" y="97.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">magenta</text>
<line x1="22" y1="116.5" x2="74" y2="116.5" stroke="hotpink" stroke-width="0.5"/>
<text x="84" y="120.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">ECMWF_IFS_ENS</text>
<text x="290" y="120.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・アンサンブル51</text>
<text x="546" y="120.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">hotpink</text>
<line x1="22" y1="139.5" x2="74" y2="139.5" stroke="darkgreen" stroke-width="3.0"/>
<text x="84" y="143.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">ECMWF_AIFS_SNGL</text>
<text x="290" y="143.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">AI・決定論</text>
<text x="546" y="143.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">darkgreen</text>
<line x1="22" y1="162.5" x2="74" y2="162.5" stroke="mediumseagreen" stroke-width="0.5"/>
<text x="84" y="166.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">ECMWF_AIFS_ENS</text>
<text x="290" y="166.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">AI・アンサンブル51</text>
<text x="546" y="166.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">mediumseagreen</text>
<rect x="14" y="174" width="532" height="20" rx="3" fill="#f3f1ea"/>
<text x="22" y="188" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#14304a">米国 NCEP</text>
<line x1="22" y1="211.5" x2="74" y2="211.5" stroke="darkviolet" stroke-width="3.0"/>
<text x="84" y="215.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_GFS</text>
<text x="290" y="215.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・決定論</text>
<text x="546" y="215.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">darkviolet</text>
<line x1="22" y1="234.5" x2="74" y2="234.5" stroke="olive" stroke-width="3.0"/>
<text x="84" y="238.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_AIGFS</text>
<text x="290" y="238.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">AI・決定論</text>
<text x="546" y="238.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">olive</text>
<line x1="22" y1="257.5" x2="74" y2="257.5" stroke="steelblue" stroke-width="0.5"/>
<text x="84" y="261.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_GEFS</text>
<text x="290" y="261.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・アンサンブル</text>
<text x="546" y="261.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">steelblue</text>
<line x1="22" y1="280.5" x2="74" y2="280.5" stroke="mediumblue" stroke-width="3.0"/>
<text x="84" y="284.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_GEFS_MEAN</text>
<text x="290" y="284.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・平均</text>
<text x="546" y="284.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">mediumblue</text>
<line x1="22" y1="303.5" x2="74" y2="303.5" stroke="mediumaquamarine" stroke-width="0.5"/>
<text x="84" y="307.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_AIGEFS</text>
<text x="290" y="307.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">AI・アンサンブル31</text>
<text x="546" y="307.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">mediumaquamarine</text>
<line x1="22" y1="326.5" x2="74" y2="326.5" stroke="darkseagreen" stroke-width="3.0"/>
<text x="84" y="330.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_AIGEFS_MEAN</text>
<text x="290" y="330.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">AI・平均</text>
<text x="546" y="330.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">darkseagreen</text>
<line x1="22" y1="349.5" x2="74" y2="349.5" stroke="darkgray" stroke-width="3.0"/>
<text x="84" y="353.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">NCEP_HGEFS</text>
<text x="290" y="353.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">AI＋物理の62メンバー・平均</text>
<text x="546" y="353.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">darkgray</text>
<rect x="14" y="361" width="532" height="20" rx="3" fill="#f3f1ea"/>
<text x="22" y="375" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#14304a">カナダ CMC</text>
<line x1="22" y1="398.5" x2="74" y2="398.5" stroke="chocolate" stroke-width="0.5"/>
<text x="84" y="402.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">CANADA_CMC_GEPS</text>
<text x="290" y="402.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・アンサンブル</text>
<text x="546" y="402.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">chocolate</text>
<line x1="22" y1="421.5" x2="74" y2="421.5" stroke="darkorange" stroke-width="3.0"/>
<text x="84" y="425.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">CANADA_CMC_GEPS_MEAN</text>
<text x="290" y="425.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・平均</text>
<text x="546" y="425.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">darkorange</text>
<rect x="14" y="433" width="532" height="20" rx="3" fill="#f3f1ea"/>
<text x="22" y="447" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#14304a">米海軍 FNMOC</text>
<line x1="22" y1="470.5" x2="74" y2="470.5" stroke="palevioletred" stroke-width="0.5"/>
<text x="84" y="474.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">FNMOC_FENS</text>
<text x="290" y="474.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・アンサンブル</text>
<text x="546" y="474.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">palevioletred</text>
<line x1="22" y1="493.5" x2="74" y2="493.5" stroke="violet" stroke-width="3.0"/>
<text x="84" y="497.0" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9.5" fill="#1f2937">FNMOC_FENS_MEAN</text>
<text x="290" y="497.0" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">物理・平均</text>
<text x="546" y="497.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#d9d3c6">violet</text>
<text x="14" y="535" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" fill="#4b5563">※ 色と太さは2026年9月時点のサイトの定義。FNMOCは表示されないことがある</text>
</svg>
</div>

4つの機関から、15本の系統です。

| 機関 | 何者か |
|---|---|
| **ECMWF** | ヨーロッパ中期予報センター。世界でいちばん精度が高いとされる全球モデル |
| **NCEP** | 米国。GFS・GEFSの本家 |
| **CMC** | カナダ気象センター |
| **FNMOC** | **米海軍**の艦隊数値気象海洋センター |

米海軍のモデルまで並んでいるのは、ちょっと驚きました。

## 線の太さが、いちばん大事なルール

このサイトのコードを読んでみると、線の太さは**2種類しかありません。**

| 太さ | 意味 |
|---|---|
| **太い線（3.0）** | **決定論モデル**、または**アンサンブルの平均** |
| **細い線（0.5）** | **アンサンブルの1メンバー** |

ここが分かると、地図の見え方が変わります。

<strong>細い線を1本追いかけても意味がありません。</strong>あれは「初期値をちょっとだけ変えて計算したら、こうなった」という**51通りのうちの1本**です。ECMWFのアンサンブルなら51メンバー、NCEPのAIアンサンブルなら31メンバー。

見るべきは**束の広がり**のほうです。

<div class="typ-read-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 250" width="100%" role="img" aria-label="スパゲッティ図の読み方">
<rect x="0" y="0" width="560" height="250" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">見るのは1本の線ではなく、束の幅</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">細い線はアンサンブルの1メンバー。その1本を追う意味はない</text>
<rect x="20" y="56" width="250" height="150" rx="5" fill="#f7f9fb" stroke="#e5e1d6"/>
<text x="145" y="74" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#2a9d8f">束が細い</text>
<circle cx="216" cy="104" r="34" fill="none" stroke="#b65a3b" stroke-width="1.2" stroke-dasharray="4 3"/>
<circle cx="216" cy="104" r="2.5" fill="#b65a3b"/>
<text x="216" y="152" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#b65a3b">自分の基地＋500km</text>
<path d="M44 178 Q114 155 248 92" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 156 248 94" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 156 248 97" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 157 248 99" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 157 248 102" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 158 248 104" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 159 248 106" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 159 248 109" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 160 248 111" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 160 248 114" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 161 248 116" fill="none" stroke="#2a9d8f" stroke-width="0.7" opacity="0.75"/>
<path d="M44 178 Q114 158 248 104" fill="none" stroke="#2a9d8f" stroke-width="2.6"/>
<circle cx="44" cy="178" r="3.5" fill="#14304a"/>
<text x="42" y="193" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#14304a">現在位置</text>
<text x="145" y="224" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10" fill="#1f2937">方向はほぼ決まっている→早めに動ける</text>
<rect x="290" y="56" width="250" height="150" rx="5" fill="#f7f9fb" stroke="#e5e1d6"/>
<text x="415" y="74" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11.5" font-weight="700" fill="#b65a3b">束が広い</text>
<circle cx="486" cy="104" r="34" fill="none" stroke="#b65a3b" stroke-width="1.2" stroke-dasharray="4 3"/>
<circle cx="486" cy="104" r="2.5" fill="#b65a3b"/>
<text x="486" y="152" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#b65a3b">自分の基地＋500km</text>
<path d="M314 178 Q384 146 518 58" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 149 518 67" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 151 518 76" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 153 518 86" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 156 518 95" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 158 518 104" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 160 518 113" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 163 518 122" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 165 518 132" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 167 518 141" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 170 518 150" fill="none" stroke="#b65a3b" stroke-width="0.7" opacity="0.75"/>
<path d="M314 178 Q384 158 518 104" fill="none" stroke="#b65a3b" stroke-width="2.6"/>
<circle cx="314" cy="178" r="3.5" fill="#14304a"/>
<text x="312" y="193" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#14304a">現在位置</text>
<text x="415" y="224" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10" fill="#1f2937">まだ決まっていない→決めないという判断</text>
</svg>
</div>

- **束が細くまとまっている**——各モデルが同じ答えに収束している。**方向は、ほぼ決まっている**
- **束が扇のように開いている**——まだ決まっていない。**「決めない」という判断の根拠**になる

気象庁の予報円が大きいか小さいかも同じことを表していますが、**どちらの方向に割れているのか**まで見えるのは、こちらだけです。

## 半分が「AIモデル」だった

凡例を分解していて、いちばん驚いたのがここでした。**15本のうち6本がAIベースのモデル**です。しかもどれも、**この1年で運用化されたばかり**でした。

### ECMWF AIFS

ECMWFの <strong>AIFS（Artificial Intelligence Forecasting System）</strong>は、

- **決定論版が2025年2月**に運用化
- **アンサンブル版（AIFS ENS）が2025年7月1日**に運用化。**50の摂動メンバー＋1つのコントロール**で、解像度は**約30km**

物理ベースのIFS ENSが**約9km**なので、解像度はかなり粗い。それでもECMWF自身の評価では、<strong>上空の変数で最大25%</strong>の改善があったとしています。

### NOAAの3兄弟

米国側はもっと新しくて、**2025年12月17日12UTCのサイクル**から3つが同時に運用化されました（Service Change Notice 25-89）。

| モデル | 中身 |
|---|---|
| **AIGFS** | AIベースの**決定論**全球モデル |
| **AIGEFS** | AIベースの**アンサンブル（31メンバー）** |
| **HGEFS** | **AIGEFSと現業GEFSv12を合わせた62メンバー**のハイブリッド（各31メンバー） |

注目したのは、そのベースです。

> The models are based on **Google DeepMind's GraphCast** model.

**AIGFSとAIGEFSは、Google DeepMindのGraphCastがベース**だと、NWSの公式通知に明記されています。NCEPがNOAAの研究所とEPIC（Earth Prediction Innovation Center）と共同で開発したもので、Project EAGLEという取り組みから出てきました。

計算コストの差も強烈です。

> 16日先までの予報1回が、**現業GFSの0.3%の計算資源**で、**約40分**で終わる。

さらにAIGEFSは、従来のGEFSより**予報スキルが18〜24時間分**延びたとされています。

**HGEFSが1本の太線でしか描かれない理由**も、通知を読むと分かりました。HGEFSは**ensstat（平均とスプレッド）しか配信されていない**のです。メンバーごとのデータが外に出ていないので、細い線が引けない。

### ただし、AIモデルには明確な弱点がある

ここは、鵜呑みにしないために書いておきます。ECMWF自身がAIFS ENSについて挙げている限界です。

- **極端な降水を著しく過小予測する**（2023年のStorm Hansの事例）
- **10m風速では、物理ベースのIFS ENSのほうが依然として優秀**
- 7日より先の2m気温は性能が落ちる
- 乾燥域で微量の偽の降水が出る
- 複雑地形上の海面気圧に異常値が出ることがある

**10m風速が弱い**というのは、運航者にとって小さくない話です。つまり——

> AIモデルの線は<strong>「どこへ行くか」を見る材料</strong>にはなるが、<strong>「どれくらい荒れるか」を読む材料としては、まだ物理モデルに劣る。</strong>

台風の**進路の束**を見る道具として使い、**強さや風の見積りは気象庁の予報に戻る**——この分け方がいいと思います。

## 操作のポイント

実際に触ってみて、押さえておくと便利だったところです。

### ① 情報メニューの「Single ON」

地図の上にある「情報メニュー」を開くと、レイヤーのチェックボックスと一緒に3つのボタンがあります。

- **All ON**——全部表示
- **Single ON**——**1つだけ表示**
- **All OFF**——全部消す

初見でいちばん役に立つのは **Single ON** です。全部出すと本当に何も見えないので、**まずECMWF_IFS_ENSだけ**にして束の形を掴み、そこから足していくのがおすすめです。

### ② 時刻スライダーと再生

地図の上部にスライダーがあり、「マーカー日時」が動きます。右下に再生ボタン（◀◀ ◀ ▶ ▶▶ ↻）があって、**時間を進めながら束がどう広がっていくか**をアニメーションで見られます。

<strong>束は先に行くほど広がります。</strong>その広がり方の速さが、そのまま不確実性の増え方です。

### ③ 自分の基地に円を描く

これがいちばん実務的だと思いました。**距離を示す円**を任意の地点に置けます。

- 地図をクリック →「**ここに円**」
- または右上の「**〇**」ボタン

教えてもらったURLにも、すでに**東京を中心に500kmと1000kmの円**が仕込まれていました。

やることは単純です。<strong>自分の基地に円を描いて、束がその円に入る時刻を読む。</strong>束が細ければ「何日の何時ごろ」と読めますし、広ければ「26日夜から28日朝までのどこか」としか読めない。**その幅こそが、いま分かっていることの限界**です。

### ④ 熱帯擾乱発生の可能性（GTH）

情報メニューのいちばん上に「**熱帯擾乱発生の可能性(GTH)**」という項目があります。これは進路ではなく、**これから台風が生まれるかもしれない領域**を、週単位で色づけしたものです。

筆者が見た日は「09/30〜10/06（09/22時点）」「10/07〜10/13（09/22時点）」の2週分が選べました。**まだ台風になっていない段階から、次の週の備えを考える**のに使えます。

### ⑤ URLが、そのまま設定の保存になる

このサイトはURLのパラメータに表示状態を全部入れています。

| パラメータ | 意味 |
|---|---|
| `la` / `ln` | 地図の中心（緯度・経度） |
| `z` | ズーム |
| `b` | ベースマップ |
| `ci` | 円。`n経度_緯度,半径1,半径2`（km） |
| `i` | **表示するレイヤーのビットマスク**（数値を2進数にして、1桁ずつレイヤーのON/OFFに対応） |

つまり、<strong>自分の基地に円を描いて、見たいモデルだけ選んだ状態をブックマークしておけば、次からはそれが開きます。</strong>台風シーズンに毎回設定し直す必要がありません。

### ⑥ 擾乱ごとに分けたページもある

同時に複数の台風があると、全部が1枚に重なって判別できなくなります。そのために、擾乱ごとに分けたページが用意されています。

- `/typmodel_ecmwf_ens.php`——ECMWF IFSアンサンブル
- `/typmodel_ecmwf_aifs_ens.php`——ECMWF AIFSアンサンブル
- `/typmodel_jma.php`——気象庁台風進路予測図
- `/typmulti.php`——各国の台風進路予想
- `/typlink.php`——各国の台風関連リンク集

## サイト自身の但し書きが、いちばん大事

ページの冒頭に、赤い字でこう書いてあります。

> このページで公開しているデータは<strong>数値予報の結果そのままのものもあり、精度の低いデータが含まれる場合があります。</strong>
> 実際の進路予報は〔気象庁の予報〕を利用してください。

**これは飾りではありません。**

気象庁の台風進路予報は、複数のモデルを見比べたうえで、**予報官が判断して1本にまとめたもの**です。その過程では統計的な補正（ガイダンス）も入りますし、過去の似た事例との照合もある。

一方このページに出ているのは、**その手前の、生の計算結果**です。

> 関連記事：[MSMとGSM——モデルの出力は、そのままでは予報になっていない](/blog/msm-gsm-guidance-2026/)

だから使い分けはこうなります。

| 知りたいこと | 見るもの |
|---|---|
| **どこに、いつ、どれくらいの強さで来るのか** | **気象庁の予報** |
| **その予報が、どれくらい確からしいのか** | **このページの束の広がり** |

## ヘリの運航で、どう効くか

正直に言うと、<strong>当日や翌日の運航判断に、このページはほとんど関係ありません。</strong>その時間帯は気象庁の予報のほうが確実に精度が高い。

効くのは**もっと手前**です。

<strong>3日後から1週間先の予定を、動かすかどうか。</strong>整備の入れ方、機体の避難、乗員の手配、依頼元への連絡——このあたりは早めに決めたいけれど、早く決めすぎると空振りになる。

束が細く収束していれば、**早めに動く根拠**になります。束が広ければ、**「まだ決めない」と言う根拠**になります。

「まだ分からない」と「まだ決まっていない」は違います。<strong>後者は、地図を見れば分かる。</strong>そこがこのページの価値だと思いました。

あとひとつだけ。**細い線が自分の基地を通っていても、慌てなくていい**ということも覚えておきたいです。あれは51分の1です。

---

### 関連記事

- [MSMとGSM——モデルの出力は、そのままでは予報になっていない](/blog/msm-gsm-guidance-2026/)
- [Windyの「Forecast Model」を使い分けよう——ECMWF・GFS・ICON・HRRRの違いと選び方](/blog/windy-forecast-models-2026/)
- [SCW（SUPERC WEATHER）の使い方](/blog/scw-weather-2026/)
- [「レベル５特別警報」は、避難するための情報ではない](/blog/alert-level5-2026/)

### 出典

- GPV Weather「[各国モデルの台風進路予想](https://www.gpvweather.com/typmodels.php)」——レイヤー構成・色と線幅の定義・操作系・URLパラメータは、2026年9月26日に筆者が実際に開いて確認しました
- ECMWF「[ECMWF's AI forecasts become operational](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational)」（2025年2月）
- ECMWF Newsletter 185「[AIFS ENS becomes operational](https://www.ecmwf.int/en/newsletter/185/earth-system-science/aifs-ens-becomes-operational)」——メンバー数・解像度・改善幅・限界
- NOAA/NWS「[Service Change Notice 25-89: Implementation of AIGFS, AIGEFS, and HGEFS](https://www.weather.gov/media/notification/pdf_2025/scn25-89_AIGFS_AIGEFS_and_HGEFS.pdf)」（2025年12月9日発出・12月17日実施）——GraphCastベースであること、メンバー数、配信仕様
- NOAA「[NOAA deploys new generation of AI-driven global weather models](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models)」——計算コストとスキル延伸

*本記事は2026年9月26日時点の内容に基づきます。サイトの仕様やレイヤー構成は変更される可能性があります。実際の防災判断は、必ず[気象庁の台風情報](https://www.jma.go.jp/bosai/map.html#contents=typhoon)をご利用ください。*

ヒーロー画像：「Super Typhoon Chaba churns away in the western Pacific Ocean while Typhoon Aere passes over Taiwan」by NOAA（[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Super_Typhoon_Chaba_churns_away_in_the_western_Pacific_Ocean_while_Typhoon_Aere_passes_over_Taiwan_(2268-314).jpg) / パブリックドメイン）。掲載にあたり切り抜きとリサイズを行いました。

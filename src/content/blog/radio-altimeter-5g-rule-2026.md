---
title: 'アメリカは「ホバー自動操縦を止める」と書いた——電波高度計と5G、決着の中身'
description: '電波高度計と5Gの周波数が近すぎる問題に、FAAが最終規則で答えを出しました。「干渉に強いこと」ではなく、3000〜5600MHzを17区分に割った電力束密度の表を条文に書き込んでいます。期限は2030年と2034年の2段階。ただしヘリコプターは、適合期限が2034年でも2030年末からカテゴリーA/B離着陸・捜索救難モード・ホバー自動操縦が使えなくなります。日本の周波数配置はガードバンド100MHzで上下から挟まれており、ヘリの保護は「離発着地点として認識されている場所から20〜50m」。一次資料で整理しました。'
pubDate: '2026-09-23'
category: '最近の変更点'
tags: ['航空安全', '法規']
heroImage: '../../assets/posts/radio-altimeter-5g-rule-hero.jpg'
---

5Gの電波が電波高度計に干渉するかもしれない——2021年末から続いていたこの話に、**アメリカが答えを出しました。**

FAAは2026年7月31日、「**干渉に耐える電波高度計システムの要件**」という最終規則を公布しました。**2026年9月29日に発効**しています。

規則の書きぶりで、いちばん驚いたのはここでした。

> 「干渉に強い装置にすること」ではなく、<strong>どの周波数で、どの強さの電波まで耐えるのか</strong>を、表にして条文に書き込んだ。

そして、ヘリコプターにとっての本題は別のところにありました。<strong>適合期限は2034年なのに、2030年末から一部の運用ができなくなります。</strong>カテゴリーA／Bの離着陸、捜索救難の自動操縦モード、そして**ホバー自動操縦**です。

一次資料（連邦官報 91 FR 48656）を読んで整理しました。

---

## そもそも、何が起きているのか

電波高度計が使うのは **4,200〜4,400 MHz**。その真下の 3,700〜4,200 MHz が、いわゆる**Cバンド**です。

アメリカでは2020年に、このうち下側の 3,700〜3,980 MHz が5Gに割り当てられました。その結果、2021年末から空港周辺で基地局の出力制限・展開制限が1年以上続き、多くの機体で電波高度計の交換が必要になりました。規則はこの経験を踏まえ、今回FAAが何もしなければ「<strong>落札者は、FCCが指定した日に新しい無線サービスを開始できるという確信をほとんど持てない</strong>」ことになる、と書いています。

今回はその続きです。2025年7月4日に成立した法律（One Big Beautiful Bill Act）の第40002条が、FCCに対して**上側Cバンド（3,980〜4,200 MHz）で100 MHz以上を2027年7月4日までに競売せよ**と指示しました。

これを受けたFCCの2026年7月の報告書兼命令は、こう区切りました。

| 周波数 | 用途 |
|---|---|
| **3,980〜4,140 MHz**（160 MHz） | **地上系の無線（5G）に開放** |
| 4,140〜4,160 MHz（20 MHz） | **ガードバンド** |
| 4,160〜4,200 MHz（40 MHz） | 固定衛星業務へ再配置 |

つまり、<strong>地上から強い電波を出す設備の上端が、4,140 MHzまで上がってきます。</strong>電波高度計の帯域まで、あと60 MHz。

<div class="ra-band-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 292" width="100%" role="img" aria-label="日本と米国の周波数配置を比べた図">
<rect x="0" y="0" width="560" height="292" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">電波高度計の隣に、何がいるのか</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">縦の帯＝電波高度計帯（4200〜4400 MHz）。数字は地上系無線の上端から高度計帯までのあき</text>
<rect x="346.0" y="56" width="80.0" height="168" fill="#efe7df" stroke="#b65a3b" stroke-width="1" stroke-dasharray="3 3"/>
<text x="386.0" y="52" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" font-weight="700" fill="#b65a3b">電波高度計</text>
<text x="14" y="87" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#14304a">日本</text>
<rect x="106.0" y="70" width="200.0" height="26" rx="2" fill="#3a7ca5" opacity="0.85"/>
<text x="206.0" y="87" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#ffffff">5G 3.7GHz帯</text>
<rect x="466.0" y="70" width="40.0" height="26" rx="2" fill="#3a7ca5" opacity="0.85"/>
<text x="486.0" y="66" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#3a7ca5">5G 4.5GHz帯</text>
<line x1="306.0" y1="103" x2="346.0" y2="103" stroke="#4b5563" stroke-width="1"/>
<text x="326.0" y="115" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" font-weight="700" fill="#4b5563">100 MHz</text>
<text x="14" y="141" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#14304a">米国（現行）</text>
<rect x="146.0" y="124" width="112.0" height="26" rx="2" fill="#3a7ca5" opacity="0.85"/>
<text x="202.0" y="141" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#ffffff">下側Cバンド 5G</text>
<line x1="258.0" y1="157" x2="346.0" y2="157" stroke="#4b5563" stroke-width="1"/>
<text x="302.0" y="169" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" font-weight="700" fill="#4b5563">220 MHz</text>
<text x="14" y="195" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="11" font-weight="700" fill="#14304a">米国（2030年末〜）</text>
<rect x="146.0" y="178" width="112.0" height="26" rx="2" fill="#3a7ca5" opacity="0.85"/>
<text x="202.0" y="195" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#ffffff">下側C</text>
<rect x="258.0" y="178" width="64.0" height="26" rx="2" fill="#b65a3b" opacity="0.85"/>
<text x="290.0" y="195" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="8.5" fill="#ffffff">上側C（新）</text>
<rect x="322.0" y="178" width="8.0" height="26" rx="2" fill="#a07000" opacity="0.85"/>
<rect x="330.0" y="178" width="16.0" height="26" rx="2" fill="#2a9d8f" opacity="0.85"/>
<line x1="322.0" y1="211" x2="346.0" y2="211" stroke="#4b5563" stroke-width="1"/>
<text x="334.0" y="223" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" font-weight="700" fill="#4b5563">60 MHz</text>
<line x1="66.0" y1="232" x2="546.0" y2="232" stroke="#d9d3c6" stroke-width="1"/>
<line x1="66.0" y1="232" x2="66.0" y2="236" stroke="#d9d3c6"/>
<text x="66.0" y="248" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">3500</text>
<line x1="146.0" y1="232" x2="146.0" y2="236" stroke="#d9d3c6"/>
<text x="146.0" y="248" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">3700</text>
<line x1="226.0" y1="232" x2="226.0" y2="236" stroke="#d9d3c6"/>
<text x="226.0" y="248" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">3900</text>
<line x1="306.0" y1="232" x2="306.0" y2="236" stroke="#d9d3c6"/>
<text x="306.0" y="248" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4100</text>
<line x1="386.0" y1="232" x2="386.0" y2="236" stroke="#d9d3c6"/>
<text x="386.0" y="248" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4300</text>
<line x1="466.0" y1="232" x2="466.0" y2="236" stroke="#d9d3c6"/>
<text x="466.0" y="248" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4500</text>
<line x1="546.0" y1="232" x2="546.0" y2="236" stroke="#d9d3c6"/>
<text x="556" y="248" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4700 MHz</text>
<text x="14" y="264" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9" fill="#4b5563">※ 米国（2030年末〜）の行：4140〜4160はガードバンド、4160〜4200は固定衛星業務</text>
</svg>
</div>

日本の配置と比べると、事情がよく分かります。**日本は5Gが上下から挟んでいて、ガードバンドは100 MHz**です。アメリカは現在220 MHz空いていますが、**2030年末からは60 MHzになります。**

だから機器の側を作り直す、というのが今回の規則です。

## 「干渉に強い」を、17区分の数値にした

新設された **第91.220条(b)** が、この規則の中心です。条文はこう書きます。

> 電波高度計システムは、この項の表1に定める干渉環境において、**地表からの高度0〜500フィートで動作しなければならない**。

そして表1が、**3,000 MHzから5,600 MHzまでを17区分**に分け、それぞれ「これだけの強さの電波が来ていても測れ」という電力束密度（単一偏波、二乗平均平方根、dBW/m²/MHz）を定めています。

全文はこうです。

| 周波数の区分（MHz） | 電力束密度 |
|---|---|
| 3000 ≤ f < 4000 | 9.5 |
| 4000 ≤ f < 4100 | 9.5 |
| 4100 ≤ f < 4150 | 9.5 |
| 4150 ≤ f < 4160 | 6.5 |
| 4160 ≤ f < 4170 | −1 |
| 4170 ≤ f < 4180 | −7 |
| 4180 ≤ f < 4190 | −17 |
| 4190 ≤ f < 4200 | −34 |
| **4200 ≤ f ≤ 4400** | **−82** |
| 4400 < f ≤ 4410 | −33 |
| 4410 < f ≤ 4430 | −21 |
| 4430 < f ≤ 4440 | −8 |
| 4440 < f ≤ 4450 | −1 |
| 4450 < f ≤ 4460 | 6.5 |
| 4460 < f ≤ 4500 | 9.5 |
| 4500 < f ≤ 4600 | 9.5 |
| 4600 < f ≤ 5600 | 9.5 |

<div class="ra-mask-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 230" width="100%" role="img" aria-label="干渉耐性マスクの形を示すグラフ">
<rect x="0" y="0" width="560" height="230" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">干渉耐性マスク（第91.220条(b)・表１）</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10" fill="#4b5563">縦軸：耐えるべき電力束密度（dBW/m²/MHz）　下にいくほど厳しい</text>
<rect x="181.5" y="54" width="239.0" height="128" fill="#efe7df"/>
<line x1="62" y1="56.6" x2="540" y2="56.6" stroke="#e5e1d6" stroke-width="1"/>
<text x="56" y="59.6" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">10</text>
<line x1="62" y1="69.8" x2="540" y2="69.8" stroke="#e5e1d6" stroke-width="1"/>
<text x="56" y="72.8" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">0</text>
<line x1="62" y1="96.2" x2="540" y2="96.2" stroke="#e5e1d6" stroke-width="1"/>
<text x="56" y="99.2" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">-20</text>
<line x1="62" y1="122.6" x2="540" y2="122.6" stroke="#e5e1d6" stroke-width="1"/>
<text x="56" y="125.6" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">-40</text>
<line x1="62" y1="149.0" x2="540" y2="149.0" stroke="#e5e1d6" stroke-width="1"/>
<text x="56" y="152.0" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">-60</text>
<line x1="62" y1="175.4" x2="540" y2="175.4" stroke="#e5e1d6" stroke-width="1"/>
<text x="56" y="178.4" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">-80</text>
<path d="M62.0 57.3 L121.8 57.3 L121.8 61.3 L133.7 61.3 L133.7 71.2 L145.7 71.2 L145.7 79.1 L157.6 79.1 L157.6 92.3 L169.6 92.3 L169.6 114.7 L181.5 114.7 L181.5 178.0 L420.5 178.0 L420.5 113.4 L432.4 113.4 L432.4 97.5 L456.4 97.5 L456.4 80.4 L468.3 80.4 L468.3 71.2 L480.2 71.2 L480.2 61.3 L492.2 61.3 L492.2 57.3 L540.0 57.3" fill="none" stroke="#b65a3b" stroke-width="2.2" stroke-linejoin="round"/>
<line x1="62" y1="182" x2="540" y2="182" stroke="#d9d3c6"/>
<line x1="62.0" y1="182" x2="62.0" y2="186" stroke="#d9d3c6"/>
<text x="62.0" y="198" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4100</text>
<line x1="181.5" y1="182" x2="181.5" y2="186" stroke="#d9d3c6"/>
<text x="181.5" y="198" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4200</text>
<line x1="301.0" y1="182" x2="301.0" y2="186" stroke="#d9d3c6"/>
<text x="301.0" y="198" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4300</text>
<line x1="420.5" y1="182" x2="420.5" y2="186" stroke="#d9d3c6"/>
<text x="420.5" y="198" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4400</text>
<line x1="540.0" y1="182" x2="540.0" y2="186" stroke="#d9d3c6"/>
<text x="556.0" y="198" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">4500 MHz</text>
<text x="301.0" y="68" text-anchor="middle" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="9.5" font-weight="700" fill="#b65a3b">電波高度計自身の帯域　−82</text>
<text x="95.5" y="70.3" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#4b5563">9.5</text>
<text x="173.1" y="108.7" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#1f2937">−34</text>
<text x="430.1" y="107.4" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="8.5" fill="#1f2937">−33</text>
<text x="14" y="218" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10" fill="#4b5563">※ 3000〜4150 MHz と 4460〜5600 MHz はいずれも 9.5で一定。全体17区分</text>
</svg>
</div>

グラフにすると、**浴槽のような形**になります。読み方はこうです。

- **自分の帯域（4,200〜4,400 MHz）は −82**。ここに強い電波が来ることは想定しない。**電波高度計は自分の帯域内の干渉をフィルタで落とせない**ため、ここは無線側で守るしかありません
- **境界に向かう区間は階段状**。4,150から10 MHz刻みで 6.5 → −1 → −7 → −17 → −34 と下がっていきます。境界に近づくほど、耐えるべき電波は弱くなる＝要求は緩む
- **離れた帯域は 9.5 で一定**

規則の中では、この表を<strong>干渉耐性マスク（ITM）</strong>と呼びます。

### なぜ数値にしたのか

「干渉に強いこと」では、<strong>試験の条件が決まりません。</strong>周波数ごとの電力束密度と高度の範囲が数字で決まっていれば、装置メーカーは同じ条件で測って合否を出せます。運航者も「うちの機体は適合しているのか」を一意に判定できる。

案の段階から1か所だけ変わっています。<strong>4,170〜4,180 MHz を −1 から −7 に緩めました。</strong>ハネウェルが試験結果を出して「この要求のままだと次世代機の供給が遅れる」と指摘し、しかもこの帯域は上側Cバンドの範囲外なので無線側との両立に影響しない、という理由です。この1区分が増えたことで、16区分が17区分になりました。

**0〜500フィートAGL**という条件にも意味があります。電波高度計が本当に効くのはその高度で、そこは同時に**地上の基地局にいちばん近づく**高度でもあります。

## 期限は2段階

<div class="ra-timeline-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 300" width="100%" role="img" aria-label="規則の期限の年表">
<rect x="0" y="0" width="560" height="300" fill="#ffffff"/>
<text x="14" y="22" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="14" font-weight="700" fill="#14304a">期限は２段階。しかしヘリは2030年末から制限がかかる</text>
<text x="14" y="40" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" fill="#4b5563">適合期限は2034年だが、適合していない機体は2030年末から一部の運用ができなくなる</text>
<line x1="150" y1="60" x2="150" y2="258" stroke="#d9d3c6" stroke-width="2"/>
<circle cx="150" cy="74" r="5" fill="#3a7ca5"/>
<text x="138" y="78" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" font-weight="700" fill="#3a7ca5">2026年9月29日</text>
<text x="164" y="78" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="400" fill="#1f2937">規則が発効</text>
<circle cx="150" cy="118" r="5" fill="#3a7ca5"/>
<text x="138" y="122" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" font-weight="700" fill="#3a7ca5">2027年7月4日</text>
<text x="164" y="122" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="400" fill="#1f2937">上側Cバンドの競売完了期限</text>
<circle cx="150" cy="162" r="5" fill="#b65a3b"/>
<text x="138" y="166" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" font-weight="700" fill="#b65a3b">2030年12月30日</text>
<text x="164" y="166" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#1f2937">第１期限　定期便（第121部・第129部の大型）</text>
<circle cx="150" cy="206" r="5" fill="#b65a3b"/>
<text x="138" y="210" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" font-weight="700" fill="#b65a3b">2030年12月31日</text>
<text x="164" y="210" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#1f2937">新しい無線が出る。同日からヘリの運用制限開始</text>
<circle cx="150" cy="250" r="5" fill="#b65a3b"/>
<text x="138" y="254" text-anchor="end" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10" font-weight="700" fill="#b65a3b">2034年10月31日</text>
<text x="164" y="254" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif" font-size="10.5" font-weight="700" fill="#1f2937">第２期限　それ以外の全機（ヘリを含む）</text>
</svg>
</div>

| 条文 | 対象 | 期限 |
|---|---|---|
| 第121.326条 | 第121部（定期便）の航空機 | **2030年12月30日** |
| 第129.16条(a) | 第129部（外国運航者）のうち旅客席30以上または搭載量7,500ポンド超 | **2030年12月30日** |
| 第91.220条(a) | 第91部の運航規則に服するその他すべて（第125・133・135・136・137・194部を含む） | **2034年10月31日** |
| 第129.16条(b) | 第129部のうち第1期限にかからないもの | **2034年10月31日** |

条文はいずれも禁止の形です。

> この日より後は、局長が別段の許可をしないかぎり、何人も、**本土48州とコロンビア特別区の空域**において、電波高度計を装備した航空機を、その電波高度計システムが第91.220条(b)の性能要件を満たさないまま運航してはならない

**アラスカ・ハワイ・海外領土は対象外**です。今回の周波数再配置が本土48州とDCに限られているためで、規則もそう明記しています。

第1期限の **2030年12月30日**は、偶然の日付ではありません。**FCCが上側Cバンドでの新しい無線サービスを認める最も早い日（2030年12月31日）の、前日**です。新しい電波が出る前に、飛ぶ回数が多く、干渉が起こりうる環境での運航が多い機体を先に揃える——という順番になっています。

なお、**公共用航空機（軍用機を含む）も対象**です。米国防省は機体交換に30〜40億ドル、予算計上後8年かかると見積もっています。

## ヘリコプターに何が起きるか

ここからが本題です。**ヘリコプターの適合期限は2034年10月31日**——第2期限のほうです。

ところが規則には、こう書いてあります。

> FAAは、この最終規則の新しい性能要件を満たす電波高度計を装備していないヘリコプターについて、**2030年12月31日をもって**現行のヘリコプター向け耐空性改善命令を置き換える命令を出す予定である。

そして、置き換え後に何が禁止されるかが具体的に列挙されています。

> **干渉耐性マスクに適合した電波高度計を持たないヘリコプターは、以下を禁止される。**
>
> - **電波高度計のデータを使う手順による離着陸**（カテゴリーA、カテゴリーB、またはロータークラフト飛行規程や運用規程に定めるPerformance Classによるもの）
> - **捜索救難の自動操縦モード（search and rescue autopilot modes）の使用**
> - **ホバー自動操縦モード（hover autopilot modes）の使用**
> - 電波高度計による最低気象条件を必要とする一定の手順

つまり、**適合期限は2034年でも、実質的な期限は2030年末**ということになります。それ以降、適合していない機体は「飛べるが、できないことがある」状態で4年近くを過ごすことになる。

そして重要なのは、**この制限が48州全域に一律でかかる**点です。規則はその理由をはっきり書いています。

> FAAは上側Cバンドの基地局の位置を追跡する意図がないため、これらの制限は本土48州とコロンビア特別区の全域に適用される。

**「基地局が近くにないから大丈夫」という運用は、成り立たせない**という判断です。基地局の場所を追いかけて例外を切る運用は、下側Cバンドのときに散々やって、結局それが無線側の投資判断を止めた——その反省が読み取れます。

### 夜間飛行（NVG）は免除申請が要る

もうひとつ、ヘリコプターの現場に直接効く話があります。<strong>第91.205条(h)(7)はNVG運航に電波高度計を要求しています。</strong>適合機でない場合、この要件からの免除（exemption）が必要になります。

規則は、すでに複数の免除を発行しており、**その多くは発行から2年間有効**だと述べています。そのうえで、「ヘリコプターのNVGコミュニティにおける改修の進み具合を見ながら、今後の申請を検討する」としています。

**恒久的な逃げ道ではない**、という含みです。

### FAAはヘリをどう評価したか

ひとつ補足しておくと、FAAは**ヘリコプターについては現行のヘリコプターADの制限で最終期限まで足りる**と判断しています。

> FAAは上側Cバンドの無線サービスによるヘリコプター運航への追加リスクを評価し、**元のヘリコプターADの制限で、最終適合期限まで不安全状態に十分対処できる**と判断した。

飛行機側は機種ごとのADで追加制限（テールストライク防止装置の誤作動、フライトディレクターの誤ガイダンス、自動フレアの誤作動や喪失、オートスロットルの低速保護の喪失など）が上乗せされますが、ヘリコプターは既存のADの内容をそのまま引き継ぐ、という整理です。

## お金は誰が払うのか

**新しく帯域を得る側です。**

FCCの命令は、米国籍の民間機の所有者・運航者向けに**電波高度計の改修リベート制度**を作りました。原資は**競売完了から6〜12か月以内**に手当てされる見込みで、競売自体は法律で**2027年7月4日まで**に完了することになっています。適合装置を装着した所有者は、トランシーバの費用と機体改造費を補填する一括払いを受け取れます。

ただし——

> FCCの命令により、**この改修リベート制度は外国運航者には適用されない。**

日本の航空会社が米国に乗り入れる機体は、**全額自己負担**です。規則は「米国運航に充てる機体だけを交換することで総額を抑える選択肢がある」と、わざわざ助け舟のような一文を添えています。

費用の見積りはこうです。

| 区分 | 台数 | 費用 |
|---|---|---|
| 第1期限（国内第121部 18,423台＋外国第129部 11,135台） | 29,558台 | 23.7億〜35.5億ドル |
| 第2期限（飛行機 28,146台＋**回転翼 5,106台**） | 33,252台 | 24.6億〜35.8億ドル |
| **民間全体** | | **48.2億〜71.3億ドル** |

飛行機は**1台あたり8万〜12万ドル**（工賃込み）。案の段階では8万ドルだけでしたが、ルフトハンザが「4〜5倍になりうる」、ATSGが「9万6,950ドル程度」、複数団体が「12万ドルまで」とコメントし、**関税や付加費用を含めると10万ドルを超える**という価格情報も提出されたため、上限を12万ドルに引き上げています。

**第2期限の群に、回転翼が5,106台**含まれている——これが米国のヘリコプター業界が抱えている規模です。

## 日本はどうなっているのか

ここが、日本で飛んでいる者としては気になるところです。

### 周波数の配置は、日本のほうが窮屈

総務省の情報通信審議会向けに電子航法研究所（ENRI）が提出した資料が、各国を並べて比較しています。

| | 5Gに割り当てられた帯域 | 高度計帯までのあき |
|---|---|---|
| **日本** | 3.6〜4.1 GHz ＋ **4.5〜4.6 GHz** | **100 MHz（上下から挟む）** |
| 米国（当時） | 3.7〜3.98 GHz | 200 MHz（下側のみ） |
| フランス | 3.49〜3.8 GHz | 400 MHz（下側のみ） |

<strong>日本だけが、電波高度計の帯域を上下から挟んでいます。</strong>しかもガードバンドは100 MHzで、当時の3か国でいちばん狭い。

ではなぜ日本で問題が起きていないのか。**基地局の側を絞っているから**です。

| | 日本 | 米国（当時） | フランス |
|---|---|---|---|
| 送信電力（EIRP） | 55 dBm/MHz | 60.3 | 58 |
| **不要発射強度** | **−39 dBm/MHz以下** | −12.9以下 | −12.9以下 |
| 下側チルト義務 | なし | なし | あり |

<strong>日本の基地局は、高度計の帯域へ落ち込む不要発射を、米仏より26 dB低く抑えています。</strong>これが実質的なガードバンドの代わりになっていた、という構図です。

一方、今回のFCC命令が上側Cバンドの基地局に課したのは、<strong>最大EIRP 65 dBm/MHz、空中線高450フィートAGL以下</strong>という条件でした。出力そのものは、日本の基地局より大きくなります。

ただし今回、<strong>その関係が逆転します。</strong>FCCの新しい命令は、上側Cバンドの基地局に **−46 dBm/MHz（伝導）または −28.4 dBm/MHz（二偏波EIRP）** という不要発射限度を課し、**下側Cバンドの限度も2020年の −13 dBm/MHz から −46 dBm/MHz へ引き下げました。**

単純に数字を並べれば、**米国の新しい基準のほうが、日本の −39 dBm/MHz より厳しい**ことになります。測定の定義が完全に同じかまでは確認できていないので断定はしませんが、少なくとも「アメリカは緩い」という前提はもう使えません。

### ヘリコプターの保護は「50メートル」

日本側の共用条件は、**平成30年7月31日の情報通信審議会報告**にまとまっています。結論部分を引きます。

> — 電波高度計が用いる周波数と５Ｇシステムが用いる周波数の間に**100MHz程度の周波数離調**を設ける。
> — 帯域内干渉の影響の回避のため、**基地局へのフィルタ挿入**を行い、不要発射の強度を低減させる（スモールセル基地局で30dB程度、マクロセル基地局で35dB程度低減）。
> — 帯域外干渉の影響の回避のため、<strong>空港周辺（１km程度）</strong>において、航空機の進入経路の**周囲100〜200m程度**の範囲にはマクロセル基地局の設置を回避する。
> — <strong>ヘリコプターが着陸する地点と基地局との間に確保される離隔距離を加味する（スモールセル基地局20m程度以上、マクロセル基地局50m程度以上）。</strong>本離隔距離を確保するため、**ヘリコプターが離発着する地点として認識されている場所**の同一／隣接の敷地には、基地局の設置を回避する。

ヘリコプターの保護は、**「離発着する地点として認識されている場所」から20〜50メートル**です。

ここは、正直に読んでおきたいところだと思いました。<strong>「認識されている場所」</strong>という限定がついている。定置場やヘリポートは入るでしょうが、**その日その場所に降ろす場外離着陸場は、この条件の前提には入っていません。**

もっとも、同じ報告の中で、干渉が問題になるのは**進入・着陸の低高度**という前提で評価が組まれています。場外での運用がただちに危険だという話ではありません。ただ、**制度が守っているのはどこまでか**は、知っておいたほうがいい種類の情報だと思います。

なお、国内免許の電波高度計は、この報告の時点で**約1,100局**でした。

### ENRIの試算では、ヘリがいちばん苦しい

同じENRIの資料に、**RTCA（米国）の評価結果に日本の基地局諸元を当てはめた**試算が載っています。所要改善量（これだけ足りない、という不足分）です。

| 評価カテゴリ | 帯域外（日本規格・200 MHz離調） |
|---|---|
| カテゴリ1：大型固定翼 | 9 dB |
| カテゴリ2：中型以下固定翼 | 43 dB |
| **カテゴリ3：ヘリコプタ** | **40 dB** |

**日本の基地局は帯域内の干渉電力を大きく下げられるが、帯域外については大きくは変わらない**——というのがENRIの結論でした。そして100 MHz離調では、米国に実機試験結果がないため詳細評価ができず、**200 MHzより影響は大きいと推定される**としています。

これは2021〜22年ごろの資料です。<strong>日本で実際に干渉が報告されたという話は、筆者が確認した範囲では見当たりません。</strong>数字の上での余裕がないことと、実際に起きることは別です。

### 日本に同じ義務づけはあるか

**筆者が確認した範囲では、見当たりませんでした。**

FAA自身も、規則の中でこう書いています。

> FAAは、**この新しい電波高度計の性能標準を採用・要求する最初の国となる**ことで、米国の航空基準と他国の基準との将来の相違を防ぎ、他の民間航空当局との将来の整合の基準を設定し、高度計帯の近くで同様の周波数再配分を検討している各国の周波数当局に情報を提供することになると判断した。

<strong>「最初の国」</strong>と自認したうえで、他国が追ってくることを前提にしています。装置の規格づくり自体は、RTCA SC-239とEUROCAE WG-119という国際的な枠組みで進んでいます。日本の運航者が使う電波高度計も、**同じサプライヤーの同じ製品**です。

そして日本に、**JCAB（国土交通省航空局）はこの規則案に意見を出しています。**

> JCABとAAAEはいずれも、改修用の新しい電波高度計が十分に供給されるよう、**合理的な期限を設定すること**をFAAに求めた。

> JCABは、第1期限の達成が困難であることが判明した場合には、**米国空域において電波高度計を必要とする運航を禁止することが必要になるかもしれない**と述べた。

かなり踏み込んだ意見です。ANA（全日本空輸）も「部品が揃ってから改修に数か月の猶予を」と意見を出しています。

## 現場としてどう受け取るか

整理するとこうなります。

<strong>いま、日本で飛んでいる分には何も変わりません。</strong>この規則が効くのは本土48州とDCの空域だけで、日本の制度は2018年の共用条件のまま動いています。

<strong>変わりうるのは、機材更新のタイミングです。</strong>2030年以降、電波高度計は「干渉耐性マスクに適合しているかどうか」で二分されます。新造機に載ってくるのは適合品になるでしょうし、**中古機を入れるときには「これは適合品か」が値段の話になる**はずです。

<strong>米国に持っていく機体は、別の話です。</strong>リベートの対象外なので全額自己負担。しかも米国の要件を満たしていない機体は、2030年末以降、**カテゴリーA離着陸も、捜索救難の自動操縦も、ホバー自動操縦も使えません。**

そして、いちばん記憶しておきたいのはここだと思いました。

> **FAAは、基地局の位置を追跡しないと決めた。**

下側Cバンドのときは「この空港の周りだけ制限」というやり方をしました。それは無線側にとっても航空側にとっても不確かさを残し、結局どちらの計画も止めた。今回はそれをやめて、**機器の側に数値を課し、期限を切り、期限までは運用制限でしのぐ**という建て方に変えています。

「配慮する」で済ませずに数字を書く、というのは、後から検証できるという意味でもあります。**日本で同じ議論が起きたとき、比べる相手ができた**——今回いちばんの収穫は、そこかもしれません。

---

### 関連記事

- [電波は「上空で使う」と話が変わる——携帯電話の上空利用を整理する](/blog/radio-altitude-cellular-2026/)
- [上空150m以上での携帯電話利用が解禁——総務省の規制改正とヘリコプターへの意味](/blog/lte-altitude-reform-2022/)

### 出典

- 米国連邦官報 91 FR 48656「Requirements for Interference-Tolerant Radio Altimeter Systems」（FAA・RIN 2120-AM21・改正番号91-384/121-396/129-56・最終規則・2026年7月31日公布・2026年9月29日発効）。条文・表1の17区分・適合期限・運用制限・費用見積り・JCAB／ANAの意見は、すべて同規則の本文で確認しました
- 総務省 情報通信審議会 情報通信技術分科会「平成30年度 新世代モバイル通信システム委員会報告」（平成30年7月31日）第4.4節「航空機電波高度計との干渉検討」
- 電子航法研究所「電波高度計と5Gモバイルシステムの共用検討についての最新動向——各国における基地局との共用条件比較」（情報通信審議会 新世代モバイル通信システム委員会 技術検討作業班 資料26-7）
- 勧告ITU-R M.2059（4,200〜4,400 MHz帯を使用する電波高度計の運用・技術特性および保護基準）

*本記事は2026年9月23日時点の公開情報に基づきます。米国の規則の適用は本土48州とコロンビア特別区の空域に限られ、日本国内の運航に直接の効力はありません。日本側の数値は、上記の2018年報告および2021〜22年ごろのENRI資料に基づくもので、その後の改定の有無までは確認していません。*

ヒーロー画像：「Telecommunications mast at sunset」by W.carter（[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Telecommunications_mast_at_sunset.jpg) / CC BY-SA 4.0）。本記事への掲載にあたり、切り抜きとリサイズを行いました。

---
title: 'ADS-B Exchangeの使い方——空港コードで飛べば、日本の空もすぐ見える'
description: 'Flightradar24で見えない機体も映る「ADS-B Exchange」。無料・ログイン不要で使えますが、英語なので敬遠されがちです。空港コードでのジャンプ、機体クリックで出る詳細パネルの読み方、キーボードショートカットまで、実際に操作しながら手順を整理しました。FMS選択高度・IAS・QNH・風まで見えるのが、このサイトの本当の強みです。パネルの構成、航法三角形、高度の基準面、選択高度の読み方を図で追加しました。'
pubDate: '2026-08-10'
updatedDate: '2026-09-16'
category: '基礎知識'
tags: ['航空安全']
heroImage: '../../assets/posts/adsbexchange-guide-hero.jpg'
---

以前、[Flightradar24はなぜ機体を映せるのか](/blog/flight-tracking-mlat-2026/)という記事で、**ADS-B Exchange**というサービスに軽く触れた。「無検閲（unfiltered）を売りにしていて、軍用機や要人機もそのまま表示される」という紹介だ。

ただ、あの記事では**使い方までは書かなかった**。実際に開いてみると全部英語で、ボタンがアルファベット1文字だけ並んでいる。**何がどこにあるか分からない**まま閉じてしまった人も多いのではないかと思う。

そこで今回は、**実際に操作しながら手順を整理した**。結論から言うと、**無料・ログイン不要**で、覚えることは驚くほど少ない。そして——**パイロットにとっての本当の価値は「無検閲」ではなかった**というのが、今回いちばんの発見だった。

## まず開く場所を間違えない

最初のつまずきポイントがここだ。

**地図は `globe.adsbexchange.com`** にある。トップページの `adsbexchange.com` は会社・サービスの紹介ページで、地図そのものではない。**いきなり `globe.` から入る**のが早い。

開くと世界地図に大量の機体が表示される。右上に **Total Aircraft**（全世界で捕捉中の機数）と **On Screen**（いま画面内にいる機数）が出る。筆者が試したときは全世界で**13,000機超**だった。

**ログインは不要**。無料で全機能が使える。有料（Premium）は「広告が消える」「衛星写真レイヤーが使える」の2点で、**位置情報の中身は無料と同じ**である。

## 手順①：空港コードで日本へ飛ぶ

初期表示はアメリカだ。日本を見たいなら、いちばん速いのが**空港コードでのジャンプ**である。

右のサイドバーで **Search** タブを選ぶと、下のほうに

> **Jump to Airport or Latitude, Longitude**

という入力欄がある。ここに **`RJTT`** と入れて **Jump** を押す。これで羽田上空に飛ぶ。

入れるのは**4文字のICAOコード**だ。日本の主な空港はこうなる。

| 空港 | コード | 空港 | コード |
|---|---|---|---|
| 羽田 | **RJTT** | 成田 | **RJAA** |
| 伊丹 | **RJOO** | 関西 | **RJBB** |
| 中部 | **RJGG** | 新千歳 | **RJCC** |
| 福岡 | **RJFF** | 那覇 | **ROAH** |
| 仙台 | **RJSS** | 八尾 | **RJOY** |

**緯度経度でも飛べる**ので、ヘリポートや山岳地帯など空港コードがない場所を見たいときは、そのまま座標を入れればいい。

実際に `RJTT` で飛んでみると、地図の地名は**日本語で表示される**（OpenStreetMapベースのため）。機体リストにも JAL・ANA・ADO・NCA といった見慣れたコールサインが並ぶ。ここまで来れば、あとは直感的に使える。

## 手順②：特定の機体を探す

同じ Search タブの上側にある **Search** 欄は、**4つの情報で検索できる**。

- **Hex ID**（ICAO 24bitアドレス。例：`86D1DE`）
- **コールサイン**（例：`ANA13`）
- **登録記号**（例：`JA01AN`）
- **機種コード**（例：`B788`）

機種コードで検索できるのが地味に便利で、たとえば `B788` と入れれば**画面内の787-8だけ**が残る。ヘリなら `EC45` `A139` `B412` といった具合だ。

## 手順③：機体をクリックする——ここが本番

**このサイトの真価は、機体を1機クリックしたときに出る詳細パネルにある。**

Flightradar24の無料版に慣れていると、情報量の差に驚くと思う。実際に1機クリックして出てきた項目を、意味とともに整理する。

先に全体像を出しておく。パネルは**8つのブロック**に分かれていて、それぞれ答えている問いが違う。

<div class="adsbx-panel-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 580" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="ADS-B Exchangeの機体詳細パネルの構成図。8つのブロックが何に答えるかを示す">
  <text x="280" y="26" text-anchor="middle" fill="#14304a" font-size="15" font-weight="bold">機体をクリックすると出る詳細パネルの構成</text>
  <text x="280" y="46" text-anchor="middle" fill="#4b5563" font-size="12">8つのブロックは、それぞれ違う問いに答えている</text>
  <rect x="14" y="70" width="532" height="54" rx="7" fill="#f6f4ee" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="81" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="102" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">SPATIAL</text>
  <text x="150" y="93" fill="#4b5563" font-size="11">位置・高度・昇降率・対地針路</text>
  <text x="150" y="113" fill="#14304a" font-size="12.5" font-weight="bold">「いまどこを、どう飛んでいるか」</text>
  <rect x="14" y="132" width="532" height="54" rx="7" fill="#ffffff" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="143" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="164" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">SPEED</text>
  <text x="150" y="155" fill="#4b5563" font-size="11">GS ／ TAS ／ IAS ／ マッハ</text>
  <text x="150" y="175" fill="#14304a" font-size="12.5" font-weight="bold">「対地・対気・指示、どれで速いのか」</text>
  <rect x="14" y="194" width="532" height="54" rx="7" fill="#f6f4ee" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="205" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="226" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">ALTITUDE</text>
  <text x="150" y="217" fill="#4b5563" font-size="11">気圧高度 ／ 幾何高度 ／ QNH</text>
  <text x="150" y="237" fill="#14304a" font-size="12.5" font-weight="bold">「どの基準で測った高度なのか」</text>
  <rect x="14" y="256" width="532" height="54" rx="7" fill="#ffffff" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="267" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="288" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DIRECTION</text>
  <text x="150" y="279" fill="#4b5563" font-size="11">対地針路 ／ 真方位 ／ 磁方位 ／ バンク角</text>
  <text x="150" y="299" fill="#14304a" font-size="12.5" font-weight="bold">「機首はどこを向いているか」</text>
  <rect x="14" y="318" width="532" height="54" rx="7" fill="#f6f4ee" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="329" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="350" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">WIND</text>
  <text x="150" y="341" fill="#4b5563" font-size="11">風向・風速 ／ TAT・OAT</text>
  <text x="150" y="361" fill="#14304a" font-size="12.5" font-weight="bold">「予報ではない、その高度の実測の風」</text>
  <rect x="14" y="380" width="532" height="54" rx="7" fill="#fdf1ec" stroke="#b65a3b" stroke-width="1.6"/>
  <rect x="24" y="391" width="112" height="32" rx="5" fill="#b65a3b"/>
  <text x="80" y="412" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">FMS SEL</text>
  <text x="150" y="403" fill="#4b5563" font-size="11">Sel. Alt. ／ Sel. Head.</text>
  <text x="150" y="423" fill="#b65a3b" font-size="12.5" font-weight="bold">「次に何をするつもりか」</text>
  <text x="536" y="400" text-anchor="end" fill="#b65a3b" font-size="11" font-weight="bold">★ここが本命</text>
  <rect x="14" y="442" width="532" height="54" rx="7" fill="#f6f4ee" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="453" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="474" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">SIGNAL</text>
  <text x="150" y="465" fill="#4b5563" font-size="11">取得元 ／ RSSI ／ 受信機数 ／ 経過秒</text>
  <text x="150" y="485" fill="#14304a" font-size="12.5" font-weight="bold">「この位置は、どれくらい新しいか」</text>
  <rect x="14" y="504" width="532" height="54" rx="7" fill="#ffffff" stroke="#d9d3c6" stroke-width="1"/>
  <rect x="24" y="515" width="112" height="32" rx="5" fill="#3a7ca5"/>
  <text x="80" y="536" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">ACCURACY</text>
  <text x="150" y="527" fill="#4b5563" font-size="11">NACp ／ SIL ／ NACv</text>
  <text x="150" y="547" fill="#14304a" font-size="12.5" font-weight="bold">「この位置は、どれくらい信用できるか」</text>
</svg>
</div>

以下、上から順に見ていく。

### 位置・速度の基本（SPATIAL）

| 項目 | 意味 |
|---|---|
| Groundspeed | 対地速度 |
| Baro. altitude | 気圧高度（▼は降下中） |
| WGS84 altitude | GPS由来の幾何高度 |
| Vert. Rate | 昇降率（ft/min） |
| Track | 対地針路 |
| Pos. | 緯度経度 |

**気圧高度とGPS高度が並んで出る**のがポイントだ。両者の差は、その空域の気圧配置を反映している。

### 速度の内訳（SPEED）

| 項目 | 意味 |
|---|---|
| Ground | 対地速度（GS） |
| True | 真対気速度（**TAS**） |
| Indicated | 指示対気速度（**IAS**） |
| Mach | マッハ数 |

<strong>IASとTASとマッハが同時に見える。</strong>GSとTASの差から、その機体が受けている風が読める。[航法計算盤](/blog/tanc3-flight-computer-2026/)で自分で出す値が、実機のものとして並んで表示されるわけだ。

### 高度と気圧（ALTITUDE）

| 項目 | 意味 |
|---|---|
| Barometric | 気圧高度 |
| Geom. WGS84 | 幾何高度 |
| **QNH** | **その機体が設定している高度計規正値** |

**QNHが見える**のは驚いた。高度計規正の実際の値が、外から分かってしまう。

そもそも、なぜ同じ機体の高度が2つ（QNHを入れれば3つ）並ぶのか。**基準にしている面が違う**からだ。

<div class="adsbx-alt-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 442" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="高度の基準面の図。1013.25hPa面、海面、WGS84楕円体面という3つの基準があるため、同じ機体の高度が違う数字になることを示す">
  <defs>
    <marker id="a2-navy" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 z" fill="#14304a"/></marker>
    <marker id="a2-gold" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 z" fill="#a07000"/></marker>
    <pattern id="grd" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="#b9b2a2" stroke-width="3"/></pattern>
  </defs>
  <text x="280" y="26" text-anchor="middle" fill="#14304a" font-size="15" font-weight="bold">同じ1機の高度が、3つの数字になる理由</text>
  <text x="280" y="46" text-anchor="middle" fill="#4b5563" font-size="12">基準にする「面」が3つあるから</text>
  <!-- aircraft -->
  <g transform="translate(250,88)">
    <path d="M0,10 L34,10 L46,4 L34,-2 L0,-2 Z" fill="#3a7ca5"/>
    <path d="M14,-2 L22,-16 L28,-16 L24,-2 Z" fill="#3a7ca5"/>
    <path d="M14,10 L20,22 L26,22 L24,10 Z" fill="#3a7ca5"/>
  </g>
  <!-- surfaces -->
  <line x1="40" y1="150" x2="520" y2="150" stroke="#14304a" stroke-width="2" stroke-dasharray="8,5"/>
  <text x="46" y="144" fill="#14304a" font-size="11.5" font-weight="bold">① 1013.25 hPa の面（標準大気）</text>
  <line x1="40" y1="215" x2="520" y2="215" stroke="#2a9d8f" stroke-width="2.5"/>
  <text x="46" y="209" fill="#1f7a70" font-size="11.5" font-weight="bold">② 海面 ＝ QNH の基準面（図では QNH 1020 hPa）</text>
  <line x1="40" y1="272" x2="520" y2="272" stroke="#a07000" stroke-width="2" stroke-dasharray="8,5"/>
  <text x="46" y="266" fill="#a07000" font-size="11.5" font-weight="bold">③ WGS84 楕円体面（GPS が高さを測る基準）</text>
  <line x1="40" y1="312" x2="520" y2="312" stroke="#8a8271" stroke-width="2"/>
  <rect x="40" y="312" width="480" height="14" fill="url(#grd)" opacity="0.8"/>
  <text x="46" y="306" fill="#6b7280" font-size="11">地表</text>
  <!-- measurement arrows -->
  <line x1="298" y1="93" x2="412" y2="93" stroke="#9aa3ad" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="400" y1="95" x2="400" y2="146" stroke="#14304a" stroke-width="1.8" marker-end="url(#a2-navy)"/>
  <text x="408" y="128" fill="#14304a" font-size="11" font-weight="bold">Barometric</text>
  <line x1="330" y1="95" x2="330" y2="268" stroke="#a07000" stroke-width="1.8" marker-end="url(#a2-gold)"/>
  <text x="338" y="240" fill="#a07000" font-size="11" font-weight="bold">Geom. WGS84</text>
  <!-- legend -->
  <rect x="40" y="336" width="480" height="90" rx="8" fill="#f6f4ee" stroke="#d9d3c6" stroke-width="1"/>
  <text x="56" y="358" fill="#14304a" font-size="11.5"><tspan font-weight="bold">Barometric</tspan> ＝ ①からの高さ（気圧で測る）</text>
  <text x="56" y="377" fill="#14304a" font-size="11.5"><tspan font-weight="bold">Geom. WGS84</tspan> ＝ ③からの高さ（GPS で測る）</text>
  <text x="56" y="396" fill="#14304a" font-size="11.5"><tspan font-weight="bold">QNH</tspan> ＝ ②の気圧として機体が高度計にセットしている値</text>
  <text x="504" y="417" text-anchor="end" fill="#6b7280" font-size="10">※QNH が 1013.25 より低いときは、①は②より下にくる</text>
</svg>
</div>

気圧高度とGPS高度の差は、その空域の気圧配置を映している。**両方が並んで出る**というのは、本来なら別々に用意しないと比べられないものが、勝手に比べられる状態で置いてあるということだ。

### 針路の内訳（DIRECTION）

Ground Track（対地針路）、**True Heading（真方位）**、**Magnetic Heading（磁方位）**、**Magnetic Decl.（偏差）**、Track Rate、そして **Roll（バンク角）**。

**機首方位と対地針路が別々に出る**ので、両者の差＝<strong>偏流（ドリフト）</strong>がそのまま読める。バンク角まで出るのは、正直やりすぎではないかと思うほどだ。

### 風と気温（WIND）

| 項目 | 意味 |
|---|---|
| Speed | 風速 |
| Direction (from) | 風向（どこから吹くか） |
| TAT / OAT | 全温度／外気温 |

**実機が測っている上空の風と気温**が見える。予報ではなく実測値だ。飛行計画の風の見積もりが妥当だったかを、あとから突き合わせられる。

### この3つは、1枚の図に収まる

ここまで見てきた **SPEED・DIRECTION・WIND** は、バラバラの数字に見えて、実は<strong>航法三角形そのもの</strong>だ。図にするとこうなる。

<div class="adsbx-triangle-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 470" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="航法三角形の図。TASベクトルと風ベクトルの合成が対地速度ベクトルになり、機首方位と対地針路の差が偏流角になることを示す">
  <defs>
    <marker id="ah-navy" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#14304a"/></marker>
    <marker id="ah-teal" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#2a9d8f"/></marker>
    <marker id="ah-rust" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#b65a3b"/></marker>
  </defs>
  <text x="280" y="26" text-anchor="middle" fill="#14304a" font-size="15" font-weight="bold">SPEED・DIRECTION・WIND は、1つの三角形に収まる</text>
  <text x="280" y="46" text-anchor="middle" fill="#4b5563" font-size="12">ADS-B Exchange は、この三角形の3辺すべてを同時に表示する</text>
  <!-- TAS vector (heading) -->
  <line x1="110" y1="350" x2="320" y2="120" stroke="#14304a" stroke-width="3" marker-end="url(#ah-navy)"/>
  <!-- Wind vector -->
  <line x1="320" y1="120" x2="400" y2="165" stroke="#2a9d8f" stroke-width="3" marker-end="url(#ah-teal)"/>
  <!-- GS vector (track) -->
  <line x1="110" y1="350" x2="400" y2="165" stroke="#b65a3b" stroke-width="3.5" marker-end="url(#ah-rust)"/>
  <!-- drift angle arc -->
  <path d="M 110 350 L 192.6 297.3 A 98 98 0 0 0 176.1 277.6 Z" fill="#6b7280" opacity="0.16"/>
  <path d="M 192.6 297.3 A 98 98 0 0 0 176.1 277.6" fill="none" stroke="#6b7280" stroke-width="1.6"/>
  <line x1="190" y1="295" x2="236" y2="330" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="240" y="330" fill="#6b7280" font-size="11.5" font-weight="bold">偏流角（ドリフト）</text>
  <text x="240" y="346" fill="#6b7280" font-size="10.5">＝ True Heading と Ground Track の差</text>
  <!-- origin -->
  <circle cx="110" cy="350" r="5" fill="#14304a"/>
  <text x="102" y="370" text-anchor="end" fill="#14304a" font-size="11">機体の</text>
  <text x="102" y="384" text-anchor="end" fill="#14304a" font-size="11">現在位置</text>
  <!-- TAS labels -->
  <text x="225" y="182" text-anchor="end" fill="#14304a" font-size="12.5" font-weight="bold">True（TAS）</text>
  <text x="225" y="199" text-anchor="end" fill="#14304a" font-size="10.5">機首が向いている方向の速度</text>
  <text x="300" y="96" text-anchor="end" fill="#14304a" font-size="11" font-weight="bold">True Heading（真方位）</text>
  <!-- wind labels -->
  <text x="410" y="112" fill="#1f7a70" font-size="12.5" font-weight="bold">Wind（風）</text>
  <text x="410" y="128" fill="#1f7a70" font-size="10.5">Speed / Direction (from)</text>
  <!-- GS labels -->
  <text x="300" y="296" fill="#b65a3b" font-size="12.5" font-weight="bold">Ground（GS）</text>
  <text x="300" y="313" fill="#b65a3b" font-size="10.5">実際に地面の上を動く速度</text>
  <text x="412" y="192" fill="#b65a3b" font-size="11" font-weight="bold">Ground Track（対地針路）</text>
  <!-- caption -->
  <rect x="30" y="392" width="500" height="62" rx="8" fill="#f6f4ee" stroke="#d9d3c6" stroke-width="1"/>
  <text x="280" y="414" text-anchor="middle" fill="#14304a" font-size="12">紺の辺と朱の辺の<tspan font-weight="bold">長さの差</tspan>が、風の前後成分。</text>
  <text x="280" y="433" text-anchor="middle" fill="#14304a" font-size="12">紺の辺と朱の辺の<tspan font-weight="bold">向きの差</tspan>が、偏流角。</text>
  <text x="280" y="449" text-anchor="middle" fill="#6b7280" font-size="10.5">航法計算盤で自分で出す値が、実機の数字として並んで表示される</text>
</svg>
</div>

紺の辺が「機首が向いている方向へ、TASで進もうとする分」。緑の辺が「風に流される分」。その合成が朱の辺、つまり**実際の動き**だ。

[航法計算盤](/blog/tanc3-flight-computer-2026/)で紙の上に描いてきた三角形が、**実機の値で全部埋まった状態**で出てくる。答え合わせができる、ということでもある。

### 自動操縦の設定（FMS SEL）

| 項目 | 意味 |
|---|---|
| **Sel. Alt.** | **選択した目標高度** |
| Sel. Head. | 選択した目標方位 |

ここがいちばん驚いた項目だ。**その機体がオートパイロットに何ftをセットしているかが分かる。**

つまり、いま21,200ftを降下中の機体が `Sel. Alt. 6016 ft` を表示していれば、**まだ6,000ft付近まで降りる予定だ**と読める。**次に何をするつもりか**が見える、ということだ。

図にすると、読み方がはっきりする。

<div class="adsbx-selalt-fig" style="max-width:560px;margin:1.6em auto;">
<svg viewBox="0 0 560 370" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="選択高度の読み方の図。現在の気圧高度と昇降率が「いま何をしているか」を示し、Sel. Alt.が「これから何をするか」を示すことを表す">
  <defs>
    <marker id="a3-rust" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 z" fill="#b65a3b"/></marker>
    <marker id="a3-blue" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 z" fill="#3a7ca5"/></marker>
    <marker id="a3-gray" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto"><path d="M0,0 L8,3.5 L0,7 z" fill="#6b7280"/></marker>
  </defs>
  <text x="280" y="26" text-anchor="middle" fill="#14304a" font-size="15" font-weight="bold">Sel. Alt. が読めると、「この先」が分かる</text>
  <text x="280" y="46" text-anchor="middle" fill="#4b5563" font-size="12">現在の高度と昇降率は「いま」。選択高度は「これから」。</text>
  <!-- axes -->
  <line x1="70" y1="70" x2="70" y2="288" stroke="#b9b2a2" stroke-width="1.5"/>
  <line x1="70" y1="288" x2="524" y2="288" stroke="#b9b2a2" stroke-width="1.5"/>
  <text x="62" y="78" text-anchor="end" fill="#6b7280" font-size="10.5">高度</text>
  <text x="520" y="304" text-anchor="end" fill="#6b7280" font-size="10.5">時間 →</text>
  <!-- Sel. Alt. line -->
  <line x1="70" y1="238" x2="524" y2="238" stroke="#3a7ca5" stroke-width="2" stroke-dasharray="7,4"/>
  <text x="78" y="231" fill="#3a7ca5" font-size="12" font-weight="bold">Sel. Alt. 6,016 ft</text>
  <!-- flown path -->
  <path d="M 92 92 Q 145 100 196 132" fill="none" stroke="#b65a3b" stroke-width="3"/>
  <!-- planned path -->
  <path d="M 196 132 Q 320 196 424 238" fill="none" stroke="#b65a3b" stroke-width="2.4" stroke-dasharray="6,5" opacity="0.75"/>
  <line x1="424" y1="238" x2="512" y2="238" stroke="#b65a3b" stroke-width="2.4" stroke-dasharray="6,5" opacity="0.75" marker-end="url(#a3-rust)"/>
  <!-- current point -->
  <circle cx="196" cy="132" r="6.5" fill="#b65a3b" stroke="#ffffff" stroke-width="2"/>
  <text x="212" y="106" fill="#b65a3b" font-size="12.5" font-weight="bold">Baro. altitude 21,200 ft ▼</text>
  <text x="212" y="124" fill="#b65a3b" font-size="11.5">Vert. Rate −1,800 ft/min</text>
  <text x="188" y="152" text-anchor="end" fill="#6b7280" font-size="10.5">いま</text>
  <!-- gap brace -->
  <line x1="330" y1="146" x2="330" y2="232" stroke="#6b7280" stroke-width="1.4" marker-start="url(#a3-gray)" marker-end="url(#a3-gray)"/>
  <text x="340" y="180" fill="#14304a" font-size="11.5" font-weight="bold">あと約 15,000 ft</text>
  <text x="340" y="196" fill="#14304a" font-size="11.5">降りる予定と読める</text>
  <!-- annotation for level off -->
  <text x="430" y="262" fill="#6b7280" font-size="10.5">ここで水平飛行に移る見込み</text>
  <!-- caption -->
  <rect x="40" y="316" width="480" height="44" rx="8" fill="#fdf1ec" stroke="#b65a3b" stroke-width="1.2"/>
  <text x="280" y="337" text-anchor="middle" fill="#8a3f26" font-size="12"><tspan font-weight="bold">Vert. Rate</tspan> が「いま何をしているか」、<tspan font-weight="bold">Sel. Alt.</tspan> が「次に何をするつもりか」。</text>
  <text x="280" y="354" text-anchor="middle" fill="#8a3f26" font-size="11.5">この2つが並ぶことに、このサイトの価値がある。</text>
</svg>
</div>

### 電波の受信状況（SIGNAL）

Source（**ADS-B / MLAT** などの別）、RSSI（受信強度）、Msg. Rate（メッセージ頻度）、Receivers（**何台の受信機が拾っているか**）、Last Pos.／Last Seen（最終受信からの経過秒）。

**その位置情報がどうやって得られたか**が明示されるのは、このサイトの誠実なところだと思う。ADS-Bなのか、[MLATで割り出した推定位置](/blog/flight-tracking-mlat-2026/)なのかで、信頼度は当然違う。

### 精度指標（ACCURACY）

**NACP**（位置精度）、**SIL**（完全性レベル）、**NACV**（速度精度）、NICBARO、RC。

[ADS-Bの基礎記事](/blog/adsb-basics-2026/)で触れた品質パラメータが、実機の値として並ぶ。「ADS-Bの位置がどれくらい信用できるか」を数字で確認できる、という意味で教材価値が高い。

## 手順④：絞り込む（Filters）

サイドバー上部の **Filters** タブに切り替えると、条件を指定して表示を絞れる。

- **Filter by altitude**（高度の範囲。低空だけ見たいときに便利）
- Filter by callsign／squawk／type code／ICAO hex id
- **Filter by source**

最後の **source** が面白い。**ADS-B / UAT / ADS-R / MLAT / TIS-B / Mode-S / Other / ADS-C** から選べる。

たとえば **MLATだけを表示**すれば、「**ADS-Bを積んでいないのに位置が割り出されている機体**」だけが残る。仕組みの理解には、これがいちばん手っ取り早い。

## 手順⑤：キーボードショートカット

このサイトは**アルファベット1文字のボタン**が並んでいて、最初は意味不明に見える。実はすべて**ショートカットキーの頭文字**だ。

| キー | 機能 |
|---|---|
| **H** | ホーム（表示をリセット） |
| **L** | ラベルの表示切替 |
| **O** | ラベルの詳細表示 |
| **K** | 航跡ラベルの切替 |
| **T** | 全機の航跡を表示 |
| **M** | 複数選択 |
| **P** | 航跡を残す（Persistence） |
| **I** | 選択した機体だけ表示（Isolate） |
| **F** | 選択機を追尾（Follow） |
| **R** | ランダムな1機を追尾 |
| **U** | 軍用機のみ表示 |

使用頻度が高いのは **H**（迷子になったら戻る）、**T**（航跡を見る）、**P**（軌跡を残して航路の傾向を見る）あたりだ。

そして **U** が、このサイトの看板機能である。

## 「無検閲」とは何を意味するか

ADS-B Exchangeが知られているのは、**表示する機体を絞り込まない**ためだ。Flightradar24などは、運航者からの申し出などで**特定の機体を意図的に非表示**にする仕組みを持つ。ADS-B Exchangeにはそれがない。

だから、**軍用機・政府専用機・要人輸送機**も、電波が受信できていればそのまま出る。「他のサイトでは見えないのに、ここでは見える」という違いは、ここから生まれる。

一点、事実として書いておくと、**運営体制は変わっている**。ADS-B Exchangeは長くボランティア主体のコミュニティ運営だったが、**2023年1月に航空データ企業のJETNETに買収された**。当時、無検閲の方針が維持されるのかという懸念がコミュニティで持ち上がり、受信機の提供をやめた人もいた。2025年8月にはJETNET側でさらに統合が進んでいる。

現時点では**無料・ログイン不要で無検閲のまま**使えることを実際に確認したが、**運営が民間企業の方針次第である**ことは、頭の片隅に置いておいていいと思う。

## パイロットとして思うこと

正直に書くと、この記事を書く前は「ADS-B Exchangeの売りは無検閲」だと思っていた。**実際に触ってみて、評価が変わった。**

パイロットにとっての価値は、**1機クリックしたときの情報の深さ**のほうだ。**IAS・TAS・マッハ・QNH・上空の風・外気温・磁方位・そしてFMSの選択高度**——これらは通常、**その機のコックピットにいる人しか知り得ない情報**である。それが地上から見える。

もちろん、これは**訓練や研究の道具**として捉えるべきものだ。たとえば、

- 自分が飛んだ空域の**実際の風**を、あとから確認する
- 進入経路で他機が**どの高度・速度で降りているか**を見て、標準的なプロファイルを掴む
- ADS-Bの**精度パラメータ**が実際どの程度の値なのかを知る

若手にとっては、**教科書の数値が実機でどう出るか**を確かめる良い教材になる。TAS/CASの換算を習っても実感が湧かないなら、実機のIASとTASを並べて見るのがいちばん早い。

一方で、**個々の機体の動きを詮索する道具ではない**とも思う。見えることと、見ていいことは別だ。運航者や乗員のプライバシーに関わる使い方には、当然ながら慎重であるべきだろう。

道具としては、間違いなく面白い。<strong>まずは `globe.adsbexchange.com` を開いて、`RJTT` と打ってみてほしい。</strong>そこから先は、触っているうちに分かる。

## まとめ

- 地図は **`globe.adsbexchange.com`**（トップページではない）。**無料・ログイン不要**。有料版の違いは**広告と衛星写真レイヤーだけ**で、位置情報の中身は同じ。
- **空港コードでジャンプ**するのが最速。Search タブの「Jump to Airport」に **`RJTT`**（羽田）などICAO4文字。**緯度経度も可**。地名は日本語で出る。
- 検索は **Hex ID・コールサイン・登録記号・機種コード**の4つに対応。機種コード検索が便利。
- **本命は機体クリック時の詳細パネル**。**IAS／TAS／マッハ、QNH、上空の風と外気温、真方位と磁方位、バンク角**、そして<strong>FMSの選択高度（Sel. Alt.）</strong>まで出る。「次に何をするつもりか」が読める。
- **Filters の source 絞り込み**で、**MLATだけ**を表示できる。仕組みの理解に有効。
- ボタンの1文字は**ショートカットキー**。**H**（リセット）、**T**（全航跡）、**P**（航跡を残す）、**U**（軍用機のみ）あたりが実用的。
- 「無検閲」は**表示する機体を絞らない**という意味。ただし**2023年1月にJETNETが買収**しており、コミュニティ運営時代とは体制が変わっている。
- パイロットにとっての価値は無検閲より**情報の深さ**。ただし**訓練・研究の道具**として使うべきで、個々の機体を詮索する用途には慎重に。

### 関連記事

- [Flightradar24で年35ドルの機能が、ADS-B Exchangeでは無料——2つの航空機追跡サービスを比較する](/blog/adsbx-vs-fr24-2026/)
- [Flightradar24はなぜ機体を映せるのか——ADS-Bとマルチラテレーション（MLAT）の仕組みを解説](/blog/flight-tracking-mlat-2026/)
- [ADS-Bとは何か——「放送型自動位置情報」の仕組み・メリット・課題](/blog/adsb-basics-2026/)
- [新千歳の「デジタル安全バリア」——GPSで誤進入を止める試み。ADS-Bと繋いだら何ができるか](/blog/digital-safety-barrier-adsb-2026/)

---

*本記事は、2026年8月時点で筆者が実際にADS-B Exchange（globe.adsbexchange.com）を操作して確認した内容をもとに整理したものです。ウェブサイトの仕様・画面構成・料金体系は変更される可能性があります。表示される情報の利用にあたっては、各サイトの利用規約および関係者のプライバシーに配慮してください。*

---

**出典**

- ADS-B Exchange（地図画面） [https://globe.adsbexchange.com](https://globe.adsbexchange.com)
- ADS-B Exchange 公式サイト・FAQ／Map Help [https://adsbexchange.com/faq/](https://adsbexchange.com/faq/)
- JETNET "JETNET Acquires ADS-B Exchange"（2023年1月25日） [https://www.jetnet.com/resources/press-releases/jetnet-acquires-ads-b-exchange](https://www.jetnet.com/resources/press-releases/jetnet-acquires-ads-b-exchange)
- tar1090（地図画面のベースとなっているオープンソースソフトウェア） [https://github.com/wiedehopf/tar1090](https://github.com/wiedehopf/tar1090)

**画像出典**：Wikimedia Commons "Discone-solid-copper-700Mhz-2Ghz" by Adamantios（CC BY-SA 3.0）。イメージ画像（広帯域受信用のディスコーンアンテナ）。

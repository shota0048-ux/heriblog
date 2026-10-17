---
title: 'GPV気象予報（weather-gpv.info）の使い方——凍結気象状態と、高度別の風を読むための整理'
description: '無料の「GPV気象予報」は、気象庁のMSM・GSMや米国のGFSなどの数値予報をそのまま地図で見られるサイトです。ただし、詳細（MSM）で見られるのは地上の値だけで、上空の気温や風は「広域」の高層気圧面図とGFSの鉛直断面図で見ることになります。0°C高度と雲・湿りから凍結気象状態の可能性を見る手順と、地上・925・850・500hPaの風を高度に置き換えて読む手順を、ヘリの運航目線で整理しました。'
pubDate: '2026-10-18'
category: '基礎知識'
tags: ['気象', '航空安全']
heroImage: '../../assets/posts/weather-gpv-guide-hero.jpg'
---

<strong>[GPV気象予報](http://weather-gpv.info/)</strong>（weather-gpv.info）は、気象庁や米国海洋大気局（NOAA）などの数値予報の計算結果を、地図の上にそのまま描いてくれる無料のサイトです。

天気予報サイトのような「晴れ・雨」のアイコンはありません。そのかわり、<strong>雨量・雲量・気温・風を1時間ごとの面で</strong>見られます。運航前のブリーフィングで、「どこで・いつ・どのくらい」を掴むのに便利です。

ただ、メニューが独特で、どの図で何が分かるのかが少し分かりにくいサイトでもあります。そこで今回は、ヘリの運航で特に知りたい次の2つに絞って整理しました。

- <strong>凍結気象状態（着氷のおそれ）があるか</strong>
- <strong>地上と上空で、風はどのくらいか</strong>

先に大事な前提を書いておきます。サイト自身が注意しているとおり、<strong>数値予報は天気予報を作るための基礎資料で、天気予報そのものではありません。</strong>モデルの癖による誤差が含まれます。ここで紹介するのは「全体像を掴む」ための使い方で、最終的な判断は、TAFや[下層悪天予想図](/blog/lowlevel-sigwx-2026/)などの公式の航空気象情報と合わせて行ってください。

---

## まず全体像——どのモデルで、何が見られるか

画面左のメニューで「<strong>モデル</strong>」と「<strong>エリア</strong>」を選び、その下の項目をクリックすると、右側に予想図が出ます。予報時刻は、マウスのホイール、キーボードの矢印キー、画面上の矢印ボタンやスライドバーで動かします。

モデルは大きく分けて次のとおりです。

| メニュー | 中身 | 格子 | 予報期間・間隔 | 更新 |
|---|---|---|---|---|
| <strong>詳細（39時間）</strong> | 気象庁 <strong>MSM</strong>（メソモデル） | 5km | 39時間先まで・1時間ごと | 1日8回（初期時刻の2時間30分後） |
| <strong>広域（264時間）</strong> | 気象庁 <strong>GSM</strong>（全球モデル） | 20km | 11日先まで | 1日2回 |
| 高層気圧面（広域） | GSMの上空の図 | — | 3時間ごと | 1日2回 |
| 米国海洋大気局予報 | NOAA <strong>GFS</strong> | 0.5度 | 16日先まで | 1日4回 |
| 欧州中期予報センター | <strong>ECMWF</strong> | 0.5度 | 10日先まで | 1日2回 |

<small>出典：GPV気象予報 トップページ、GFS・ECMWFの各ページ（2026年10月時点）</small>

ここで押さえておきたいのが、<strong>詳細（MSM）で見られるのは「地上」の値だけ</strong>という点です。雨量・雲量、気温・湿度、気圧・風速はいずれも地表面の予想です。高層気圧面のメニューも、詳細モデルで選べるのはSSI（ショワルター安定指数）だけで、それ以外を選ぶと自動的に広域（GSM）に切り替わります。

つまり、このサイトで<strong>上空の気温と風を見るには、GSMの「高層気圧面」と、GFSの図を使う</strong>ことになります。

### 地図上の「ポイント数値データ」も地上の値

トップページから入れる「<strong>ポイント数値データ</strong>」（試験運用）は、地図をクリックした地点のMSMの予想を表で出してくれる機能です。表示されるのは、<strong>雨量（mm/h）・雲量（%）・気温（°C）・風向・風速（m/s）</strong>の1時間ごとの値で、こちらも地上の値です。

サイトの注意書きにあるとおり、値は<strong>約5km四方の平均</strong>です。格子の平均標高と実際の地点の標高が大きく違う山岳部では、予想とのずれが大きくなります。

---

## 高度別の風を読む

### 気圧面と高度の対応

上空の図は「高度」ではなく「<strong>気圧面</strong>」で描かれています。おおよその高度に置き換えると、次のとおりです。

| 気圧面 | 標準大気での高度 | フィート換算 | このサイトで見られる図 |
|---|---|---|---|
| 地上 | — | — | <strong>詳細（MSM）「気圧・風速」</strong>：風速は <strong>m/s</strong>、1時間ごと |
| <strong>925hPa</strong> | 約 <strong>760m</strong> | 約2,500ft | 「925hPa相当温位/風」：矢羽は <strong>kt</strong> |
| <strong>850hPa</strong> | 約 <strong>1,460m</strong> | 約4,800ft | 「850hPa高度/気温/風」「850気温/風/700上昇流」：矢羽は <strong>kt</strong> |
| <strong>700hPa</strong> | 約 <strong>3,010m</strong> | 約9,900ft | 「700hPa湿数/500hPa気温」：<strong>風の図はない</strong> |
| <strong>500hPa</strong> | 約 <strong>5,570m</strong> | 約18,300ft | 「500hPa高度/気温/風」：矢羽は <strong>kt</strong> |
| 300hPa | 約 9,160m | 約30,100ft | 「300hPa高度/気温/風」：矢羽は <strong>kt</strong> |

<small>高度はICAO標準大気による値。実際の高度は気温や気圧配置によって変わります（たとえば850hPaの高度は、おおむね1,300〜1,600mの範囲で動きます）。</small>

ヘリの巡航高度帯で直接使えるのは、<strong>地上（MSM）・925hPa・850hPa</strong>の3枚です。

<figure>
<svg viewBox="0 0 560 420" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="気圧面と高度の対応、およびGPV気象予報で見られる図の模式図。地上はMSMの風（m/s）、925hPa約760mと850hPa約1460mはGSM・GFSの風（kt）、700hPa約3010mは湿数のみで風の図はない、500hPa約5570mは風（kt）。0°C高度の例と、−10〜0°Cの着氷しやすい層を示す">
  <rect x="0" y="0" width="560" height="420" fill="#f7f6f2"/>
  <text x="20" y="28" fill="#14304a" font-size="14" font-weight="bold">気圧面と高度——GPV気象予報で見られる図</text>
  <text x="20" y="46" fill="#4b5563" font-size="11">高度は標準大気。縦軸は概略</text>
  <line x1="80" y1="380" x2="80" y2="90" stroke="#8a8173" stroke-width="1.5"/>
  <text x="72" y="384" text-anchor="end" fill="#4b5563" font-size="10.5">0m</text>
  <text x="72" y="324" text-anchor="end" fill="#4b5563" font-size="10.5">1,000m</text>
  <text x="72" y="264" text-anchor="end" fill="#4b5563" font-size="10.5">2,000m</text>
  <text x="72" y="204" text-anchor="end" fill="#4b5563" font-size="10.5">3,000m</text>
  <text x="72" y="144" text-anchor="end" fill="#4b5563" font-size="10.5">4,000m</text>
  <rect x="80" y="152" width="460" height="114" fill="#dbe8f5" opacity="0.8"/>
  <text x="535" y="168" text-anchor="end" fill="#2f5f8f" font-size="11" font-weight="bold">−10〜0°C：着氷しやすい温度帯（例）</text>
  <line x1="80" y1="266" x2="540" y2="266" stroke="#c8402f" stroke-width="2" stroke-dasharray="7 4"/>
  <text x="535" y="260" text-anchor="end" fill="#c8402f" font-size="11" font-weight="bold">0°C高度（例：約1,900m）</text>
  <line x1="80" y1="380" x2="540" y2="380" stroke="#14304a" stroke-width="2"/>
  <text x="92" y="372" fill="#14304a" font-size="12" font-weight="bold">地上</text>
  <text x="200" y="372" fill="#14304a" font-size="11">詳細（MSM）気圧・風速 … 風速 m/s・1時間ごと</text>
  <line x1="80" y1="334" x2="540" y2="334" stroke="#6b7785" stroke-width="1"/>
  <text x="92" y="328" fill="#14304a" font-size="12" font-weight="bold">925hPa ≈ 760m</text>
  <text x="330" y="328" fill="#14304a" font-size="11">925hPa相当温位/風 … 矢羽 kt</text>
  <line x1="80" y1="292" x2="540" y2="292" stroke="#6b7785" stroke-width="1"/>
  <text x="92" y="286" fill="#14304a" font-size="12" font-weight="bold">850hPa ≈ 1,460m</text>
  <text x="330" y="286" fill="#14304a" font-size="11">850hPa高度/気温/風 … °C・矢羽 kt</text>
  <line x1="80" y1="200" x2="540" y2="200" stroke="#6b7785" stroke-width="1"/>
  <text x="92" y="194" fill="#14304a" font-size="12" font-weight="bold">700hPa ≈ 3,010m</text>
  <text x="330" y="194" fill="#14304a" font-size="11">700hPa湿数 … 風の図はない</text>
  <line x1="80" y1="90" x2="540" y2="90" stroke="#6b7785" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="92" y="84" fill="#14304a" font-size="12" font-weight="bold">500hPa ≈ 5,570m（縮尺外）</text>
  <text x="330" y="84" fill="#14304a" font-size="11">500hPa高度/気温/風 … 矢羽 kt</text>
  <text x="92" y="114" fill="#4b5563" font-size="10.5">925hPaより上の図は、広域（GSM）の高層気圧面とGFS</text>
  <text x="92" y="130" fill="#4b5563" font-size="10.5">GFSの「鉛直断面」なら、地上〜上空の気温を1枚で見られる</text>
</svg>
<figcaption>気圧面とおおよその高度、GPV気象予報で見られる図の対応（筆者作成）。0°C高度と着氷しやすい温度帯は一例です。</figcaption>
</figure>

### 風の読み方

<strong>地上の風（MSM）</strong>——「気圧・風速」を開くと、等圧線（hPa）と、風向・風速のベクトル（<strong>m/s</strong>）が出ます。1時間ごとに動かせるので、<strong>強まる時間帯</strong>を掴むのに向いています。

<strong>上空の風（GSM・GFS）</strong>——高層気圧面の図は、風を<strong>矢羽</strong>で描いています。単位は<strong>ノット（kt）</strong>です。一般的な矢羽の読み方どおり、短い羽が5kt、長い羽が10kt、三角の旗が50ktです。

単位が違うので、地上と上空を比べるときは換算が必要です。

> <strong>1 m/s ≒ 1.94 kt</strong>（10 m/s ≒ 19kt、15 m/s ≒ 29kt）

### 風の確認手順

| 知りたいこと | 開く図 | 見るところ |
|---|---|---|
| 離着陸場の風・強まる時間 | 詳細（MSM）「気圧・風速」 | 1時間ごとのベクトル。等圧線が混んでいる所ほど風が強い |
| 地上の風を地点の数値で | ポイント数値データ | 風向・風速（m/s）の時系列。山岳部は誤差が大きい |
| 巡航高度帯（〜1,500m）の風 | 高層気圧面「925hPa相当温位/風」「850hPa高度/気温/風」。ECMWFのページにも850hPaの風の図がある | 矢羽（kt）。地上の風との差＝高度による風の変化の目安。モデル同士で風が大きく違う日は、予想の確度が低い |
| 上空の強風・ジェット | 「500hPa高度/気温/風」「300hPa高度/気温/風」 | 矢羽（kt）。ヘリの高度帯より上だが、天気の変化の手がかり |

ひとつコツを書いておきます。<strong>地上の風と850hPaの風を並べると、山越えや谷沿いで風がどう変わりそうかの見当がつきます。</strong>850hPaで強い風が吹いているのに地上が弱い日は、尾根を越えるあたりで急に揺れることがあります。ただ、地形の細かい影響はGSM・GFSの格子では表現しきれないので、あくまで見当です。

なお、このサイトには<strong>700hPa（約3,000m）の風の図がありません</strong>。700hPa付近の風が必要なときは、気象庁の[下層悪天予想図](/blog/lowlevel-sigwx-2026/)などで補ってください。

---

## 凍結気象状態の可能性を読む

### 考え方

着氷が起きやすいのは、<strong>過冷却の水滴がある雲の中、気温がおおむね0°Cから−10°Cの範囲</strong>です（詳しくは[着氷の基礎](/blog/icing-basics-2026/)の記事で書きました）。

「凍結気象状態」が具体的に何を指すかは、<strong>機体の飛行規程（RFM）の定義</strong>に従います。多くの場合、「目に見える水分（雲・霧・雨・雪など）があり、外気温が一定の温度以下」という形で書かれていますが、その温度は機種によって違います。

GPV気象予報でできるのは、次の2つを重ねて「<strong>どの高さに、凍結気象状態になりうる層がありそうか</strong>」の見当をつけることです。

1. <strong>0°C高度</strong>——どの高さから下が0°C以上で、上が氷点下か
2. <strong>湿り</strong>——その高さに雲（水分）がありそうか

### 手順1：0°C高度を見積もる

<strong>方法A：GFSの「鉛直断面」で直接読む（いちばん分かりやすい）</strong>

「米国海洋大気局予報」のページの下に、「<strong>鉛直断面 気温・温位・風</strong>」があります。<strong>東経130度・135度・140度</strong>と<strong>北緯30度・35度・40度</strong>に沿って、地上から上空までを切った断面図です。

- <strong>塗りつぶし</strong>が気温（°C）です。凡例の<strong>0°Cの境目の高さ</strong>を探します。
- <strong>緑の線</strong>が高度（m）なので、0°Cの境目が何メートルにあるかを読みます。
- 白い線は断面に直交する向きの風速、矢印は断面方向の風です。

自分の飛ぶ場所に近い線を選びます。たとえば福島や仙台なら東経140度、関西なら東経135度です。断面の線から離れた場所では使えないこと、GFSは格子が0.5度と粗いことには注意が必要です。

<strong>方法B：地上気温と850hPa気温から見積もる</strong>

断面の線から外れている場所では、2枚の図から見積もります。

1. 詳細（MSM）の「気温・湿度」で、<strong>地上の気温</strong>を読む
2. 広域の高層気圧面「<strong>850hPa高度/気温/風</strong>」で、<strong>850hPa（約1,460m）の気温</strong>を読む（塗りつぶしの色）。GFSやECMWFのページにも850hPa気温の図がある
3. この2点を直線でつないで、0°Cになる高さを出す

> 例：地上（標高0m）が <strong>+8°C</strong>、850hPa（約1,460m）が <strong>−2°C</strong> なら、
> 1,460m × 8 ÷（8＋2）≒ <strong>約1,170m</strong> が0°C高度の目安

<small>直線でつなぐ近似です。逆転層がある日や、地上付近の冷え込みが強い朝は外れます。</small>

850hPaの気温がまだ0°Cより高い日は、0°C高度はそれより上にあります。その場合は、「700hPa湿数/500hPa気温」の白線（500hPa、約5,570mの気温）と850hPaの気温の間で同じように見積もれますが、間が4,000m以上開くので精度は落ちます。

### 手順2：その高さに湿り（雲）があるかを見る

| 開く図 | 見るところ | 読み方の目安 |
|---|---|---|
| 詳細（MSM）「雨量・雲量」 | 灰色の等値線が雲量（%）、色が雨量（mm/h） | 雲量が多く、雨や雪が予想されている所 |
| 高層気圧面「700hPa湿数/500hPa気温」 | 塗りつぶしが700hPaの<strong>湿数</strong>（気温−露点温度）。<strong>黒線が湿数3°C</strong> | 湿数が小さい（黒線の内側）ほど湿っていて、雲がある可能性が高い |
| 高層気圧面「850気温/風/700上昇流」 | 塗りつぶしが700hPaの鉛直p速度（hPa/h） | 上昇流がある所は雲ができやすい |

ここでいう<strong>湿数</strong>は、気温と露点温度の差です。差が小さいほど空気が飽和に近く、雲ができやすい状態です。この図では湿数3°Cの線が黒線で描かれています。

### 手順3：重ねて判断する

1. 手順1で、<strong>0°C高度</strong>と、<strong>−10°Cくらいになる高さ</strong>の見当をつける
2. その高度帯に、手順2で<strong>雲・湿り・降水</strong>がありそうかを見る
3. 自分の飛ぶ高度が、<strong>その高度帯にかかるかどうか</strong>を確かめる

<strong>「飛ぶ高度が0°C高度より上」かつ「その高さで雲が予想されている」なら、凍結気象状態になりうる</strong>、というのが基本の見方です。逆に、0°C高度が飛ぶ高度より十分高ければ、その日の構造的な着氷の心配は小さくなります。

冬の日本海側のように、地上付近から氷点下で雪雲が広がっている日は、離着陸の段階から凍結気象状態になりえます。その場合は、MSMの「雨量・雲量」にある<strong>雨雪判別</strong>（黄の実線が雨とみぞれ、紫の実線がみぞれと雪の境界）も参考になります。

---

## 使うときの注意

- <strong>数値予報は「生の計算結果」</strong>です。位置や時刻のずれ、地形による系統的な誤差が含まれます。
- <strong>GSM・GFSの格子は粗い</strong>（20km・0.5度）ため、山の細かい影響は出ません。山岳の風や局地的な雲は、実況とあわせて判断します。
- <strong>0°C高度の見積もりは近似</strong>です。逆転層や地上付近の冷気は、直線の見積もりでは表せません。
- 広域（週間）予報は誤差が大きくなりやすいので、サイトのメニューの「<strong>信頼度</strong>」も確認します。
- 着氷や上空の風については、気象庁の<strong>下層悪天予想図</strong>（FL020・050・100の0°C線や着氷域を含む）、空港のTAFなど、<strong>航空用の公式な情報で最終確認</strong>をします。

GPV気象予報は、それらの公式情報の「前後」を埋めるのに向いています。<strong>下層悪天予想図で全体の状況を確かめ、GPV気象予報の1時間ごとの図で「いつ変わりそうか」を掴む</strong>、という使い分けがしやすいと思います。

## まとめ

- GPV気象予報は、<strong>MSM（詳細・5km・39時間先まで1時間ごと）</strong>、<strong>GSM（広域・20km・11日先まで）</strong>、<strong>GFS</strong>、<strong>ECMWF</strong>の数値予報を地図で見られる無料サイト。
- <strong>詳細（MSM）で見られるのは地上の値だけ</strong>。上空の気温・風は、<strong>広域の「高層気圧面」</strong>と<strong>GFSの図</strong>で見る。
- 高度の目安は、<strong>925hPa≒760m、850hPa≒1,460m、700hPa≒3,010m、500hPa≒5,570m</strong>。
- <strong>地上の風はm/s、上空の矢羽はkt</strong>。1 m/s ≒ 1.94 kt。ヘリの高度帯では、<strong>地上（MSM）・925hPa・850hPa</strong>の風を並べて見る。700hPaの風の図はない。
- 凍結気象状態の可能性は、<strong>0°C高度</strong>と<strong>湿り（雲）</strong>を重ねて見る。0°C高度は、<strong>GFSの鉛直断面</strong>で直接読むか、<strong>地上気温と850hPa気温から見積もる</strong>。湿りは<strong>700hPa湿数（黒線＝湿数3°C）</strong>とMSMの<strong>雲量・雨量</strong>で見る。
- 凍結気象状態の定義は<strong>機種の飛行規程</strong>に従う。数値予報は基礎資料なので、<strong>下層悪天予想図・TAFなどの公式情報と合わせて判断</strong>する。

---

### 関連記事

- [下層悪天予想図とは——SFC〜FL150を網羅する小型機・ヘリ運航者の必須資料](/blog/lowlevel-sigwx-2026/)
- [着氷（アイシング）の基礎——学生のうちに押さえておきたい仕組みと対処](/blog/icing-basics-2026/)
- [MSMとGSM——モデルの出力は、そのままでは予報になっていない](/blog/msm-gsm-guidance-2026/)
- [SCW（SUPERC WEATHER）の使い方——プロが使う天気予報ビジュアライザを徹底解説](/blog/scw-weather-2026/)
- [Windyの「Forecast Model」を使い分けよう——ECMWF・GFS・ICON・HRRRの違いと選び方](/blog/windy-forecast-models-2026/)

### 出典

- [GPV気象予報](http://weather-gpv.info/)——トップページ（モデル・更新時刻・ご利用上の注意）、高層気圧面の各図の凡例、[米国海洋大気局 数値予報 GFS](http://weather-gpv.info/gfsd.html)（鉛直断面）、[欧州中期予報センター ECMWF](http://weather-gpv.info/ecmd.html)、[詳細予報ポイント数値データ](http://s5.weather-gpv.info/p/m-f.s5.html)、[雨雪判別マップの見方](http://weather-gpv.info/sjd.html)、[風速の目安](http://weather-gpv.info/gw.php)
- 標準大気の気圧面高度：ICAO標準大気（ICAO Doc 7488）による

*本記事は2026年10月18日時点のサイトの構成に基づきます。サイトのメニューや図の仕様は変更されることがあります。凍結気象状態の判断と運航の可否は、機体の飛行規程と公式の航空気象情報に基づいて行ってください。*

ヒーロー画像：2018年2月5日、強い寒気の吹き出しで日本海に筋状の雪雲が広がった日の衛星画像。NASA EOSDIS Worldview（Aqua/MODIS）、海岸線：© OpenStreetMap contributors（[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:20180205_Sea_of_Japan_cold_wave_turbulences_by_Aqua.jpg)）。掲載にあたり切り抜きとリサイズを行いました。

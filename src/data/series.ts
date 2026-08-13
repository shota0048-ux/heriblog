// 連載・シリーズの定義。トップページ（index.astro）と特集ハブ（/blog/series/）で共用。
// ids は読み順（古い→新しい）で並べる。存在しないIDは自動で除外されます。
export interface SeriesDef {
	slug: string;
	title: string;
	description: string;
	ids: string[];
}

export const SERIES: SeriesDef[] = [
	{
		slug: 'crm-decision',
		title: 'CRMと「決めること」',
		description:
			'意見を集めれば安全になる、という思い込みを解きほぐすシリーズ。権威勾配は急すぎても平坦すぎても事故を招きます。「意見収集」と「決定」を分けて考える枠組みを、CRMの歴史と実際の事故から整理していきます。',
		ids: [
			'crm-amrm-2026',
			'crm-authority-gradient-2026',
			'crm-assertion-silence-2026',
			'crm-time-decision-2026',
			'crm-briefing-expectation-2026',
			'crm-organization-decision-2026',
		],
	},
	{
		slug: 'laser-aircraft',
		title: '航空機へのレーザー照射',
		description:
			'飛行中の航空機への緑レーザー照射は何の罪になるのか。報道ヘリから自衛隊機まで相次ぐ事案を題材に、航空法134条の3・威力業務妨害・航空危険罪の射程と実際の量刑を読み解くシリーズです。',
		ids: [
			'laser-aircraft-crime-2026',
			'laser-jgsdf-heli-hokkaido-2026',
		],
	},
	{
		slug: 'doctor-heli',
		title: 'ドクターヘリの担い手問題',
		description:
			'整備士同乗の法的根拠から、整備士不足による運休、厚労省の特例措置、そして国の検討会設置まで——ドクターヘリの担い手確保を続報で追う特集です。',
		ids: [
			'doctor-heli-mechanic-onboard-2026',
			'doctor-heli-mechanic-onboard-deepdive-2026',
			'doctor-heli-suspension-mechanic-2026',
			'doctor-heli-review-committee-2026',
			'doctor-heli-two-pilot-hyogo-2026',
			'doctor-heli-budget-2027-2026',
			'doctor-heli-doctors-survey-2026',
		],
	},
	{
		slug: 'beijing-citic-crash',
		title: '北京・CITICタワー小型機衝突',
		description:
			'北京の超高層ビルに小型機が衝突した事故をきっかけに、中国の安全報告制度（SCASS）と情報統制、そして全国の一般航空を止めた異例の規制対応を読み解くシリーズです。',
		ids: [
			'china-aviation-crm-scass-2026',
			'china-general-aviation-grounding-2026',
			'beijing-citic-nearmiss-a330-2026',
			'beijing-citic-cause-personal-2026',
			'beijing-crash-operator-suspend-2026',
		],
	},
	{
		slug: 'mobile-battery',
		title: 'モバイルバッテリー機内持込み新ルール',
		description:
			'令和8年4月24日施行の新ルールを、旅客向けの「7つのルール」と自家用運航者向けの規則解説の両面から整理する特集です。',
		ids: ['mobile-battery-passenger-2026', 'mobile-battery-kisoku-2026'],
	},
	{
		slug: 'aso-heli-salvage',
		title: '阿蘇・火口のヘリ回収',
		description:
			'阿蘇山の火口に墜落したヘリコプターの回収を巡る動きを、計画承認から膠着、警察の回収作業まで続報で追うシリーズです。',
		ids: ['aso-heli-salvage-2026', 'aso-heli-salvage-deadlock-2026', 'aso-heli-police-recovery-2026'],
	},
	{
		slug: 'robinson-safety-notices',
		title: 'ロビンソンの安全情報（SN）',
		description:
			'Robinson社が公開するSafety Notice（安全情報）を、現役パイロットの視点で読み解くシリーズ。公式資料の入手方法もまとめています。',
		ids: [
			'robinson-publications-guide-2026',
			'robinson-sn40-postcrash-fire-2026',
			'robinson-sn32-turbulence-2026',
		],
	},
	{
		slug: 'ifr-minima-approach',
		title: 'IFRの最低気象条件と進入方式',
		description:
			'離陸・着陸の最低気象条件（暫定基準と飛行方式設定基準の違い）、RVRの読み方、視認進入と目視進入の使い分けまで。IFRで「どこまで降りて、いつ見えていればいいか」を実務目線で整理するシリーズです。',
		ids: [
			'rvr-metar-atis-2026',
			'visual-contact-approach-2026',
			'takeoff-minima-provisional-2026',
			'landing-minima-provisional-2026',
		],
	},
	{
		slug: 'runway-safety',
		title: '滑走路の安全とリモート対空援助',
		description:
			'羽田衝突事故以降に進む滑走路安全対策と、運航情報官の集約化（リモート対空援助）の動きを追う特集です。',
		ids: [
			'remote-flight-service-airport-2026',
			'wakkanai-runway-incursion-2026',
			'haneda-runway-joint-heli-rollover-2026',
			'haneda-runway-joint-committee-2026',
		],
	},
	{
		slug: 'heli-hr-issues',
		title: 'ヘリ操縦士・人材の課題',
		description:
			'操縦士・整備士の不足はなぜ解消しないのか。運航形態、訓練の入口と経験の受け皿、国の対策まで、ヘリ業界の人材問題を構造から考える特集です。',
		ids: [
			'fire-disaster-heli-operation-2026',
			'heli-pilot-training-course-pipeline-2026',
			'heli-pilot-experience-accumulation-2026',
			'doctor-heli-suspension-mechanic-2026',
			'heli-pilot-training-cost-support-2026',
			'koudai-heli-instructor-2026',
			'heli-pilot-supply-demand-2026',
		],
	},
];

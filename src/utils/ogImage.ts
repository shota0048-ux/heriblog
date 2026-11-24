import type { ImageMetadata } from 'astro';
import { getImage } from 'astro:assets';

/**
 * SNSのプレビュー（OGP）用に、元画像を 1200×630 の軽いJPEGに変換する。
 * 元画像（約1MB）をそのまま配信すると転送量が増えるため。
 */
export async function getOgImageUrl(image: ImageMetadata, base: URL | string | undefined) {
	const og = await getImage({
		src: image,
		width: 1200,
		height: 630,
		fit: 'cover',
		format: 'jpg',
		quality: 75,
	});
	return new URL(og.src, base).href;
}

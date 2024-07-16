<script lang="ts">
	import Page from '$lib/components/Page.svelte'
	import TimeLine from '$lib/components/TimeLine.svelte'
	import type { TimelinePointType } from '$lib/types/tools'

	import cenynizke from '$lib/assets/img/cenynizke.png'
	import binderadvokat from '$lib/assets/img/binder-advokat.png'
	import sokolprimetice from '$lib/assets/img/sokolprimetice.png'
	import prettifier from '$lib/assets/img/PrettifierJSON.png'
	import maluckevinarstvi from '$lib/assets/img/malucke-vinarstvi.png'

	const points: TimelinePointType[] = [
		{
			date: new Date(2005, 0, 1),
			title: 'Služby Kubík',
			text: '',
			img: cenynizke,
			url: 'https://cenynizke.cz'
		},
		{

			date: new Date(2009, 0, 1),
			title: 'TJ Sokol Přímětice',
			text: '',
			img: sokolprimetice,
			url: 'https://sokolprimetice.cz'
		},
		{
			date: new Date(2016,0,1),
			title: 'Binder Advokát',
			text: '',
			img: binderadvokat,
			url: 'https://binder-advokat.cz'
		},
		{
			date: new Date(2018, 7, 1),
			title: 'Prettifier',
			text: '',
			img: prettifier,
			url: 'https://github.com/fleury08/prettifier'
		},
		{
			date: new Date(2023, 0, 1),
			title: 'Malučké Vinařství',
			text: 'Local winehouse, simple static website, made with SvelteKit and Tailwindcss',
			img: maluckevinarstvi,
			url: 'https://maluckevinarstvi.cz/',
		}
	]
</script>

<Page>
	<svelte:fragment slot="title">Public projects</svelte:fragment>
	<TimeLine {points}></TimeLine>
</Page>
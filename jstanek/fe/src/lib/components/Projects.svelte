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
			text: 'My first payed job. It was horrible, but I learned a lot. Everybody has to start somewhere.',
			img: cenynizke,
			url: 'https://cenynizke.cz'
		},
		{

			date: new Date(2009, 0, 1),
			title: 'TJ Sokol Přímětice',
			text: 'Our local football club page. Made with WordPress. Still active and well.',
			img: sokolprimetice,
			url: 'https://sokolprimetice.cz'
		},
		{
			date: new Date(2016,0,1),
			title: 'Binder Advokát',
			text: 'Static website for a friend. Simple static website made with Bootstrap.',
			img: binderadvokat,
			url: 'https://binder-advokat.cz'
		},
		{
			date: new Date(2018, 7, 1),
			title: 'Prettifier',
			text: 'Simple Vala app for Elementary OS, I needed an app so I created. It was fun experiment to know how to distribute app on a Linux platform, specifically through flatpak.',
			img: prettifier,
			url: 'https://github.com/fleury08/prettifier'
		},
		{
			date: new Date(2023, 0, 1),
			title: 'Malučké Vinařství',
			text: 'Local winehouse, simple static website, made with SvelteKit and Tailwind CSS.',
			img: maluckevinarstvi,
			url: 'https://maluckevinarstvi.cz/',
		}
	]
</script>

<Page>
	{#snippet title()}Public projects{/snippet}
	<TimeLine {points}></TimeLine>
</Page>
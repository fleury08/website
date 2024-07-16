<script lang="ts">
	import { onMount } from 'svelte'
	import { Progress } from '$lib/components/ui/progress'


	let items = []
	onMount(async () => {
		const res = await fetch('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
		const text = await res.text()
		const feedDocument = new DOMParser().parseFromString(text, 'text/xml')
		items = [...feedDocument.querySelectorAll('item')].map(item => {
			const title = item?.querySelector('title')?.textContent
			const url = item?.querySelector('link')?.textContent

			return { title, url }
		})
	})


	const speedModifier = 1
	let currentIndex = 0
	let progress = 0

	const tick = () => {
		currentIndex = (currentIndex + 1) % items.length
		progress = (currentIndex / (items.length)) * 100
	}



	const interval = setInterval(tick, 1000 * speedModifier)


</script>

<div class="flex flex-col w-full items-center">
	<a href={items[currentIndex]?.url} target="_blank" rel="noreferrer">{items[currentIndex]?.title}</a>
	<Progress bind:value={progress} />
</div>
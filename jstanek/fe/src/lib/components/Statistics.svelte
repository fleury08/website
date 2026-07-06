<script>

import Page from '$lib/components/Page.svelte'
</script>
<Page>
	{#snippet title()}Personal stats{/snippet}
		<div class="grid grid-cols-1 lg:grid-cols-3">
			<a href="https://codeium.com/profile/jstanek" class="lg:col-span-3" target="_blank">
				<img class="m-auto rounded-2xl" src="https://codeium.com/profile/jstanek/card.png" alt="Statistics of Jaroslav Staněk">
			</a>
		</div>
</Page>

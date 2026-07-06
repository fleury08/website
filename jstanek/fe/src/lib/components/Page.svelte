<script lang="ts">
	import type { Snippet } from 'svelte';
	let { title, children }: { title?: Snippet, children: Snippet } = $props();
</script>

<div class="pt-4 pb-10 scroll-smooth flex flex-col justify-center items-center min-h-dvh">
	<div class="text-6xl text-center pb-10">
		{#if title}
			{@render title()}
		{/if}
	</div>
	<div class="w-full h-full container">
		{@render children()}
	</div>
</div>

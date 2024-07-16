<script lang="ts">
import ThemeSwitcher from '$lib/components/ThemeSwitcher.svelte';
import { onMount } from 'svelte'

let time = new Date();

	onMount(() => {
		const interval = setInterval(() => {
			time = new Date();
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

<nav class="w-full p-3 sticky top-0  z-10 " id="navbar">

		<div class="flex items-center justify-between container rounded-2xl bg-accent">
			<div class="website-logo"></div>

			<ThemeSwitcher />
		</div>

</nav>
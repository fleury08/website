<script lang="ts">
import ThemeSwitcher from '$lib/components/ThemeSwitcher.svelte';
</script>

<nav class="w-full p-3" id="navbar">
	<div class="container">
		<div class="flex align-items-center justify-between">
			<div class="website-logo"></div>
			<ThemeSwitcher />
		</div>
	</div>
</nav>
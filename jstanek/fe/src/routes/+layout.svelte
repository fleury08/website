
<script lang="ts">
	import '../app.pcss';
	import '$lib/assets/css/theme.pcss';
	import { ModeWatcher } from 'mode-watcher';
	import type { LayoutData } from './$types';
	import { onMount } from 'svelte';
	import { frontend_path } from '$lib/stores/settings';

	export let data: LayoutData;
	onMount(()=>{
		frontend_path.set(data.frontend_api_path)
	})
</script>

<ModeWatcher />
<slot></slot>



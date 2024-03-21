
<script lang="ts">
	import '../app.pcss';
	import '$lib/assets/css/theme.pcss';
	import { ModeWatcher } from 'mode-watcher';
	import type { LayoutData } from './$types';
	import { onMount } from 'svelte';
	import { frontend_path } from '$lib/stores/settings';
	import { createWsConnection } from '$lib/backend-consumer';


	export let data: LayoutData;
	onMount(()=>{
		frontend_path.set(new URL(data.frontend_api_path))
		const ws = createWsConnection(new URL(`${data.backend_ws_url}`))
		ws.send("test")
	})
</script>

<ModeWatcher />
<slot></slot>



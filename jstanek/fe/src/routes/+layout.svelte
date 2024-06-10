
<script lang="ts">
	import '../app.pcss';
	import '$lib/assets/css/theme.pcss';
	import { ModeWatcher } from 'mode-watcher';
	import type { LayoutData } from './$types';
	import { onMount } from 'svelte';
	import { frontend_api_path, frontend_ws_path } from '$lib/stores/settings';
	import { createWsConnection } from '$lib/websocket-tools';


	export let data: LayoutData;
	onMount(()=>{
		frontend_api_path.set(data.frontend_api_path)
		//frontend_ws_path.set(data.frontend_ws_path)
		//const ws = createWsConnection($frontend_ws_path)
		//console.log(ws);
	})
</script>

<ModeWatcher />
<slot></slot>



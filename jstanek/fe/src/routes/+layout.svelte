<script lang="ts">
    import '../app.css';
    import '$lib/assets/css/theme.pcss';
    import {ModeWatcher} from 'mode-watcher';
    import {onMount} from 'svelte';
    import {frontend_api_path} from '$lib/stores/settings';


    let { data, children } = $props();

    onMount(() => {
        frontend_api_path.set(data.frontend_api_path)
    })
</script>

<ModeWatcher/>
{@render children()}



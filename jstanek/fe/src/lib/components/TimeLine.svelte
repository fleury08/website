<script lang="ts">
import TimelinePoint from '$lib/components/TimelinePoint.svelte'
import type { TimelinePointType } from '$lib/types/tools'

let { points = [] } = $props();
const sortedPoints = $derived(points.toSorted((a, b) => a.date > b.date ? 1 : -1));
</script>

{#each sortedPoints as point, i (point.date)}
	<TimelinePoint {point} last={sortedPoints.length - 1 === i} first={i === 0}/>
{/each}


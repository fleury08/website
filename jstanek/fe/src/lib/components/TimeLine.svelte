<script lang="ts">
import TimelinePoint from '$lib/components/TimelinePoint.svelte'
import type { TimelinePointType } from '$lib/types/tools'

export let points: TimelinePointType[] = [];

$: points = points.sort((a, b) => a.date > b.date ? 1 : -1)
</script>

{#each points as point}
	<TimelinePoint {point} last={points.length - 1 === points.indexOf(point)} first={points.indexOf(point) === 0}/>
{/each}

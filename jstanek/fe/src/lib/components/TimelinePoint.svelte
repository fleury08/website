<script lang="ts">
	import type { TimelinePointType } from '$lib/types/tools'

	export let first = false
	export let last = false
	export let point: TimelinePointType | undefined
</script>
{#if point}
	<div class="flex gap-3">
		<div class="flex flex-col gap-1 items-center">
			<div class="w-0 min-h-20 h-full border" class:border-dashed={first}></div>
			<div class="w-auto h-auto border rounded-l-full rounded-r-full p-2">{point.date.getFullYear() ?? ''}</div>
			<div class=" w-0 min-h-20 h-full border" class:border-dashed={last}></div>
		</div>
		<div class="w-full rounded-2xl border m-auto overflow-hidden flex my-10">
			{#if point.img}
				<a href={point.url} target="_blank">
					<img src={point.img} alt={point.title}
							 class="object-cover object-center max-h-64 max-w-72 saturate-50 hover:saturate-100 transition-all">
				</a>
			{/if}
			<div class="flex flex-col p-4">
				<div class="text-2xl">{point.title ?? ''}</div>
				<a class="text-sm mb-3" href={point.url}>{point.url ?? ''}</a>
				<p>{point.text ?? ''}</p>
			</div>
		</div>
	</div>
{/if}
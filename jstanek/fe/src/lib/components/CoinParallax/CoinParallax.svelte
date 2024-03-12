<script>
	import { handleHover, resetStyles, spinCard } from './coin-parallax';

	export let image = '';
	export let rounded = true;
	export let borderless = true;

</script>

<div class="card-parallax" class:rounded-full={rounded}
		 role="img"

		 on:mousemove={handleHover}
		 on:mouseleave={resetStyles}
		 on:dblclick={spinCard}
>
	<div class="card-parallax-content">
		<img alt="Jaroslav Staněk"
				 class="aspect-square"
				 class:rounded-full={rounded}
				 class:border-0={borderless}
				 class:border={!borderless}
				 src="{image}">
	</div>
</div>
<style lang="postcss">
    .card-parallax img {
        @apply aspect-square;
    }

    .card-parallax {
        @apply bg-contain
					m-auto
					h-auto
					relative
					will-change-transform
					z-0
					overflow-hidden
					transition-transform
					duration-100
					ease-in;

        --opacity-before-content: 0;
        --left-before-content: -80%;
        --top-before-content: -80%;
        transform-style: preserve-3d;
    }

    .card-parallax:hover .card-parallax-content {
        @apply z-0;
        transform: translateZ(1em);
    }

    .card-parallax-content {
        @apply z-[1]
					w-max
					h-max
					m-auto
					relative
						overflow-hidden
					transition-transform
					duration-300
					ease-in-out;
    }

    .card-parallax-content::before {
				@apply content-['']
					absolute
					w-[200%]
					h-[200%]
					rotate-45
        	z-[2]
        	transition-opacity
					duration-200
					ease-linear
					opacity-[var(--opacity-before-content)]
					left-[var(--left-before-content)]
					top-[var(--top-before-content)];
				  background: radial-gradient(circle, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 80%, rgba(255, 255, 255, 0) 100%);
    }

    @media (prefers-reduced-motion) {
        .card-parallax {
						@apply transform-none;
        }

    }
</style>
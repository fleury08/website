<script>
	import { handleHover, resetStyles, spinCoin } from './coin-parallax';

	export let image = '';
	export let rounded = true;
	export let borderless = true;

</script>
<div class="m-auto w-fit h-fit"
		 on:click={spinCoin} role="none">
	<div class="card-parallax"
			 role="img"
			 on:mousemove={handleHover}
			 on:mouseleave={resetStyles}
	>
		<div class="card-parallax-content" class:rounded-full={rounded}>
			<img alt="Jaroslav Staněk"
					 class:rounded-full={rounded}
					 class:border-0={borderless}
					 class:border={!borderless}
					 src="{image}">
		</div>
	</div>
</div>
<style lang="postcss">
    .card-parallax img {
        @apply aspect-square;
    }

    .card-parallax {
        @apply bg-cover
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
        w-fit
        m-auto
        relative
        overflow-hidden
        transition-transform
        duration-300
        ease-in-out;
    }

		.coin-rotate {
				transition-duration: 1s;
				--opacity-before-content: 1	;
				transform: rotate3D(0, 1, 0, 360deg);
		}

    .card-parallax-content::before {
        @apply content-['']
        absolute
        w-[150%]
        h-[150%]
        rotate-45
        z-[2]
        transition-opacity
        duration-200
        ease-linear
        opacity-[var(--opacity-before-content)]
        left-[var(--left-before-content)]
        top-[var(--top-before-content)]
				bg-gradient-to-l from-white to-transparent;
        //background: radial-gradient(circle, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 99%, rgba(255, 255, 255, 0) 100%);
    }

    @media (prefers-reduced-motion) {
        .card-parallax {
            @apply transform-none;
        }

    }
</style>
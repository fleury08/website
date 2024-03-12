<script>
	import { handleHover, resetStyles, spinCard } from './card-parallax.ts';

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
	<div class="card-parallax-content" >
		<img alt="Jaroslav Staněk"
				 class:rounded-full={rounded}
				 class:border-0={borderless}
				 class:border={!borderless}
				 src="{image}">
	</div>
</div>
<style lang="postcss">
    .card-parallax {
        --opacity-before-content: 0;
        --left-before-content: -80%;
        --top-before-content: -80%;
        background-size: contain;
        margin: auto;
        height: auto;
        position: relative;
        transition: transform 0.1s ease;
        transform-style: preserve-3d;
        will-change: transform;
        z-index: 0;
        overflow: hidden;
    }

    .card-parallax:hover .card-parallax-content {
        transform: translateZ(1em);
        z-index: 0;
    }

    .card-parallax-content {
        position: relative;
        z-index: 1;

        transition: transform 0.3s ease;
    }

    .card-parallax-content::before {
        content: "";
        position: absolute;
        left: var(--left-before-content);
        top: var(--top-before-content);
        width: 150%;
        height: 150%;
        transform: rotate(-45deg);
        background: radial-gradient(circle, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 80%, rgba(255, 255, 255, 0) 100%);
        opacity: var(--opacity-before-content);
        z-index: 2;
        transition: opacity 0.2s linear;
    }

    @media (prefers-reduced-motion) {
        .card-parallax {
            transform: none !important;
        }
    }
</style>
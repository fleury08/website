<script>
	import Contact from "./Contact.svelte";
	import portrait from "$lib/assets/img/DSC_7787upBW_closeup.jpg";
	import CoinParallax from "$lib/components/CoinParallax/CoinParallax.svelte";
</script>
<div class="page">
  <div class="container">
    <div class="flex flex-col sm:flex-row gap-12 sm:gap-24 items-center">
      <div class="flex flex-col gap-3 w-8/12 sm:w-4/12 ">
          <CoinParallax image={portrait} borderless={false} />
        <Contact />
      </div>
      <div class="align-self-center w-8/12">
        <div class="p-3">
          <div class="text-4xl md:text-8xl pb-6">Hello there!</div>
          <div class="text-2xl md:text-3xl">It's me, <b>Jaroslav Staněk</b></div>
          <p>Let me quickly introduce myself. I was born in 1989 and started exploring PCs at the age of 4. My first encounters were with the Commodore 64 and a 286 PC. After elementary school, I attended high school for four years and then university for three years, both specializing in networking. I am currently developing for a private company but am also working on my own projects.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
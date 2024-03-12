<script>
	import Contact from "./Contact.svelte";
	import portrait from "$lib/assets/img/DSC_7787upBW_closeup.jpg";
	import CoinParallax from "$lib/components/CoinParallax/CoinParallax.svelte";
</script>
<div id="me-page"
     class="page">
  <div class="container">
    <div class="flex sm:flex-col">
      <div>
        <CoinParallax image={portrait}></CoinParallax>
        <Contact></Contact>
      </div>
      <div class="align-self-center">
        <div class="p-3">
          <div class="text-6xl">Hello there!</div>
          <div class="text-3xl">It's me, <b>Jaroslav Staněk</b></div>
          <p>Let me quickly introduce myself. I was born in 1989 and started exploring PCs at the age of 4. My first encounters were with the Commodore 64 and a 286 PC. After elementary school, I attended high school for four years and then university for three years, both specializing in networking. I am currently developing for a private company but am also working on my own projects.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
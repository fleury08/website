<script lang="ts">
	import Navigation from '$lib/components/Navigation.svelte'
	import Footer from '$lib/components/Footer.svelte'
	import Donations from '$lib/components/Donations.svelte'
	import Statistics from '$lib/components/Statistics.svelte'
	import Tools from '$lib/components/Tools.svelte'
	import AboutMe from '$lib/components/AboutMe.svelte'
	import Projects from '$lib/components/Projects.svelte'
</script>


<div class="flex flex-col">

	<Navigation/>

	<AboutMe />

	<div class="separator"></div>

	<Projects />

	<Tools />

	<Statistics />

	<Donations />

	<Footer></Footer>

</div>

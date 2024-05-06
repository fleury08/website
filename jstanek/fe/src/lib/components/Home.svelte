<script>
    import AboutMe from "./AboutMe.svelte";
    import Tools from "./Tools.svelte";
    import Donations from "./Donations.svelte";
    import Statistics from '$lib/components/Statistics.svelte';
</script>
<div class="flex flex-col">

    <AboutMe></AboutMe>

    <div class="separator"></div>

    <Tools />

    <Statistics />

    <Donations />

</div>

<script>
    import AboutMe from "./AboutMe.svelte";
    import Tools from "./Tools.svelte";
    import Donations from "./Donations.svelte";
    import {aboutPage, encodeBase64} from "$lib/public/api";
    import {onMount} from "svelte";
    import {json} from "@sveltejs/kit";

    let test_result

    onMount(async ()=>{
        await aboutPage().then(response => {
            console.log(' response', response)
            response.json().then(json => {
                console.log('json', json)
                test_result = json
            }).catch(error => console.log(error))
        })
    })
</script>
<div>

    <AboutMe></AboutMe>

    <div class="separator"></div>

    <Tools></Tools>

    <Donations></Donations>

</div>

<script>
    import Contact from "./Contact.svelte";
	import portrait from "$lib/assets/img/DSC_7787upBW_closeup.jpg"
	import CardParallax from "./CardParallax/CardParallax.svelte";

</script>
<div id="me-page"
		 class="page">
		<div class="container h-100">
			<div class="row">
				<div class="col-sm-12 col-md-4">
					<div class="row">
						<div class="col-12">
							<CardParallax image={portrait}></CardParallax>
						</div>
					</div>
                    <Contact></Contact>
				</div>
				<div class="col-sm-12 col-md-8 align-self-center">
					<div class="me-page-header p-3">
						<div class="display-1">Hello there!</div>
						<div class="display-3">It's me, <b>Jaroslav Staněk</b></div>
						<p>Let me quickly introduce myself. Born in 1989, started discovering PCs by age 4.
							My first encounter was Commodore 64 and 286 PC. After elementary I went for 4 Years to High School then 3 years of University (both
							specialized on networking).
							Currently developing for private company but trying to do my own stuff.
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
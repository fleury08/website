<script>
	import bitcoin from '$lib/assets/img/bitcoin.png'
	import banano from '$lib/assets/img/share_ban_3h6guuuhqimjzm4d7w6tywzwtmhyq13rg5rqjmt5piysomhdoek6jcsfmgki.png'
	import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '$lib/components/ui/card/index'
	import Page from '$lib/components/Page.svelte'
</script>
<Page>
	<svelte:fragment slot="title">Donations</svelte:fragment>
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
			<Card class="border-0 shadow-none">
				<CardHeader>
					<CardTitle>Bitcoin Lightning Address</CardTitle>
				</CardHeader>
				<CardContent>
					<a href="lightning:acridswamp32@walletofsatoshi.com"><img src="{bitcoin}"
																																		alt="Bitcoin Donation QR Code"></a>
				</CardContent>
				<CardFooter>
					<p class="font-mono break-all text-muted-foreground">acridswamp32@walletofsatoshi.com</p>
				</CardFooter>
			</Card>
			<Card class="border-0 md:col-span-2 shadow-none">
				<CardHeader>
					<CardTitle>Banano Address</CardTitle>
				</CardHeader>
				<CardContent>
					<a href="banano:3h6guuuhqimjzm4d7w6tywzwtmhyq13rg5rqjmt5piysomhdoek6jcsfmgki"> <img src="{banano}"
																																															alt="Banano Donation QR Code"></a>
				</CardContent>
				<CardFooter>
					<p class="font-mono break-all text-muted-foreground">
						3h6guuuhqimjzm4d7w6tywzwtmhyq13rg5rqjmt5piysomhdoek6jcsfmgki</p>
				</CardFooter>
			</Card>
		</div>
</Page>

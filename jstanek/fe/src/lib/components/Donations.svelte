<script>
	import paypal from '$lib/assets/img/paypal.png';
	import bitcoin from '$lib/assets/img/bitcoin.png';
	import banano from '$lib/assets/img/share_ban_3h6guuuhqimjzm4d7w6tywzwtmhyq13rg5rqjmt5piysomhdoek6jcsfmgki.png';
	import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '$lib/components/ui/card/index';
</script>
<div class="page">
	<div class="text-6xl text-center">Donations</div>
	<div class="container">
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
			<Card class="border-0">
				<CardHeader>
					<CardTitle>
						PayPal
					</CardTitle>
				</CardHeader>
				<CardContent>
					<a href="https://paypal.me/jaroush"><img src="{paypal}" alt="PayPal Donation QR Code"></a>
				</CardContent>
				<CardFooter>
					<a class="font-mono break-all text-muted-foreground" href="https://paypal.me/jaroush">https://paypal.me/jaroush</a>
				</CardFooter>
			</Card>
			<Card class="border-0">
				<CardHeader>
					<CardTitle>Bitcoin Address</CardTitle>
				</CardHeader>
				<CardContent>
					<a href="bitcoin:bc1q7pt5gwkn7umnk72u763uvwuyd99kmwh0g24eekl6828x3wyezscskq65wd"><img src="{bitcoin}"
																																																alt="Bitcoin Donation QR Code"></a>
				</CardContent>
				<CardFooter>
					<p class="font-mono break-all text-muted-foreground">bc1q7pt5gwkn7umnk72u763uvwuyd99kmwh0g24eekl6828x3wyezscskq65wd</p>
				</CardFooter>
			</Card>
			<Card class="border-0 md:col-span-2">
				<CardHeader>
					<CardTitle>Banano Address</CardTitle>
				</CardHeader>
				<CardContent>
					<a href="banano:3h6guuuhqimjzm4d7w6tywzwtmhyq13rg5rqjmt5piysomhdoek6jcsfmgki"> <img src="{banano}"
																																															alt="Banano Donation QR Code"></a>
				</CardContent>
				<CardFooter>
					<p class="font-mono break-all text-muted-foreground">3h6guuuhqimjzm4d7w6tywzwtmhyq13rg5rqjmt5piysomhdoek6jcsfmgki</p>
				</CardFooter>
			</Card>
		</div>
	</div>
</div>

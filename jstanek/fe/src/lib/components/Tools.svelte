<script lang="ts">
	import {
		base64Decode,
		base64Encode,
		defaultBase64Object,
		defaultHashObject, defaultMongoDbIdObject,
		defaultPasswordOptions,
		generatePassword,
		hashText, mongoIdConvert
	} from '$lib/tools';
	import type { Base64Object, HashObject, MongoDbObject, PasswordOptions } from '$lib/types/tools';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '$lib/components/ui/card';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '$lib/components/ui/button';
	import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue, SelectInput } from '$lib/components/ui/select';

	type SelectedHash = { name: string, value: string, default: boolean }
	const hashes: [SelectedHash] = [
		{ name: 'SHA-512', value: 'sha512', default: true },
		{ name: 'SHA-256', value: 'sha256' },
		{ name: 'SHA-1', value: 'sha1' },
		{ name: 'MD5', value: 'md5' }
	];
  const passSecurities = ['Basic', 'Medium', 'Strong', 'Secure']



	let passwordObject: PasswordOptions = defaultPasswordOptions();
	let hashObject: HashObject = defaultHashObject();
	let base64EncObject: Base64Object = defaultBase64Object();
	let base64DecObject: Base64Object = defaultBase64Object();
	let mongoDBObject: MongoDbObject = defaultMongoDbIdObject();
	let selectedHash: SelectedHash = hashes.find(x => x.default);
	let selectedSecurity = "Strong";
	let generated = {
		password: '',
		hash: '',
		base64decoded: '',
		base64encoded: '',
		mongoTimestamp: ''
	};


	async function generatePasswordHandler() {
		generated.password = await generatePassword(passwordObject);
	}

	async function hashTextHandler() {
		generated.hash = await hashText(hashObject);
	}

	async function base64EncodeHandler(){
		generated.base64encoded = await base64Encode(base64EncObject);
	}

	async function base64DecodeHandler(){
		generated.base64decoded = await base64Decode(base64DecObject);
	}

	async function mongoIdConvertHandler() {
		generated.mongoTimestamp = await mongoIdConvert(mongoDBObject);
	}

	function passTemplateHandler(event: Event) {
		selectedSecurity = (event.target as HTMLButtonElement).getAttribute("data-value") ?? 'Strong';
		passwordObject = defaultPasswordOptions()
		switch (selectedSecurity) {
			case 'Basic':
				passwordObject.length = 8
				passwordObject.special = false
				passwordObject.numbers = false
				break;
			case 'Medium':
				passwordObject.length = 12
				passwordObject.special = false
				break;
			case 'Strong':
				break;
			case 'Secure':
				passwordObject.length = 24
		}

		return passwordObject
	}

	$:{
		hashObject.alg = selectedHash.value
	}
</script>


<div class="page">
	<div class="text-6xl text-center pb-10">Useful tools</div>
	<div class="container">
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3  gap-4">
			<Card>
				<CardHeader>
					<CardTitle>Password Generator</CardTitle>
				</CardHeader>
				<CardContent>
					<div class="w-full mb-3 gap-3 flex-col flex">
						<div class="flex  gap-1">
							{#each passSecurities as passSecurity}
								<Button class="w-full" variant="{selectedSecurity === passSecurity ? 'default' : 'outline'}" on:click={passTemplateHandler} data-value={passSecurity}>{passSecurity}</Button>
							{/each}
						</div>
						<div>
							<Label for="passwordLength">Password length</Label>
							<Input type="number"
										 max="4096"
										 id="passwordLength"
										 bind:value={passwordObject.length} />
						</div>
						<div>
							<Checkbox bind:checked={passwordObject.uppercase}
												id="passwordSubsetUppercase" />
							<Label for="passwordSubsetUppercase">Uppercase letters [A-Z]</Label>
						</div>

						<div>
							<Checkbox bind:checked={passwordObject.lowercase}
												id="passwordSubsetLowercase" />
							<Label for="passwordSubsetLowercase">Lowercase letters [a-z]</Label>
						</div>
						<div>
							<Checkbox id="passwordSubsetNumbers"
												bind:checked={passwordObject.numeric} />
							<Label for="passwordSubsetNumbers">Numbers [0-9]</Label>
						</div>
						<div>
							<Checkbox bind:checked={passwordObject.special}
												id="passwordSubsetSymbols" />
							<Label for="passwordSubsetSymbols">Special characters [$#/...]</Label>
						</div>
						<div><Label for="passwordOutput">Password</Label>
							<Textarea rows="4"
												id="passwordOutput" value={generated.password} /></div>
					</div>
				</CardContent>
				<CardFooter>
					<Button class="w-full" id="passwordRegenerate"
									on:click={generatePasswordHandler}
					>Generate
					</Button>
				</CardFooter>
			</Card>


			<Card>
				<CardHeader>
					<CardTitle>
						Hashing tool
					</CardTitle>
				</CardHeader>
				<CardContent>
					<div class="w-full mb-3 gap-3 flex-col flex">
						<div>
							<Label for="hashInput">Input to hash</Label>
							<Input
								id="hashInput"
								bind:value={hashObject.text} />
						</div>
						<div>
							<Label for="hashAlgSelect">Hashing algorithm</Label>
							<Select id="hashAlgSelect" bind:selected={selectedHash}>
								<SelectTrigger>
									<SelectValue placeholder="Select an algorithm, default is {hashes.find(x=>x.default).name}"/>
								</SelectTrigger>
								<SelectContent>
									{#each hashes as hash}
										<SelectItem value={hash.value} label={hash.name} >{hash.name}</SelectItem>
									{/each}
								</SelectContent>

							</Select>
						</div>
						<div>
								<Textarea rows="5" id="hashOutput" value={generated.hash} />
						</div>
					</div>
				</CardContent>
				<CardFooter>
					<Button class="w-full" on:click={hashTextHandler}
					>Generate
					</Button>
				</CardFooter>
			</Card>

			<Card>
				<CardHeader>
					<CardTitle>
						Base64
					</CardTitle>
				</CardHeader>
				<CardContent>
					<div class="w-full mb-3 gap-3 flex-col flex">
						<div>
							<Label for="base64EncodeInput">Encode</Label>
							<Input id="base64EncodeInput" type="text" on:keyup={base64EncodeHandler} bind:value={base64EncObject.text}/>
						</div>
						<div>
							<Textarea id="base64EncodeOutput" value={generated.base64encoded} />
						</div>

						<div>
							<Label for="base64DecodeInput"
										 class="form-label">Decode</Label>
							<Input id="base64DecodeInput" type="text" on:keyup={base64DecodeHandler} bind:value={base64DecObject.text} />
						</div>
						<div>
							<Textarea id="base64DecodeOutput" value={generated.base64decoded} />
						</div>
					</div>
				</CardContent>
			</Card>

			<Card>
				<CardHeader>
					<CardTitle>
						MongoDB _id tool
					</CardTitle>
				</CardHeader>
				<CardContent>
					<div class="w-full mb-3 gap-3 flex-col flex">
						<div>
							<Label for="mongoDbIdInput">_id</Label>
							<Input id="mongoDbIdInput" type="text" on:keyup={mongoIdConvertHandler} bind:value={mongoDBObject.object_id}/>
						</div>
						<div>
							<Label for="mongoDbIdOutput">Timestamp</Label>
							<Input type="text" id="mongoDbIdOutput" value={generated.mongoTimestamp}/>
						</div>
					</div>
				</CardContent>
				<CardFooter>
				</CardFooter>
			</Card>

			<Card>
				<CardHeader />
				<CardContent>
					...more to come.
				</CardContent>
			</Card>
		</div>
	</div>
</div>




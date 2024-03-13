<script lang="ts">
	import { defaultHashObject, defaultPasswordOptions, generatePassword, hashText } from '$lib/tools';
	import type { HashObject, PasswordOptions } from '$lib/types/tools';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '$lib/components/ui/card';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '$lib/components/ui/button';
	import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '$lib/components/ui/select';


	let passwordObject: PasswordOptions = defaultPasswordOptions();
	let hashObject: HashObject = defaultHashObject();
	let generated = {
		'password': '',
		'hash': ''
	};

	const hashes: [{ name: string, value: string, default: boolean }] = [
		{ name: 'SHA-512', value: 'sha512', default: true },
		{ name: 'SHA-256', value: 'sha256' },
		{ name: 'SHA-1', value: 'sha1' },
		{ name: 'MD5', value: 'md5' }
	];

	async function generatePasswordHandler() {
		generated.password = await generatePassword(passwordObject);
	}

	async function hashTextHandler() {
		generated.hash = await hashText(hashObject);
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
												id="passwordOutput">{generated.password}</Textarea></div>
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
							<Select id="hashAlgSelect"
											class="form-control"
											selected={hashes.find(hash => hash.default).value}
											bind:value={hashObject.alg}>
								<SelectTrigger>
									<SelectValue placeholder="Select an option" />
								</SelectTrigger>
								<SelectContent>
									{#each hashes as hash}
										<SelectItem value={hash.value} label={hash.name} />
									{/each}
								</SelectContent>
							</Select>
						</div>
						<div>
								<Textarea rows="5"
													id="hashOutput"
													class="form-control">{generated.hash}</Textarea>
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
							<Input id="base64EncodeInput" type="text" />
						</div>
						<div>
							<Textarea id="base64EncodeOutput"></Textarea>
						</div>

						<div>
							<Label for="base64DecodeInput"
										 class="form-label">Decode</Label>
							<Input id="base64DecodeInput" type="text" />
						</div>
						<div>
							<Textarea id="base64DecodeOutput"></Textarea>
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
							<Input id="mongoDbIdInput" type="text" />
						</div>
						<div>
							<Label for="mongoDbIdOutput">Timestamp</Label>
							<Input type="text" id="mongoDbIdOutput" />
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




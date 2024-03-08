import type { HashObject, PasswordOptions } from '$lib/types/tools';

export const defaultHashObject = (): HashObject => {
	return {
		text: '',
		alg: 'sha-512'
	};
};

export const defaultPasswordOptions = (): PasswordOptions => {
	return {
		length: 16,
		numeric: true,
		special: true,
		uppercase: true,
		lowercase: true
	};
};

export async function hashText(hashObject: HashObject) {
	const hash = await fetch('/api/hash', {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(hashObject)
	}).then((j) => j.json());

	return hash.result;
}

export async function generatePassword(passwordObject: PasswordOptions) {
	const ps = await fetch('/api/password', {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(passwordObject)
	}).then((j) => j.json());

	return ps.result;
}

async function encodeText() {}

async function decodeText() {}

async function mongoIdConvert() {}

import type { Base64Object, HashObject, MongoDbObject, PasswordOptions, TextObject } from '$lib/types/tools';
import { frontend_api_path } from '$lib/stores/settings';
import { get } from 'svelte/store';


export const defaultHashObject = (): HashObject => {
	return {
		text: '',
		alg: ''
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

export const defaultTextObject = (): TextObject => {
	return {
		text: ''
	}
}

export const defaultBase64Object = (): Base64Object => {
	return defaultTextObject();
}

export const defaultMongoDbIdObject = (): MongoDbObject => {
	return {object_id: ''};
}

export async function hashText(hashObject: HashObject) {
	const hash = await fetch(`${get(frontend_api_path)}/hash`, {
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
	const ps = await fetch(`${get(frontend_api_path)}/password`, {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(passwordObject)
	}).then((j) => j.json());

	return ps.result;
}

export async function base64Encode(base64Object: Base64Object) {
	return base64Convert('encode', base64Object);
}

export async function base64Decode(base64Object: Base64Object) {
	return base64Convert('decode', base64Object);
}

async function base64Convert(method: 'encode' | 'decode', base64Object: Base64Object) {
	const b64o = await fetch(`${get(frontend_api_path)}/base64/${method}`, {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(base64Object)
	}).then((j) => j.json());
	return b64o.result;
}

export async function mongoIdConvert(mdbObj: MongoDbObject) {
	const mdbId = await fetch(`${get(frontend_api_path)}/convert/mongodb/id`, {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(mdbObj)
	}).then((j) => j.json());

	return mdbId.result;
}


export async function generateQrCode(textObject: TextObject) {
	const qr = await fetch(`${get(frontend_api_path)}/qrcode`, {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(textObject)
	}).then((j) => j.json());
	return 'data:image/png;base64,' + qr.result;
}
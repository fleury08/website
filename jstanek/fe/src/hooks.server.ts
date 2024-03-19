import { error, type Handle } from '@sveltejs/kit';
import { ENV_BACKEND_API_PATH, ENV_BACKEND_URL, ENV_FRONTEND_API_PATH, ENV_FRONTEND_URL } from '$env/static/private';
import { env } from '$env/dynamic/private';


export const handle: Handle = async ({ event, resolve }) => {
	const fe_url = ENV_FRONTEND_URL + ENV_FRONTEND_API_PATH;

	// reject requests that don't come from the webapp, to avoid your proxy being abuse
	if (env.NODE_ENV === 'production') {
		const origin = event.request.headers.get('Origin');
		console.log(origin);
		if (!origin || new URL(origin).origin !== event.url.origin) {
			throw error(403, 'Request Forbidden.');
		}
	}

	// API PROXY
	if (event.request.url.startsWith(fe_url)) {
		return apiProxyHandle({
			event,
			resolve
		})
	}
	//TODO: WS proxy

	return resolve(event);
};


const apiProxyHandle: Handle = async ({ event }) => {
	const be_url = ENV_BACKEND_URL + ENV_BACKEND_API_PATH;
	const backend_request = be_url + event.url.pathname.slice(ENV_FRONTEND_API_PATH.length+1);
	event.request.headers.delete('connection');

	return fetch(backend_request, {
		method: event.request.method,
		headers: event.request.headers,
		body: await event.request.body?.getReader().read().then((r) => r.value) || undefined
	}).catch((err) => {
		console.log('Could not proxy API request: ', err);
		throw err;
	});

};


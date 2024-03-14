import { sequence } from '@sveltejs/kit/hooks';
import { proxyHandle } from '@born05/sveltekit-proxy';
import { ENV_BACKEND_URL } from '$env/static/private';

export const handle = sequence(
	proxyHandle({
		'/api': `${ENV_BACKEND_URL}`
	})
);
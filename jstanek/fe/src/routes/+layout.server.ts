import type { LayoutServerLoad } from './$types';
import { ENV_FRONTEND_API_PATH, ENV_FRONTEND_URL } from '$env/static/private';

export const load: LayoutServerLoad = async () => {
	return {
		frontend_api_url: ENV_FRONTEND_URL+ENV_FRONTEND_API_PATH
	};
};
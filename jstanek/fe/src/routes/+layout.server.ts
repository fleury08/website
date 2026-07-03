import type { LayoutServerLoad } from './$types';
import {
	ENV_FRONTEND_API_PATH,
	ENV_FRONTEND_WS_PATH,
} from '$env/static/private';

export const load: LayoutServerLoad = async () => {
	return {
		frontend_api_path: ENV_FRONTEND_API_PATH,
		frontend_ws_path: ENV_FRONTEND_WS_PATH,
	};
};
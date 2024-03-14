import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, loadEnv } from 'vite';
import Icons from 'unplugin-icons/vite';


export default defineConfig(({ mode }) => {
	/* IMPORTANT: Load env variables from .env file
	 * Plugins do not work without this, in this case Websocket plugin
	 * won't load any svelte env variables from .env file
	 */
	const env = loadEnv(mode, process.cwd(), '');
	return {
		plugins: [sveltekit(),
			Icons({
				compiler: 'svelte'
			})],
		server: {
			proxy: {
				'/api':
					{
						target: env.ENV_BACKEND_URL ?? 'http://localhost:8000',
						changeOrigin: true,
						secure: false,
						rewrite: (path) => path.replace(/^\/api/, '')
					}

			}
		}
	}
});
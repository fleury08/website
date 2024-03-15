import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/kit/vite';
import * as child_process from 'node:child_process';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: [vitePreprocess({})],

	kit: {
		version: {
			name: child_process.execSync('git rev-parse HEAD').toString().trim()
		},
		// adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
		// If your environment is not supported or you settled on a specific environment, switch out the adapter.
		// See https://kit.svelte.dev/docs/adapters for more information about adapters.
		adapter: adapter(),

		vite: () => ({
		server: {
			proxy: {
				'/api':
					{
						target: process.env.ENV_BACKEND_URL ?? 'http://localhost:8000',
						changeOrigin: true,
						secure: false,
						rewrite: (path) => path.replace(/^\/api/, '')
					}

			}
		}
	})
	},
};

export default config;

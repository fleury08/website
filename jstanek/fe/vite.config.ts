import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import Icons from 'unplugin-icons/vite';


export default defineConfig(() => {
	return {
		plugins: [sveltekit(),
			Icons({
				compiler: 'svelte'
			})],
		//dev proxy settings, prod uses reverse proxy
		server: {
			proxy:{
				'/api': {
					target: 'http://127.0.0.1:8000',
					ssl: false,
					changeOrigin: true,
					secure: false,
				},
				'/ws':{
					target: 'http://127.0.0.1:8000',
					ssl: false,
					ws: true,
					changeOrigin: true
				}
			}
		}
	}
});
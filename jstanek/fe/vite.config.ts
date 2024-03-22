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
					target: 'http://localhost:8000',
					changeOrigin: true,
					secure: false
				},
				'/ws':{
					target: 'http://localhost:8000',
					ws: true,
					changeOrigin: true
				}
			}
		}
	}
});
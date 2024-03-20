import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import Icons from 'unplugin-icons/vite';


export default defineConfig(() => {
	return {
		plugins: [sveltekit(),
			Icons({
				compiler: 'svelte'
			})],
	//dev proxy settings
		server: {
			proxy:{
				'/api': {
					target: 'http://localhost:8000',
					changeOrigin: true,
					secure: false,
					rewrite: (path) => path.replace(/^\/api/, '')
				},
				'/ws':{
					target: 'http://localhost:8000',
					ws: true,
				}
			}
		}
	}
});
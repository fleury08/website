import Icons from 'unplugin-icons/vite';
import tailwindcss from '@tailwindcss/vite';
import {sveltekit} from '@sveltejs/kit/vite';
import {defineConfig} from 'vite';

export default defineConfig({
    plugins: [tailwindcss(), sveltekit(), Icons({
        compiler: 'svelte'
    })],
    //dev proxy settings, prod uses reverse proxy
    server: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
                secure: false,
            },
            '/ws': {
                target: 'http://127.0.0.1:8000',
                ws: true,
                changeOrigin: true
            }
        }
    }
});
import adapter from '@sveltejs/adapter-node';
import {vitePreprocess} from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    kit: {
        adapter: adapter(),

        // ... other config
        alias: {
            "@/*": "./path/to/lib/*",
        },

        experimental: {
            remoteFunctions: true
        }
    },
    compilerOptions: {
        experimental: {
            async: true
        }
    },
    preprocess: vitePreprocess(),
};
export default config;
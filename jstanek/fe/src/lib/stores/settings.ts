import { writable } from 'svelte/store';

export const frontend_path = writable(new URL('http://localhost'))
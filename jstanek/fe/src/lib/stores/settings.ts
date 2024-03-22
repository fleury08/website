import { writable } from 'svelte/store';

export const frontend_api_path = writable('/api')
export const frontend_ws_path = writable('/ws')

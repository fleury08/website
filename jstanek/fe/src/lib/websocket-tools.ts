import { browser } from '$app/environment'

export const createWsConnection = (ws_path: string) => {

	if (!browser) return null
	console.log('Creating WS connection', ws_path)
	const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
	const host = window.location.host
	const ws = new WebSocket(protocol + '//' + host + ws_path)
	ws.addEventListener('open', () => {
		console.log('Opened WS connection')
	})
	ws.addEventListener('message', (event) => {
		console.log(event.data)
	})
	ws.addEventListener('close', (event) => {
		console.log('Closed WS connection', event.code)
	})
	ws.addEventListener('error', (event) => {
		console.log(event)
	})
	return ws
}

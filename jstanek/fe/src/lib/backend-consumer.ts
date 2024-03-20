import { type Writable, writable } from 'svelte/store';


type ApiObjects = {
	[key: string]: CallableFunction
}

type WsObjects = {
	[key: string]: WebSocket
}

export const createWsConnection = (key: string, url: string) => {

	const ws = new WebSocket(url);
	ws.addEventListener("open", () => {
		console.log();
	})
}


class BackendConsumer {

	public webservices: WebSocket = new WebSocket("ws://localhost:8000/ws");
	public apis: Writable<ApiObjects> = writable({});


	public addApi = (key: string, fn: CallableFunction) => {
		this.apis.update((a) => {
			a[key] = fn;
			return a;
		});
	}

	public addWs = (key: string, ws: WebSocket) => {
		this.webservices.update((a) => {
			a[key] = ws;
			return a;
		});
	}

	public rmApi = (key: string) => {
		this.apis.update((a) => {
			delete a[key];
			return a;
		});
	}

	public rmWs = (key: string) => {
		this.webservices.update((a) => {
			delete a[key];
			return a;
		});
	}


}
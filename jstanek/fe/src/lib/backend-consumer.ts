
export const createWsConnection = (ws_url: URL) => {

	ws_url.protocol="ws";
	const ws = new WebSocket(ws_url);
	ws.addEventListener("open", () => {
		console.log("Opened WS connection");
	})
	ws.addEventListener("message", (event) => {
		console.log(event.data);
	})
	ws.addEventListener("close", (event) => {
		console.log("Closed WS connection", event.code);
	})
	ws.addEventListener("error", (event) => {
		console.log(event);
	})
	return ws
}

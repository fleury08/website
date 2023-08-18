
export class Api{

    api_address: string
    api_token: string | null

    constructor(api_address: string){
        if (api_address == null){
            this.api_address = window.location.protocol+"//"+window.location.hostname+":"+window.location.port+window.location.pathname+"api";
        }else {
            this.api_address = api_address
        }
        this.api_token = new URLSearchParams(window.location.search).get("token");
    }

    async sendRequest(request: {query: any, method: string}){
        return await fetch(this.api_address, {
            method: request.method,
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(request.query)
        });
    }

    async getBase64(query: string, method: string, target: HTMLInputElement){
        const request = {
            'query': query,
            'method': method
        };
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
            target.value = json['result']
        });
    }

    async getPassword(length: number, lowercase: boolean, uppercase: boolean, numbers: boolean, symbols: boolean, target: HTMLInputElement){
        const request = {
            'query': {
                'lowercase': lowercase,
                'uppercase': uppercase,
                'numbers': numbers,
                'symbols': symbols,
                'length': length
            },
            'method': 'GET'
        };
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
             target.value = json['result']
        });
    }

    async getMongoId(mongoId: string, target: HTMLInputElement){
        const request={
            'query': mongoId,
            'method': 'GET'
        };
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
             target.value = json['result']
        });
    }

    async getHash(alg: string, value: string, target: HTMLInputElement){
        const request = {
            'query': {
                'alg': alg,
                'value': value
            },
            'method': 'GET'
        }
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
             target.value = json['result']
        });
    }
}
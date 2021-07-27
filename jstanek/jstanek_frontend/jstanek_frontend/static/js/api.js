
class Api{

    constructor(api_address){
        if (api_address == null){
            this.api_address = window.location.protocol+"//"+window.location.hostname+":"+window.location.port+window.location.pathname+"api";
        }else {
            this.api_address = api_address
        }
        this.api_token = new URLSearchParams(window.location.search).get("token");
    }

    async sendRequest(request){
        return await fetch(this.api_address, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(request)
        });
    }

    async getBase64(query, method, target){
        var request = {
            'query': query,
            'method': method
        };
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
            target.value = json['result']
        });
    }

    async getPassword(length, lowercase, uppercase, numbers, symbols, target){
        var request = {
            'query': {
                'lowercase': lowercase,
                'uppercase': uppercase,
                'numbers': numbers,
                'symbols': symbols,
                'length': length
            }
        };
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
             target.value = json['result']
        });
    }

    async getMongoId(mongoId, target){
        var request={
            'query': mongoId
        };
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
             target.value = json['result']
        });
    }

    async getHash(alg, query, target){
        var request = {
            'query': query,
            'alg': alg
        }
        this.sendRequest(request).then(r=>{return r.json()}).then(json=>{
             target.value = json['result']
        });
    }
}
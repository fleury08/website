
class Api{

    constructor(api_address){
        if (api_address == null){
            this.api_address = window.location.protocol+"//"+window.location.hostname+":"+window.location.port+window.location.pathname+"api";
        }else {
            this.api_address = api_address
        }
        this.api_token = new URLSearchParams(window.location.search).get("token");
    }

    async sendRequest(request,target){
        let response = await fetch(this.api_address, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(request)
        });
        var txt = await response.text();
        target.value = txt;
    }

    async getBase64(query, method, target){
        var request = {
            'query': query,
            'method': method
        };
        this.sendRequest(request,target);
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
        this.sendRequest(request,target);
    }

    async getMongoId(mongoId, target){
        var request={
            'query': mongoId
        };
        this.sendRequest(request,target);
    }

    async getHash(alg, query, target){
        var request = {
            'query': query,
            'alg': alg
        }
        this.sendRequest(request,target);
    }
}
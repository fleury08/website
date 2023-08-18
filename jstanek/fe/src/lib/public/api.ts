
const api_address = "http://localhost:8000/";
export const encodeBase64 = async (to_encode: string) => {
    return fetch(api_address+"base64/encode/"+to_encode, {
        mode: "no-cors",
    })
}

export const aboutPage = async () => {
    return fetch(api_address, {
        mode: "no-cors",
    })
}
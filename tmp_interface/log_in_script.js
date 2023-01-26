function loginUserForm() {
    const name = document.getElementById("name").value;
    const password = document.getElementById("password").value;
    prepareDataCreateUser(name, password);
}

async function prepareDataCreateUser(name, password) {
    name = String(name)
    password = String(password)

    encoder = new TextEncoder();
    dataArray = encoder.encode(password);
    hash = await crypto.subtle.digest('SHA-512', dataArray);
    password_hash = bufferToHexString(hash);

    password = ""

    sendDataToAPI(name, password_hash)
}

function bufferToHexString(buffer) {
    const byteArray = new Uint8Array(buffer);
    const hexCodes = [...byteArray].map(value => {
        const hexCode = value.toString(16);
        const paddedHexCode = hexCode.padStart(2, '0');
        return paddedHexCode;
    });
    return hexCodes.join('');
}

function sendDataToAPI(name, password_hash) {
    const data = { name: name, password_hash: password_hash };
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    };
    fetch('http://127.0.0.1:8000/login', options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}
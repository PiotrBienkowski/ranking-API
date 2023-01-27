API_link = "http://127.0.0.1:5000/"

// start of temporary interface

function loginUserForm() {
    const name = document.getElementById("name").value;
    const password = document.getElementById("password").value;
    loginUser(name, password)
}

function createUserForm() {
    const name = document.getElementById("name").value;
    const password = document.getElementById("password").value;
    createUser(name, password);
}

function loginUserForm() {
    const user_id = document.getElementById("user_id").value;
    const password_hash = document.getElementById("password_hash").value;
    const result = document.getElementById("result").value;
    const points = document.getElementById("points").value;
    
    updateResult(user_id, password_hash, result, points);
}

// end of temporary interface

function createUser(name, password) {
    prepareDataUser(name, password, "create-user")
}

function loginUser(name, password) {
    prepareDataUser(name, password, "login");
}

function updateResult(user_id, password_hash, result, points) {
    sendDataToAPI({ user_id: user_id, password_hash: password_hash, result: result, points: points }, "update-result")
}

async function prepareDataUser(name, password, link) {
    name = String(name)
    password = String(password)

    encoder = new TextEncoder();
    dataArray = encoder.encode(password);
    hash = await crypto.subtle.digest('SHA-512', dataArray);
    password_hash = bufferToHexString(hash);
    password = ""

    sendDataToAPI({ name: name, password_hash: password_hash }, link)
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

function sendDataToAPI(tmp_data, link) {
    const data = tmp_data
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    };
    fetch(API_link + link, options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}
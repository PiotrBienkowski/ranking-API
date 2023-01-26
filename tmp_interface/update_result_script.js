function loginUserForm() {
    const user_id = document.getElementById("user_id").value;
    const password_hash = document.getElementById("password_hash").value;
    const result = document.getElementById("result").value;
    const points = document.getElementById("points").value;
    
    sendDataToAPI(user_id, password_hash, result, points);
}

function sendDataToAPI(user_id, password_hash, result, points) {
    const data = { user_id: user_id, password_hash: password_hash, result: result, points: points };
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    };
    fetch('http://127.0.0.1:8000/update-result', options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}
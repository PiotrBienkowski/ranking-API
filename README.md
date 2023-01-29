# ranking-API
A simple API for rankings created in flask

API functionality:
- adding user
- users login
- updating users' max-score and level
- displaying the ranking

In the [tmp_interface](https://github.com/PiotrBienkowski/ranking-API/tree/main/tmp_interface)
 directory there is a [tmp_interface](https://github.com/PiotrBienkowski/ranking-API/blob/main/tmp_interface/script.js) file with all the functions needed on the client side.

### Adding user
```bash
function createUser(name, password)
```
### Users login
The API returns the user ID in case of successful login. 
```bash
function loginUser(name, password)
```
### Updating users
```bash
function updateResult(user_id, password_hash, result, points)
```
### Displaying the ranking
API returns first 10 players in json format. 
```bash
https://[API_LINK]/ranking
```
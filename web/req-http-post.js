// fetch利用 POST版
fetch('http://localhost:5000/test', {
    headers: {
        'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify({
        ctf: 'book'
    })
})
.then(response => {
    if (response.ok) {
        return response.text()
    } else {
        throw new Error()
    }
})
.then(text => console.log(text))
.catch(error => console.error(error))
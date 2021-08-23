import fetch from 'node-fetch'

fetch('http://localhost:5000/test', {
    method: 'GET'
})
.then((Response) => {
    if (Response.ok) {
        console.log("[200 OK]", Response.text())
    } else {
        console.log("[ERROR]", Response.statusText)
    }
})
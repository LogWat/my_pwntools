// URL指定(method省略時GET)
fetch('http://localhost:5000/test')
    .then((response) => {
        if (response.ok) {
            return response.text()
        } else {
            throw new Error()
        }
    })
    // レスポンスを正常にテキストに変換できた場合
    .then(text => console.log(text))
    // エラーだった場合
    .catch(error => console.error(error))
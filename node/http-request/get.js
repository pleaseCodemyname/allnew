const https = require('https'); //https를 이용한 request방법

const data = JSON.stringify({
    todo: 'Buy the milk'
})

const options = {
    hostname : '192.168.1.189',
    port : 8000,
    path : '/todos',
    method : 'GET'
}

const req = https.request(options, res => {
    console.log(`statusCode : ${res.statusCode}`);
    res.on('data', d => {
        process.stdout.write(d);
    })
})

req.on('error', error => {
    console.log(error)
})

res.write(data)
req.end()
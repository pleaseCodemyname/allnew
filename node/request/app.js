const express = require('express'); //npm install 할때 require에 있는 것 install
const request = require('request');
const CircularJSON = require('circular-json')
const app = express();

app.get('/', (req, res) => {
    res.send("Web Server started...");
})

app.get('/hello', (req, res) => {  // 내 Hello
    res.send("Hello World - Yun");
})

let option = "http://192.168.1.189:8000/Hello"
app.get("/rhello", function (req, res) {   //원격 Hello
    request(option, {json:true},(err, result, body) => {
    if(err) { return console.log(err)} 
    res.send(CircularJSON.stringify(body))
    })
})

const data = JSON.stringify({ todo: 'Buy the milk'})
app.get("/data", function (req, res) {
    res.send(data);
})

option = "http:192.168.1.189:8000/data"
app.get("/rdata", function (req, res) {
  request(option, {json:true},(err, result, body) => {
    if(err) { return console.log(err)} 
    res.send(CircularJSON.stringify(body))
    })
})

app.listen(8000, function () {
    console.log('8000 Port : Server Started....');
})
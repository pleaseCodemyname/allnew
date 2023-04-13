const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/hello', (req, res) => {
    res.send('Hello World~!!')
})

// request O, query X
app.get('/select', (req, res) => {
    const result = connection.query('select * from user');
    console.log(result);
    //res.send(result);
    res.writeHead(200);
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
        </head>
        <body>
        <table border="1" style="margin:auto; text-align:center;">
        <thead>
            <tr><th>User ID</th><th>Password</th></tr>
        </thead>
        <tbody>
        `;
    for (var i = 0; i < result.length; i++) {
        template += `
        <tr>
            <td>${result[i]['userid']}</td>
            <td>${result[i]['passwd']}</td>
        </tr>
        `;
    }
    template += `
        </tbody>
        </table>
        </body>
        </html>
    `;
    res.end(template);
})

// request O, query X
app.post('/select', (req, res) => {
    const result = connection.query('select * from user');
    console.log(result);
    res.send(result);
})

// request O, query O
// request O, query O
app.get('/selectQuery', (req, res) => {
    const id = req.query.id;
    if (id == "") {
        res.writeHead(200);
        var template = `
    <!doctype html>
    <html>
    <head>
        <title>Error</title>
        <meta charset="utf-8">
    </head>
    <body>
        <div>
            <h3 style="margin-left: 30px">필드 입력</h3>
        </div>
    </body>
    </html>
    `;
        res.end(template);
    } else {
        let result = connection.query("select * from user where userid=?", [id]);
        if (result.length == 0) {
            var template = `
            <!doctype html>
            <html>
            <head>
                <title>Error</title>
                <meta charset="utf-8">
            </head>
            <body>
                <div>
                    <h3 style="margin-left: 30px">사용자가 존재하지 않음</h3>
                </div>
            </body>
            </html>
            `;
                res.end(template);
            } else {
                

    const result = connection.query("select * from user where userid=?", [id]);
    console.log(result);
    //res.send(result);
    res.writeHead(200);
    var template2 = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
        <table border="2" style="margin:auto; text-align:center;">
        <thead>
            <tr><th>User ID</th><th>Password</th></tr>
        </thead>
        <tbody>
        `;
    for (var i = 0; i < result.length; i++) {
        template2 += `
        <tr>
            <td>${result[i]['userid']}</td>
            <td>${result[i]['passwd']}</td>
        </tr>
        `;
    }
    template2 += `
        </tbody>
        </table>
        </body>
        </html>
    `;
    res.end(template2);
}}
})


// request O, query O
app.post('/selectQuery', (req, res) => {
    const id = req.body.id;
    // console.log(req.body);
    const result = connection.query("select * from user where userid=?", [id]);
    if (id == "") {
        res.redirect('index.html')}
var template = `
            <!doctype html>
            <html>
            <head>
                <title>Error</title>
                <meta charset="utf-8">
            </head>
            <body>
                <div>
                    <h3 style="margin-left: 30px">Register Failed</h3>
                    <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
                    <a href="register.html" style="margin-left: 30px"> 다시 시도하기</a>
                </div>
            </body>
            </html>
            `;
            res.end(template);
    
    //console.log(result);
    //res.send(result);
})

// request O, query O
app.post('/insert', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("insert into user values (?, ?)", [id, pw]);
    if (result.length == 0 ) {
        res.send("아이디와 패스워드를 입력해 주세요");
    } else {
        
    }
    //console.log(result);
    res.redirect('/selectQuery?id=' + req.body.id);
})

// request O, query O
app.post('/update', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("update user set passwd=? where userid=?", [pw, id]);
    //console.log(result);
    res.redirect('/selectQuery?id=' + req.body.id);
})

// request O, query O
app.post('/delete', (req, res) => {
    const id = req.body.id;
    const result = connection.query("delete from user where userid=?", [id]);
    console.log(result);
    res.redirect('/select');
})

module.exports = app;
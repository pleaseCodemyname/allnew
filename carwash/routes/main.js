const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const mongoose = require("mongoose");
// const async = require("async");
const env = require('dotenv').config({ path: "../../.env" });

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true })); //여기까지는 건들 필요X

function template_nodata(res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
        <h3>데이터가 존재하지 않습니다.</h3>
    </body>
    </html>
    `;
    res.end(template);
}

function template_result(result, res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
    <table border="1" style="margin:auto;">
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
}

//define schema
var userSchema = mongoose.Schema({
    userid: String,
    passwd: Number,
    name: String,
    gender: String,
    mobile: String,
    laptitude: String,
    longitude: String
}, {
    versionKey: false
})

//create model with mongodb collection and schema
var User = mongoose.model('userTbl', userSchema);

app.get('/hello', (req, res) => {
    res.send('hello world~!!')
})

// request O, query X
app.get('/select', (req, res) => {
    const result = connection.query('select * from userTbl');
    console.log(result);
    res.send(result);
})

// list
app.get('/list', function (req, res, next) {
    User.find({}, function (err, docs) {
        if (err) console.log('err')
        res.send(docs)
    })
})

// get
app.get('/get', function (req, res, next) {
    var userid = req.query.input 
    User.findOne({'userid':userid }, function (err, doc) {
        if (err) console.log('err')
        res.send(doc)
    })
})

// insert
    app.post('/insert', function(req, res, next) {
        var userid = req.body.userid;
        var name = req.body.name;
        var city = req.body.city; //post와 req.body는 짝꿍
        var sex = req.body.sex;
        var age = req.body.age;
        var user = new User({'userid': userid, 'name': name, 'city': city, 'sex': sex, 'age': age})
    
        user.save(function(err, silence) {
            if(err) {
                console.log('err')
                res.status(500).send('insert error')
                return;
            }
            res.status(200).send("Inserted")
        })
    })

    //update
    app.post('/update', function(req, res, next) {
        var userid = req.body.userid;
        var name = req.body.name;
        var city = req.body.city; //post와 req.body는 짝꿍
        var sex = req.body.sex;
        var age = req.body.age;

        User.findOne({ 'userid':userid }, function(err, user){
            if(err) {
                console.log('err')
                res.status(500).send('update error') //500은 error
                return;
            }
        user.name = name;
        user.sex = sex;
        user.city = city;
        user.age = age;
            
        user.save(function(err, silence) {
            if(err) {
                console.log('err')
                res.status(500).send('update error')
                return;
                }
            res.status(200).send("Updated")
            })
        })
})
        
// delete
    app.post('/delete', function (req, res, next) {
        var userid = req.body.userid;
        var user = User.find({'userid':userid})
        user.deleteOne(function(err) {
            if(err) {
                console.log('err')
                res.status(500).send('delete error')
                return;
            }
            res.status(200).send("Removed")
        })
    })

//mysql 
// request O, query X
app.post('/select', (req, res) => {
    const result = connection.query('select * from userTbl');
    console.log(result);
    res.send(result);
})

// request O, query O
app.get('/selectQuery', (req, res) => {
    const userid = req.query.userid;
    const result = connection.query("select * from userTbl where userid=?", [userid]);
    console.log(result);
    res.send(result);
})

// request O, query O
app.post('/selectQuery', (req, res) => {
    const userid = req.body.userid;
    const result = connection.query("select * from userTbl where userid=?", [userid]);
    console.log(result);
    res.send(result);
})

// request O, query O
app.post('/insert', (req, res) => {
    const { userid, name, mobile, gender, birth, mdate } = req.body;
    const result = connection.query("insert into userTbl values (?, ?, ?, ?, ?, ?)", [userid, name, mobile, gender, birth, mdate]);
    console.log(result);
    res.redirect('/selectQuery?userid=' + req.body.id);
})

// request O, query O
app.post('/update', (req, res) => {
    const { userid, name, mobile, gender, birth, mdate } = req.body;
    const result = connection.query("update userTbl set Name=?, Mobile=?, Gender=?, Birth=?, mDate=? where userid=?", [userid, name, mobile, gender, birth, mdate]);
    console.log(result);
    res.redirect('/selectQuery?userid=' + req.body.id);
})

// request O, query O
app.post('/delete', (req, res) => {
    const userid = req.body.id;
    const result = connection.query("delete from userTbl where userid=?", [userid]);
    console.log(result);
    res.redirect('/select');
})

module.exports = app;
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

//request O, query X (req는 있는데 parameter가 없음)
app.get('/select', (req, res) => {
    const result = connection.query('select * from user');    //db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   //밑에 터미널창에 나타남
    res.send(result);  // 밑에 터미널 창에 연결해주는 역할
})

//request O, query X 
app.post('/select', (req, res) => {
    const result = connection.query('select * from user');    //db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   //밑에 터미널창에 나타남
    res.send(result);  // 밑에 터미널 창에 연결해주는 역할
})

//request O, query X 
app.get('/selectQuery', (req, res) => {
    const userid = req.query.userid;  //id를 where 조건으로 사용할 수 있음
    const result = connection.query("select * from user where userid=?", [userid]);    // ?는 id를 받아서 where? 에 출려해줌 db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   //밑에 터미널창에 나타남
    res.send(result);  // 밑에 터미널 창에 연결해주는 역할
})

//request O, query X 
app.post('/selectQuery', (req, res) => {    //pwd로 받으면 불안전함  //get은 post/param // post=body로 보내야함
    const userid = req.body.userid;  //id를 where 조건으로 사용할 수 있음
    const result = connection.query("select * from user where userid=?", [userid]);    // ?는 id를 받아서 where? 에 출려해줌 db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   //밑에 터미널창에 나타남
    res.send(result);  // 밑에 터미널 창에 연결해주는 역할
})

//request O, query X 
app.post('/insert', (req, res) => {    //pwd로 받으면 불안전함  //get은 post/param // post=body로 보내야함
    const { id, pw } = req.body;  //id를 where 조건으로 사용할 수 있음
    const result = connection.query("insert into user values (?, ?)", [id, pw]);    // ?는 id를 받아서 where? 에 출려해줌 db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   //밑에 터미널창에 나타남
    res.redirect('/selectQuery?userid=' + req.body.id);   //?userid = get에게 요청하는 것임
})

//request O, query X 
app.post('/update', (req, res) => {    
    const { id, pw} = req.body;  
    const result = connection.query("update user set passwd=? where userid=?", [pw, id]);  
    console.log(result);   
    res.redirect('/selectQuery?userid=' + req.body.id);   
})

//request O, query X 
app.post('/delete', (req, res) => {    
    const id= req.body.id;  
    const result = connection.query("delete from user where userid=?", [id]);  
    console.log(result);   
    res.redirect('/select');   
})

module.exports = app;
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });  ///../env로 숨김

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));  ///body Parser말고 urlencoded에서 true로 함
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/hello', (req, res) => {
    res.send('환영합니다~!!')
})

//request O, query X (req는 있는데 Query parameter가 없음)
app.get('/select', (req, res) => {    ///쿼리 방식이기 때문에 주소만 있으면 전달이 됨
    const result = connection.query('select * from super_user');    //db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   //밑에 터미널창에 나타남
    res.send(result);  // 밑에 터미널 창에 연결해주는 역할
})

//request O, query X 
app.post('/select', (req, res) => {
    const result = connection.query('select * from super_user');   
    console.log(result);   
    res.send(result);  
})

//request O, query X 
app.get('/selectQuery', (req, res) => {
    const userid = req.query.userid;  
    const result = connection.query("select * from super_user where userid=?", [userid]);    // ?는 id를 받아서 where? 에 출려해줌 db에 접속하는 기능 query결과가 result에 들어감
    console.log(result);   
    res.send(result);  
})

//request O, query X 
app.post('/selectQuery', (req, res) => {    //pwd로 받으면 불안전함  //get은 post/param // post=body로 보내야함
    const userid = req.body.userid;  
    const result = connection.query("select * from super_user where userid=?", [userid]);   
    console.log(result);   
    res.send(result); 
})

//request O, query X 
app.post('/insert', (req, res) => {    
    const { userid, passwd, address, birth, phone_num, sc_size } = req.body; 
    const result = connection.query("insert into super_user values (?, ? ,?, ?, ?, ?)", [userid, passwd, address, birth, phone_num, sc_size]);   
    console.log(result);   //밑에 터미널창에 나타남
    res.redirect('/selectQuery?userid=' + req.body.userid);   
    //?userid = get에게 요청하는 것임
    //  //id를 where 조건으로 사용할 수 있음
    // console.log(id+pw+addr+bday+number+cpu)
})

//request O, query X 
app.post('/update', (req, res) => {    
    const { userid, passwd, address, birth, phone_num, sc_size} = req.body;  
    const result = connection.query("update super_user set passwd=?, address=?, birth=?, phone_num=?, sc_size=?  where userid=?", [passwd, address, birth, phone_num, sc_size, userid]);  
    console.log(result);   
    res.redirect('/selectQuery?userid=' + req.body.userid);   
})

//request O, query X 
app.post('/delete', (req, res) => {    
    const userid= req.body.userid;  
    const result = connection.query("delete from super_user where userid=?", [userid]);  
    console.log(result);   
    res.redirect('/select');   
})

module.exports = app;
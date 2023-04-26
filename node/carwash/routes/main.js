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

function template_nodata(res) {   
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
        <tr><th>store_name</th>
            <th>gu</th>
            <th>type_of_business</th>
            <th>address</th>
            <th>start_work</th>
            <th>end_work</th>
            <th>tel_no</th>
            <th>latitude</th>
            <th>longitude</th></tr>
    </thead>
    <tbody>
    `;
    for (var i = 0; i < result.length; i++) {   
        template += `
    <tr>
        <td>${result[i]['store_name']}</td> 
        <td>${result[i]['gu']}</td>
        <td>${result[i]['type_of_business']}</td>
        <td>${result[i]['address']}</td>
        <td>${result[i]['start_work']}</td>
        <td>${result[i]['end_work']}</td>
        <td>${result[i]['tel_no']}</td>
        <td>${result[i]['latitude']}</td>
        <td>${result[i]['longitude']}</td>
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
function template_user(result, res) {
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
        <tr><th>id</th>
            <th>pwd</th>
            <th>address</th>
            <th>latitude</th>
            <th>longitude</th>
    </thead>
    <tbody>
    `;
    for (var i = 0; i < result.length; i++) {   
        template += `
    <tr>
        <td>${result[i]['id']}</td> 
        <td>${result[i]['pwd']}</td>
        <td>${result[i]['address']}</td>
        <td>${result[i]['latitude']}</td>
        <td>${result[i]['longitude']}</td>
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

app.get('/hello', (req, res) => {
    res.send('Hello World~!!')
})

app.post('/login', (req, res) => {
    const { id, pwd } = req.body; //post니깐 body, {id, pwd}니깐 req.body(.id는 한개만 req받을때)
    // const stringId = String(id);
    // const stringPwd = String(pwd)
    const result = connection.query("select * from user where id=? and pwd=?", [id, pwd]);
    // console.log(result);
    if (result.length == 0) {
        return res.redirect('error.html')
    }
    if (id == 'admin' || id == 'root') {
        console.log(id + " => Administrator Logined")
        return res.redirect('member.html?id=' + id); //주소뒤에 붙음
    } else {
        console.log(id + " => User Logined")    
        return res.redirect('user.html?id=' + id)
    }
})

app.get('/select', (req, res) => {
    const result = connection.query('select * from carWash');
    console.log(result);
    //res.send(result);
    // res.writeHead(200);
    res.write(JSON.stringify({ "ok": true, "result": result, "service": "select" })); //json.stringify = result값은 객체인데 문자로 바꿔주는 것 
    if (result.length== 0) {
        template_nodata(res)
    } else {
        template_result(result, res);
    }
})

app.post('/select', (req, res) => {
    const result = connection.query('select * from carWash');
    console.log(result);
    //res.send(result);
    res.writeHead(200);
    if (result.length== 0) {
        template_nodata(res)
    } else {
        template_result(result, res);
    }
    res.end();
})

app.get('/selectQuery', (req, res) => {
    const id = req.query.id;
    if (id == "") {
      // res.send('User-id를 입력하세요.')
      res.send("<script>alert('조회할 User-id를 입력하세요.')</script>");
    } else {
      connection.query("select * from user where id=?", [id], (err, result) => {
        if (err) {
          console.error(err);
          res.status(500).send('서버 에러');
          return;
        }
        console.log(result);
        res.send(JSON.stringify({ "ok": true, "result": result, "service": "selectQuery" }));
        if (result.length == 0) {
          template_nodata(res)
        } else {
          template_user(result, res);
        }
      });
    }
  });
  

app.post('/selectQuery', (req, res) => {
    const id = req.body.id;
    if (id == "") {
        res.send('User-id를 입력하세요.')
    } else {
        const result = connection.query("select * from user where id=?", [id]);
        console.log(result);
        // res.send(result);
        res.writeHead(200);
        if (result.length == 0) {
            template_nodata(res)
        } else {
            template_user(result, res);
        }
    }
})

app.post('/insert', (req, res) => {
    const { id, pw } = req.body;
    if (id == "" || pw == "") {   
        res.write("<script>alert('가입할 User-id를 입력하세요.')</script>")
    } else {
        let result = connection.query("select * from user where id=?", [id]);
        if (result.length > 0) {  
            res.write("<script>alert('중복된 id 입니다.'</script>")
            res.end(template);
        } else {
            result = connection.query("insert into user values (?, ?)", [id, pw]);
            console.log(result);
            res.write("<script>alert('가입되었습니다')</script>")
        }
    }
})
// app.get('/find/', (req, res) => {
//     const location = req.
// })
module.exports = app;
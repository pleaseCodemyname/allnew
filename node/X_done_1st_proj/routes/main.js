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

function template_carWash(result, res) {
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
        <tr>
        <th>store_name</th>
        <th>gu</th>
        <th>type_of_business</th>
        <th>carwash_type</th>
        <th>address</th>
        <th>start_work</th>
        <th>end_work</th>
        <th>tel_no</th>
        <th>latitude</th>
        <th>longitude</th>
        </tr>
    </thead>
    <tbody>
    `;
    for (var i = 0; i < result.length; i++) {   
        template += `
    <tr>
    <td>${result[i]['store_name']}</td> 
    <td>${result[i]['gu']}</td>
    <td>${result[i]['type_of_business']}</td>
    <td>${result[i]['carwash_type']}</td>
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
    <table border="1" style="margin:auto:";>
    <thead>
        <tr>
        <th>id</th>
        <th>pwd</th>
        <th>address</th>
        <th>latitude</th>
        <th>longitude</th>
        </tr>
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

//사용자로그인
app.post('/login', (req, res) => {
    const { id, pwd } = req.body; //post니깐 body, {id, pwd}니깐 req.body(.id는 한개만 req받을때)
    const result = connection.query("select * from user where id=? and pwd=?", [id, pwd]);
    // console.log(result);
    if (result.length == 0) {
        res.redirect('error.html')
    }
    if (id == 'admin' || id == 'root') {
        console.log(id + " => Administrator Logined")
        res.redirect('member.html?id=' + id); //주소뒤에 붙음
    } else {
        console.log(id + " => User Logined")    
        res.redirect('user.html?id=' + id)
    }
})

//사용자 가입(가입이 안됨)
app.post('/register', (req, res) => {
    const { id, pwd} = req.body;
    if (id == "") {
        res.redirect('register.html')
    } else {
        let register = connection.query("select * from user where id=?", [id]);
        if (register.length > 0) {
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
                <h3 style="margin-left: 30px">Registrer Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
                <a href="register.html" style="margin-left: 30px">다시 시도하기</a>
            </div>
        </body>
        </html>  
        `; 
            // res.send(1)
            res.end(template);
        } else {
            register = connection.query("insert into user values (?, ?)", [id, pwd])
            console.log(register);
            res.send("3")
            // res.redirect('/');
        }
    }
})

//회원 info 조회(get방식)
app.get('/user/select', (req, res) => {
    const user = connection.query('select * from user');
    console.log(user);
    //res.send(result);
    // res.writeHead(200);
    if (user.length== 0) {
        template_nodata(res)  //발표할때 얘 주석 풀기
        // res.send({ "ok": false, "users": user, "service": "user/select" }); //발표할떄는 이 Line을 주석처리
    } else {
        template_user(user, res); //발표할때 주석 풀기
        // res.send({ "ok": true, "users": user, "service": "user/select" }); //발표할떄는 이 Line을 주석처리
    }
    res.end()
})

//특정회원 조회(get방식)
app.get('/user/selectQuery', (req, res) => {
    const id = req.query.id;
    if (id == "") {
      // res.send('User-id를 입력하세요.')
      res.send("<script>alert('조회할 User-id를 입력하세요.')</script>");
    } else {
      const userId = connection.query("select * from user where id=?", [id]);
         console.log(userId);
        if (userId.length == 0) {
            template_nodata(res) // 발표할때 주석 풀기
            // res.send({ "ok": false, "userFind": userId, "service": "/user/selectQuery" });
        } else {
            template_user(userId, res); // 발표할때 주석 풀기
            // res.send({ "ok": true, "userFind": userId, "service": "/user/selectQuery" });
        }
        res.end()
    }
})

// 회원 추가(add user)
app.post('/user/add', (req, res) => {
    const { id, pwd, address, latitude,longitude } = req.body;
    if (id == "" || pwd == "") {   
        res.write("<script>alert('가입할 User-id를 입력하세요.')</script>")
    } else {
        let userAdd = connection.query("select * from user where id=?", [id]);
        if (userAdd.length > 0) {  
             template_nodata(res)
        } else {
            userAdd = connection.query("insert into user values (?, ?, ?, ?, ?)", [id, pwd, address, latitude,longitude]);
            console.log(userAdd);
            template_user(userAdd, res)
        }
    }
})

//사용자 정보 수정 XXX
app.post('/user/update', (req, res) => {
    const { id, pwd, address, latitude, longitude} = req.body;
    if (id == "" || pwd == "") {
        res.write("<script>alert('User-id를 입력하세요')</script>")
    } else {
        let user = connection.query("select * from user where id=?", [id]);
        console.log(user);
        // res.send();
        if (user.length == 0) {
            template_nodata(res)
        } else {
        user = connection.query("update user set pwd=? where id=?", [pwd, id, address, latitude, longitude]);
            // console.log(result);
            template_user(user, res)
            // res.redirect('/selectQuery?id=' + id);
        }
        res.end()
    }
})

//사용자정보 삭제
app.post('/user/delete', (req, res) => {
    const id = req.body.id;
    if (id == "") {
        // res.send('User-id를 입력하세요.')
        res.write("<script>alert('삭제할 User-id를 입력하세요')</script>")
    } else {
        let userDel = connection.query("select * from user where id=?", [id]);
        console.log(userDel);
        // res.send(result);
        // res.writeHead(200);
        if (userDel.length == 0) {
            template_nodata(res)
            // res.send({ "ok": false, "userDelete": userDel, "service": "/user/delete" });
        } else {
            userDel = connection.query("delete from user where id=?", [id]);
            template_user(userDel, res)
            // console.log(result);
            // res.redirect('/select');
            // res.send({ "ok": true, "userDelete": userDel, "service": "/user/delete" });
        }
        res.end()
    }
})




//세차장 info 조회(get방식)
app.get('/carWash/select', (req, res) => {
    const carWash = connection.query('select * from carWash');
    console.log(carWash);
    //res.send(result);
    // res.writeHead(200);
    // res.send(JSON.stringify({ "ok": true, "result": result, "service": "select" })); //json.stringify = result값은 객체인데 문자로 바꿔주는 것, 발표할때 주석 풀기
    if (carWash.length== 0) {
        template_nodata(res)  //발표할때 얘 주석 풀기
        // res.send({ "ok": false, "carWashFind": carWash, "service": "/carWash/select" }); //발표할떄는 이 Line을 주석처리
    } else {
        template_carWash(carWash, res); //발표할때 주석 풀기
        // res.send({ "ok": true, "carWashFind": carWash, "service": "/carWash/select" }); //발표할떄는 이 Line을 주석처리
    }
})

//특정세차장 조회(get방식)
app.get('/carWash/selectQuery', (req, res) => {
    const id = req.query.gu;
    if (id == "") {
      // res.send('User-id를 입력하세요.')
      res.send("<script>alert('조회할 세차장을 입력하세요.')</script>");
    } else {
      const carWashId = connection.query("select * from carWash where gu=?", [id]);
         console.log(carWashId);
        //  res.send(JSON.stringify({ "ok": false, "userFind": result, "service": "/selectQuery" }));
        // res.send(result);
        // res.writeHead(200);
        // res.write(JSON.stringify({ "ok": true, "result": result, "service": "selectQuery" })); 발표할때 주석 풀기
        if (carWashId.length == 0) {
            console.log(carWashId)
            template_nodata(res) // 발표할때 주석 풀기
            // res.send({ "ok": false, "carWashFind": carWashId, "service": "/carWash/selectQuery" });
        } else {
            template_carWash(carWashId, res); // 발표할때 주석 풀기
            // res.send({ "ok": true, "carWashFind": carWashId, "service": "/carWash/selectQuery" });
        }
        res.end()
    }
})

// 세차장 추가
app.post('/carWash/add', (req, res) => {
    const { store_name, gu, type_of_business, carwash_type, address, start_work, end_work, tel_no, latitude, longitude } = req.body;
    if (store_name == "") {   
        res.write("<script>alert('추가할 세차장을 입력하세요.')</script>")
    } else {
        let carWashName = connection.query("select * from carWash where store_name=?", [store_name]);
        console.log(carWashName);
        if (carWashName.length > 0) {  
            template_nodata(res)
        } else {
            carWashName = connection.query("insert into carWash values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [store_name, gu, type_of_business, carwash_type, address, start_work, end_work, tel_no, latitude, longitude]);
            template_user(carWashName, res)
        }
        res.end()
    }
})
//세차장 정보 수정
app.post('/carWash/update', (req, res) => {
    const { store_name, gu, type_of_business, carwash_type, address, start_work, end_work, tel_no, latitude, longitude } = req.body;
    if (store_name == "") {
        res.write("<script>alert('세차장 정보를 입력하세요')</script>")
    } else {
        let carWashModify = connection.query("select * from carWash where store_name=?", [store_name]);
        console.log(carWashModify);
        // res.send();
        if (carWashModify.length == 0) {
            // template_nodata(res)
            res.send({ "ok": false, "carWashUpdate": carWashModify, "service": "/carWash/update" });
        } else {
        carWashModify = connection.query("update carWash set =? where store_name=?", [store_name, gu, type_of_business, carwash_type, address, start_work, end_work, tel_no, latitude, longitude]);
            // console.log(result);
            res.send({ "ok": true, "userUpdate": carWashModify, "service": "/carWash/update" });
            // res.redirect('/selectQuery?id=' + id);
        }
        res.end()
    }
})

//세차장 정보 삭제
app.post('/carWash/delete', (req, res) => {
    const store_name = req.body.store_name
    if ( store_name== "") {
        // res.send('User-id를 입력하세요.')
        res.write("<script>alert('삭제할 User-id를 입력하세요')</script>")
    } else {
        let carWashDel = connection.query("select * from carWash where store_name=?", [store_name]);
        console.log(carWashDel);
        // res.send(result);
        // res.writeHead(200);
        if (carWashDel.length == 0) {
            template_nodata(res)
            res.send({ "ok": false, "carWashDel": carWashDel, "service": "/carWash/delete" });
        } else {
            carWashDel = connection.query("delete from carWash where store_name=?", [store_name]);
            // console.log(result);
            // res.redirect('/select');
            template_carWash(carWashDel,res)
        }
        res.end()
    }
})

module.exports = app;


































// app.get('/navigator', (req, res) => {
//   const { latitude, longitude } = req.body;

//   pool.getConnection((err, connection) => {
//     if (err) throw err;
    
//     // carWash 테이블에서 위도, 경도를 기준으로 가까운 순서대로 5개의 레코드를 가져오는 쿼리
//     const query = `
//       SELECT * FROM carWash ORDER BY SQRT(POWER(${latitude} - lat, 2) + POWER(${longitude} - lng, 2))
//       LIMIT 5
//     `;

//     connection.query(query, (err, rows) => {
//       connection.release();
//       if (err) throw err;
      
//       res.send(rows);
//     });
//   });
// });

// app.listen(3000, () => {
//   console.log('Server is running on port 3000');
// });

// app.post('/find', (req, res) => {
        // const location {latitude, loaction} = req.body;
        // if ()
const express = require('express');
const morgan = require('morgan');
const fs = require('fs'); //파일시스템 다루기 위한 모듈=> writeFile 함수 사용
const path = require('path');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const router = express.Router();

const mongoClient = require('mongodb').MongoClient;
const app = express();
app.set('port', process.env.PORT || 8000);
app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// mongoose configuration
const mongoose = require("mongoose")
mongoose.connect("mongodb://192.168.1.79:27017/testdb")

var main = require('./routes/main.js');
app.use('/', main);

var db;
var databaseUrl = "mongodb://192.168.1.79:27017";

app.get('/', (req, res) => {
    res.send("Web server Started~!!");
})

app.get('/gangnam', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, database) {
        if (err !=null) {
            res.json({ 'count': 0 })
        } else {
            db = database.db('testdb')
            db.collection('gangnam').find({}).toArray(function (err, result) {
                if (err) throw err
                console.log('result :')
                console.log(result)
                res.json(JSON.stringify(result))
            })
        }
    })
});

app.get('/seocho', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, database) {
        if (err !=null) {
            res.json({ 'count': 0 })
        } else {
            db = database.db('testdb')
            db.collection('seocho').find({}).toArray(function (err, result) {
                if (err) throw err
                console.log('result :')
                console.log(result)
                res.json(JSON.stringify(result))
            })
        }
    })
});

app.get('/songpa', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, database) {
        if (err !=null) {
            res.json({ 'count': 0 })
        } else {
            db = database.db('testdb')
            db.collection('songpa').find({}).toArray(function (err, result) {
                if (err) throw err
                console.log('result :')
                console.log(result)
                res.json(JSON.stringify(result))
            })
        }
    })
});

app.listen(app.get('port'), () => {
    console.log('8000 Port : Server Started...')
});
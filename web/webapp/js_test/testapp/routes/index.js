const express = require('express');
const router = express.Router();
const mysql = require('mysql');
const { route } = require('./signup');
require('dotenv').config();
const pass = process.env.KALI_PASS;

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'kali',
  password: pass,
  database: 'todo_app'
});

let todos = [];

/* GET home page. */
router.get('/', function(req, res, next) {
  connection.query(
    `SELECT * FROM tasks;`,
    (error, result) => {
      console.log(error);
      console.log(result);
      res.render('index', {
        title: 'ToDo App',
        todos: result,
      });
    }
  );
});

/* POST */
router.post('/', function(req, res, next) {
  connection.connect((err) => {
    if (err) {
      console.log('error connecting: ', err.stack);
      return
    }
    console.log('success');
  })
  const todo = req.body.add; // <= req.body.<inputのname>
  connection.query(
    `INSERT INTO tasks (user_id, content) VALUES (1, '${todo}');`,
    (error, result) => {
      console.log(error);
      res.redirect('/');
    }
  );
});

router.use('/signup', require('./signup'));

module.exports = router;

const express = require('express');
const { route } = require('.');
const router = express.Router();
const mysql = require('mysql');
require('dotenv').config();
const pass = process.env.KALI_PASS;

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'kali',
    password: pass,
    database: 'todo_app'
});

router.get('/', function(req, res, next) {
    res.render('signup', {
        title: 'Sign up',
    });
});

router.post('/', function(req, res, next) {
    const username = req.body.username;
    const password = req.body.password;
    const repassword = req.body.repassword;

    connection.query(
        `SELECT * FROM users WHERE name = '${username}';`,
        (error, result) => {
          if (error) throw error;
          console.log(result);
          if (result.length !== 0) {
              res.render("signup", {
                  title: "Signup",
                  errorMessage: ["このユーザー名は既に使われています"],
              });
          } else if (password == repassword) {
              connection.query(
                  `INSERT INTO users (name, password) VALUES ('${username}', '${password}');`,
                  (error, result) => {
                      if (error) throw error;
                      console.log(result);
                      res.redirect('/');
                  }
              );
          } else {
              res.render("signup", {
                  title: "Signup",
                  errorMessage: ["パスワードが一致しません"],
              });
          }
        }
    );
});

module.exports = router;
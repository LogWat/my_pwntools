import os

from flask import Flask, request, render_template, jsonify
import pymysql.cursors

app = Flask(__name__)

# MySQL接続
db = pymysql.connect(
    host = os.getenv('MYSQL_HOST'),
    port = os.getenv('MYSQL_PORT'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
cursor = db.cursor()

def db_init():
    # DB init
    cursor.execute('CREATE DATABASE IF NOT EXISTS DB')
    cursor.execute('USE DB')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT,
        name CHAR(100) NOT NULL,
        age INT NOT NULL,
        PRIMARY KEY (id)    
    )''')
    db.commit()
    
@app.route('/', methods=['GET'])
def index():
    # クエリ文字列nameから値を取得
    # 値が定義されていない場合はCTFをデフォに
    default_name = 'CTF'
    name = request.args.get('name', default_name)
    return render_template('index.html', name=name)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        cursor.execute('SELECT name, age FROM users')
        users = cursor.fetchall()
        
        return jsonify({
            'users': users
        })
    
    if request.method == 'POST':
        name = request.json['name']
        age = request.json['age']
        cursor.execute('INSERT INTO users (name, age) VALUES (%s %s)', (name, age))
        
        return jsonify({
            'result': 'success',
            'name': name
        })
        
if __name__ == '__main__':
    db_init()
    app.run(host='0.0.0.0', port=5000)
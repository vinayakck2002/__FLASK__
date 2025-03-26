from flask import Flask,render_template,request
import sqlite3
App = Flask(__name__)



con = sqlite3.connect('database.db')
con.execute('CREATE TABLE IF NOT EXISTS users(name TEXT,age int)')


@App.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name  = request.form['name']
        age = request.form['age']
        print(name,age)
        con = sqlite3.connect('database.db')
        con.execute('insert into users(name,age) values(?,?)',(name,age))
        # insert the value then values are in ?,? and variable
        con.commit()
        con.close()
    return render_template('index.html')
    
App.run()
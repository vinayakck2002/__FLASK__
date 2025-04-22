from flask import Flask,render_template,request,redirect
import mysql.connector

App = Flask(__name__)


con = mysql.connector.connect(
    host='localhost',
    user='vinayak',
    password='asd123.',
    database='vinayak'
)
con.autocommit=True
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,age int)")

@App.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name  = request.form['name']
        age = request.form['age']
        print(name,age)
        cur = con.cursor()

        cur.execute('insert into users(name,age) values(%s,%s)',(name,age))
        # insert the value then values are in ?,? and variable
        # cur.close()
    return render_template('index.html')
    
App.run()
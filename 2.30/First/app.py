from flask import Flask,render_template,request
App = Flask(__name__)

@App.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name  = request.form['name']
        age = request.form['age']
        print(name,age)

    return render_template('index.html')
    
App.run()
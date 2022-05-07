
from flask import Flask, redirect, render_template, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')
@app.route('/users')
def users():
    return render_template("index.html", all_users = User.get_all())

@app.route('/user/new')
def new():
    return render_template('new_user.html')

@app.route('/add/user', methods =['POST'])
def add_user():
    print( request.form)
    User.save(request.form)
    return redirect('/users')



if __name__=="__main__":     
    app.run(debug=True) 
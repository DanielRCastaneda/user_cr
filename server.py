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

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html", all_users =User.get_one(data))

@app.route('/user/delete/<int:id>')
def delete_all(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id' : id
    }
    return render_template('edit.html', all_users = User.get_one(data))

@app.route('/return/user', methods=['POST'])
def return_to_user():
    return redirect('/users')

@app.route('/user/update', methods=['POST'])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/users')
if __name__=="__main__":     
    app.run(debug=True) 
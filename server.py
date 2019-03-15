from flask import Flask, request, redirect, render_template, session
from loginform import LoginForm
from db import DB, UserModel

dbase = DB()
##nm = UserModel(dbase.get_connection())
##nm.init_table()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

 
@app.route('/')
@app.route('/index')
def index():
    if 'username' in session.keys():
        return session['username']
    return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', title='Авторизация', form=form)
    elif request.method == 'POST':
        form = LoginForm()
        user_name = form.username.data
        password = form.password.data
        print(user_name, password)
        user_model = UserModel(dbase.get_connection())
        exists = user_model.exists(user_name, password)
        if exists[0]:
            session['username'] = user_name
            session['user_id'] = exists[1]
        return redirect("/index")

    
##    if form.validate_on_submit():
##        return redirect('/success')
##    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

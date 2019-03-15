from flask import Flask, request, redirect, render_template, session
from loginform import LoginForm
from registerform import RegisterForm
from db import DB, UserModel

dbase = DB()
##nm = UserModel(dbase.get_connection())
##nm.init_table()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

 
@app.route('/')
@app.route('/drive')
def drive():
    if not('username' in session.keys()):
        return redirect("/login")
    return '''<head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            </head>
            <body>
                <nav class="navbar fixed-top navbar-light bg-light">
                      <span class="navbar-text"></span>
                        <span class="navbar-text"><a class="btn btn-primary" href="/login" role="button">Выйти</a>{}</span>
                </nav>
                
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
            </body>
'''.format(session['username'])
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', title='Авторизация', form=form, error='')
    elif request.method == 'POST':
        form = LoginForm()
        user_name = form.username.data
        password = form.password.data
        user_model = UserModel(dbase.get_connection())
        exists = user_model.exists(user_name, password)        
        if not exists[0]:
            return render_template('login.html', title='Авторизация', form=form, error='Неверное имя пользователя или пароль!')
        session['username'] = user_name
        session['user_id'] = exists[1]
        return redirect("/drive")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', title='Регистрация', form=form, error='')
    elif request.method == 'POST':
        form = RegisterForm()
        user_name = form.username.data
        password = form.password.data
        print(user_name, password)
        user_model = UserModel(dbase.get_connection())
        if not user_model.insert(user_name, password):
            return render_template('register.html', title='Регистрация', form=form, error='Данный пользователь уже существует!')
        if user_name == '':
            return render_template('register.html', title='Регистрация', form=form, error='Введите имя пользователя!')
        if password == '':
            return render_template('register.html', title='Регистрация', form=form, error='Введите пароль!')
        exists = user_model.exists(user_name, password)
        session['username'] = user_name
        session['user_id'] = exists[1]
        return redirect("/drive")
    
##    if form.validate_on_submit():
##        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

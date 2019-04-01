from flask import Flask, request, redirect, render_template, session, send_from_directory
from loginform import LoginForm
from registerform import RegisterForm
from db import DB, UserModel
from shutil import copy
import os

dbase = DB()
##nm = UserModel(dbase.get_connection())
##nm.init_table()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

 
@app.route('/')
def index():
    return redirect('/drive')


@app.route('/drive', methods=['GET', 'POST'])
def drive():
    if request.method == 'GET':
        if not('username' in session.keys()) or not('remember_me' in session.keys()):
            return redirect("/login")
        if not session['remember_me']:
            session['remember_me'] = None
        return '''<head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            </head>
            <body>
                <nav class="navbar fixed-top navbar-light bg-light">
                    
                    <span class="navbar-text"></span>
                      <ul class="nav">
                       <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">''' + session['username'] + '''</a>
                        <div class="dropdown-menu">
                          <a class="dropdown-item" href="/login">Выйти</a>
                        </div>
                      </li>
                    </ul>
                </nav>
                </br></br>
                <p>
                    <form method="POST" enctype="multipart/form-data">
                    
                    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#addfile">Добавить файл</button>
                    

                    <div class="modal fade" id="addfile" tabindex="-1" role="dialog" aria-labelledby="addfiletitle" aria-hidden="true">
                      <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                          <div class="modal-header">
                            <h5 class="modal-title" id="addfiletitle">Добавление файла</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>
                          <div class="modal-body">
                            <div class="form-group">
                                    <label for="file1">Приложите файл</label>
                                    <input type="file" class="form-control-file" id="file1" name="file">
                            <input class="form-control" type="text" name="foldername" placeholder="Название папки...">
                            </div>
                          </div>
                          <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Отмена</button>
                            <button type="submit" class="btn btn-primary">Добавить</button>
                          </div>
                        </div>
                      </div>
                    </div>
                    </form>




                    
                    <div class="row">
                      <div class="col-3">
                        <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical"> 
                          <a class="nav-link active" id="v-pills-nodir-tab" data-toggle="pill" href="#v-pills-nodir" role="tab" aria-controls="v-pills-nodir" aria-selected="true">.</a>
                          
                          ''' + ''.join(['<a class="nav-link" id="v-pills-{0}-tab" data-toggle="pill" href="#v-pills-{0}" role="tab" aria-controls="v-pills-{0}" aria-selected="false">{0}</a>'.format(folder) for folder in list(filter(lambda x: os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files')))]) + '''
                        </div>
                      </div>
                      
                      <div class="col-9">
                        <div class="tab-content" id="v-pills-tabContent">
                          <div class="tab-pane fade show active" id="v-pills-nodir" role="tabpanel" aria-labelledby="v-pills-nodir-tab">''' + ''.join(['''





                        <div class="dropdown">
                        <a class="nav-link dropdown-toggle" id="{0}" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">{0}</a>
                        <div class="dropdown-menu" aria-labelledby="{0}">
                          <a class="dropdown-item" href="/download/nodir/{0}">Скачать</a>
                          <a class="dropdown-item" href="/delete/nodir/{0}">Удалить</a>
                        </div>
                        </div>


                      '''.format(filename) for filename in list(filter(lambda x: not os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files')))]) + '</div>' + ''.join([('<div class="tab-pane fade" id="v-pills-{0}" role="tabpanel" aria-labelledby="v-pills-{0}-tab">'.format(folder) + ''.join([('''





                        <div class="dropdown">
                        <a class="nav-link dropdown-toggle" id=''' + filename + ''' data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">''' + filename + '''</a>
                        <div class="dropdown-menu" aria-labelledby= ''' + filename + '''>
                          <a class="dropdown-item" href="/download/''' + folder + '/' + filename + '''">Скачать</a>
                          <a class="dropdown-item" href="/delete/''' + folder + '/' +  filename + '''">Удалить</a>
                          
                        </div>
                      </div>



                      ''') for filename in list(filter(lambda x: not os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder + '\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder)))]) + '</div>') for folder in list(filter(lambda x: os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session + '\\files\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files')))]) + '''
                        </div>
                      </div>
                    </div>

                    
                    
                </p>
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
           </body>'''
    elif request.method == 'POST':
        f = request.files['file']
        if request.form['foldername'] != '' and not os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + request.form['foldername']):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + request.form['foldername'])
        f.save(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + request.form['foldername'] + '\\' + f.filename)
        if session['remember_me'] is None:
            session['remember_me'] = False
        return redirect('/drive')
            



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', title='Авторизация', form=form, error='')
    elif request.method == 'POST':
        form = LoginForm()
        user_name = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        user_model = UserModel(dbase.get_connection())
        exists = user_model.exists(user_name, password)
        if not exists[0]:
            return render_template('login.html', title='Авторизация', form=form, error='Неверное имя пользователя или пароль!')
        session['username'] = user_name
        session['user_id'] = exists[1]
        session['remember_me'] = remember_me
##        print(remember_me)
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
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + user_name)
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + user_name + '\\files')
        #      os.mkdir('static/' + user_name)
        return redirect("/drive")
    
##    if form.validate_on_submit():
##        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/delete/<folder>/<file>')
def delete(folder, file):
    if not 'username' in session.keys():
        return redirect('/login')
    if folder == 'nodir':
        if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + file):
            os.remove(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + file)
    else:
        if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder + '\\' + file):
            os.remove(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder + '\\' + file)
    if session['remember_me'] is None:
        session['remember_me'] = False
    return redirect('/drive')


@app.route('/download/<folder>/<file>')
def download(folder, file):
    if not 'username' in session.keys():
        return redirect('/login')
    if session['remember_me'] is None:
        session['remember_me'] = False
    if folder == 'nodir':
        if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + file):
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files', file, as_attachment=True)
    else:
        if os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder + '\\' + file):
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder, file, as_attachment=True)
##    return redirect('/drive')

    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

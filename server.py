from flask import Flask, request, redirect, render_template, session, send_from_directory
from loginform import LoginForm
from registerform import RegisterForm
from db import DB, UserModel
from shutil import copy
import os
from re import *



def get_address(address):
    pattern = compile('''(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)''')
    is_valid = pattern.match(address)
    if is_valid:
        return True
    else:
        return False



dbase = DB()
##nm = UserModel(dbase.get_connection())
##nm.init_table()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'

RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

@app.route('/')
def index():
    try:
        return redirect('/drive')
    except:
        redirect('/404')


@app.route('/drive', methods=['GET', 'POST'])
def drive():
    try:
        if request.method == 'GET':
            if not('username' in session.keys()) or not('remember_me' in session.keys()):
                return redirect("/login")
            if not session['remember_me']:
                session['remember_me'] = None
            return '''<head>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                    <style>
                        .litt{
                            margin-left: 15px;
                        }
                        
                        #footer {
                            position: fixed;
                            left: 0; 
                            bottom: 0;
                            color: #fff;
                            width: 100%;
                            height: 5%;
                       }
                       
                        #footer div {
                            padding: 10px;
                            background: rgba(52, 58, 64, 1); 
                       }
                       
                       .searcher{
                            margin-left: 30px;
                       }
                    </style>
                </head>
                <body class="bg-secondary">
                    <nav class="navbar fixed-top navbar-dark bg-dark">
                        <span>
                            <a href="http://127.0.0.1:8080/drive"><img src="static/img/LogoDarkUndStilished.png" width="130" height="50" alt="ERROR">
                            <input class="bg-dark searcher" type="text" placeholder="   Поиск">
                        </span>
                     
                        <span class="navbar-text"></span>
                          <ul class="nav">
                           <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false"><font color="white">''' + session['username'] + '''</font></a>
                            <div class="dropdown-menu bg-secondary">
                              <a class="dropdown-item bg-secondary text-white" href="/login">Выйти</a>
                            </div>
                          </li>
                        </ul>
                    </nav>
                    </br></br></br>
                    <p>
                        
                        <div class="row">
                        <form class="col-2 litt" method="POST" enctype="multipart/form-data">
                        
                        <button type="button" class="btn btn-primary bg-info" data-toggle="modal" data-target="#addfile">Добавить файл</button>
                        
    
                        <div class="modal fade" id="addfile" tabindex="-1" role="dialog" aria-labelledby="addfiletitle" aria-hidden="true">
                          <div class="modal-dialog modal-dialog-centered" role="document">
                            <div class="modal-content bg-dark">
                              <div class="modal-header">
                                <h5 class="modal-title text-white" id="addfiletitle">Добавление файла</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                  <span aria-hidden="true">&times;</span>
                                </button>
                              </div>
                              <div class="modal-body">
                                <div class="form-group text-white">
                                        <label for="file1">Приложите файл</label>
                                        <input type="file" class="form-control-file bg-dark" id="file1" name="file">
                                <input class="form-control bg-dark" type="text" name="foldername" placeholder="Название папки...">
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
    
    
    
    
                        
                          <div class="col-2">
                            <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical"> 
                              <a class="nav-link active text-white" id="v-pills-nodir-tab" data-toggle="pill" href="#v-pills-nodir" role="tab" aria-controls="v-pills-nodir" aria-selected="true">NoDir</a>
                              
                              ''' + ''.join(['<a class="nav-link text-white" id="v-pills-{0}-tab" data-toggle="pill" href="#v-pills-{0}" role="tab" aria-controls="v-pills-{0}" aria-selected="false">{0}</a>'.format(folder) for folder in list(filter(lambda x: os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files')))]) + '''
                            </div>
                          </div>
                          
                          <div class="col-5">
                            <div class="tab-content" id="v-pills-tabContent">
                              <div class="tab-pane fade show active text-white" id="v-pills-nodir" role="tabpanel" aria-labelledby="v-pills-nodir-tab">''' + ''.join(['''
    
    
    
    
    
                            <div class="dropdown">
                            <a class="nav-link dropdown-toggle text-white" id="{0}" role="button" aria-haspopup="true" aria-expanded="false"  data-toggle="dropdown"  href="#" >{0}</a>
                            <div class="dropdown-menu bg-secondary text-white" aria-labelledby="{0}">
                              <a class="dropdown-item bg-secondary text-white" href="/download/nodir/{0}">Скачать</a>
                              <a class="dropdown-item bg-secondary text-white" href="/delete/nodir/{0}">Удалить</a>
                            </div>
                            </div>
    
    
                          '''.format(filename) for filename in list(filter(lambda x: not os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files')))]) + '</div>' + ''.join([('<div class="tab-pane fade text-white" id="v-pills-{0}" role="tabpanel" aria-labelledby="v-pills-{0}-tab">'.format(folder) + ''.join([('''
    
    
    
    
    
                            <div class="dropdown">
                            <a class="nav-link dropdown-toggle text-white" id="''' + filename + '''" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">''' + filename + '''</a>
                            <div class="dropdown-menu bg-secondary text-white" aria-labelledby= ''' + filename + '''>
                              <a class="dropdown-item bg-secondary text-white" href="/download/''' + folder + '/' + filename + '''">Скачать</a>
                              <a class="dropdown-item bg-secondary text-white" href="/delete/''' + folder + '/' +  filename + '''">Удалить</a>
                              
                            </div>
                          </div>
    
    
    
                          ''') for filename in list(filter(lambda x: not os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder + '\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + folder)))]) + '</div>') for folder in list(filter(lambda x: os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + x), os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files')))]) + '''
                            </div>
                          </div>
                        </div>
    
                        
                        
                    </p>
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    <div id="footer">
                   <div>
                    &copy; Alex(GameTrue) & Артем(Zyrome64)
                   </div>
                  </div>
                </body>
               
                    '''
        elif request.method == 'POST':
            f = request.files['file']
            print(f.filename)
            if f.filename:
                if request.form['foldername'] != '' and not os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + request.form['foldername']):
                    os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + request.form['foldername'])
                f.save(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + '\\files\\' + request.form['foldername'] + '\\' + f.filename)
                if session['remember_me'] is None:
                    session['remember_me'] = False
                return redirect('/drive')
            else:
                redirect('/404')
    except:
        redirect('/404')
            



@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'GET':
            form = LoginForm()
            return render_template('login.html', title='Авторизация', form=form, error='')
        elif request.method == 'POST':
            form = LoginForm()
            user_name = form.username.data
            password = form.password.data
            remember_me = form.remember_me.data
            # Здесь надо сделать проверку на наличие символов в нике и пароле, чтобы они не были пустыми
            user_model = UserModel(dbase.get_connection())
            exists = user_model.exists(user_name, password)
            if not exists[0]:
                return render_template('login.html', title='Авторизация', form=form, error='Неверное имя пользователя или пароль!')
            session['username'] = user_name
            session['user_id'] = exists[1]
            session['remember_me'] = remember_me
            #print(remember_me)
            return redirect("/drive")
    except:
        redirect('/404')


@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'GET':
            form = RegisterForm()
            return render_template('register.html', title='Регистрация', form=form, error='')
        elif request.method == 'POST':
            print('Заходит в пост')
            form = RegisterForm()
            user_name = form.username.data
            password = form.password.data
            email = form.email.data
            name = form.name.data
            photo = form.photo.data
            print(user_name, password)
            user_model = UserModel(dbase.get_connection())
            if not user_model.insert(user_name, password):
                return render_template('register.html', title='Регистрация', form=form, error='Данный пользователь уже существует!')
            if user_name == '':
                return render_template('register.html', title='Регистрация', form=form, error='Введите имя пользователя!')
            if password == '':
                return render_template('register.html', title='Регистрация', form=form, error='Введите пароль!')
            if not(get_address(email)):
                return render_template('register.html', title='Регистрация', form=form, error='Неверный EMail!')
            exists = user_model.exists(user_name, password)
            session['username'] = user_name
            session['user_id'] = exists[1]
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + user_name)
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + user_name + '\\files')
            # photo.save(os.path.dirname(os.path.abspath(__file__)) + '\\static\\' + session['username'] + "\\avatar.png")
            #      os.mkdir('static/' + user_name)
            return redirect("/drive")

        return render_template('login.html', title='Авторизация', form=form)
    except:
        redirect('/404')
##    if form.validate_on_submit():
##        return redirect('/success')


@app.route('/delete/<folder>/<file>')
def delete(folder, file):
    try:
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
    except:
        redirect('/404')


@app.route('/download/<folder>/<file>')
def download(folder, file):
    try:
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
    except:
        redirect('/404')
##    return redirect('/drive')


@app.route('/404')
def not_found_error():
    return '''<head>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                    <style>
                        .litt{
                            margin-left: 15px;
                        }
                        #footer {
                            position: fixed;
                            left: 0; 
                            bottom: 0;
                            color: #fff;
                            width: 100%;
                            height: 5%;
                       }
                       #footer div {
                            padding: 10px;
                            background: rgba(52, 58, 64, 1); 
                       }
                       .bige{
                            font-size: 40px;
                            margin-left: 160px;
                            margin-top: 100px;
                       }
                    </style>
                </head>
                <body class="bg-secondary">
                    <nav class="navbar fixed-top navbar-dark bg-dark">
                        <span><a href="127.0.0.1:8080/drive"><img src="static/img/LogoDarkUndStilished.png" width="130" height="50" alt="ERROR"></span>
                        <span class="navbar-text"></span>
                          <ul class="nav">
                           <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false"><font color="white">''' + \
           session['username'] + '''</font></a>
                            <div class="dropdown-menu bg-secondary">
                              <a class="dropdown-item bg-secondary text-white" href="/login">Выйти</a>
                            </div>
                          </li>
                        </ul>
                    </nav>
                    </br></br></br>
                    <p>
                    <img width="15%" height="40%" class="bige" alt="ERROR" src="static/img/404Rob.png">
                    </p>
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    <div id="footer">
                   <div>
                    &copy; Alex(GameTrue) & Артем(Zyrome64)
                   </div>
                  </div>
                </body>

                    '''
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

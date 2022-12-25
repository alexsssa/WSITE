#pip install -r requirements.txt
import os
import sqlite3
from flask_login import LoginManager, login_user, login_required, logout_user
from flask import Flask, render_template, url_for, redirect, flash, request, g
from UserLogin import UserLogin
from FDataBase import FDataBase

DATABASE = 'users.db'
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'users.db')))
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(user_id, dbase)

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/', methods=["POST", "GET"])
def index():
    return login()


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = dbase.getUserBySurname(request.form['surname'])
        if user and (int(user['password']) == int(request.form['password'])):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for('menu_page'))
        flash("Ошибка доступа!", "error")

    return render_template("login_page.html", title="Авторизация")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/menu')
@login_required
def menu_page():
    return render_template('menu_page.html')


@app.route('/OT1-page')
@login_required
def OT1_page():
    return render_template('OT1-page.html')


@app.route('/OT4-page')
@login_required
def OT4_page():
    return render_template('OT4-page.html')


@app.route('/OT9-page')
@login_required
def OT9_page():
    return render_template('OT9-page.html')


@app.route('/OT12-page')
@login_required
def OT12_page():
    return render_template('OT12-page.html')


@app.route('/OT13-page')
@login_required
def OT13_page():
    return render_template('OT13-page.html')


@app.route('/OT15-page')
@login_required
def OT15_page():
    return render_template('OT15-page.html')


@app.route('/OT18-page')
@login_required
def OT18_page():
    return render_template('OT18-page.html')


@app.route('/OT22-page')
@login_required
def OT22_page():
    return render_template('OT22-page.html')


@app.route('/OT23-page')
@login_required
def OT23_page():
    return render_template('OT23-page.html')


@app.route('/OT40-page')
@login_required
def OT40_page():
    return render_template('OT40-page.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)

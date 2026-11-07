import sys
sys.path.insert(0,'db/')

from flask import Flask, request,redirect,url_for,flash,session,render_template
from dbhelper import *

app:any = Flask(__name__)
app.secret_key ='dc269212b6164b8b95e38c288a6cb351'

@app.after_request
def after_request(response)->None:
    response.headers['Cache-Control']="no-cache, no-store,must-revalidate"
    return response

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    print('LOGGED OUT')
    return redirect(url_for('index'))


@app.route('/main')
def main():
    email = session.get('email')
    if email != None:
        slist = getall('students')
        return render_template('main.html', students=slist)
    print('INVALID USER')
    return redirect(url_for('index'))


@app.route('/userlogin', methods=['POST'])
def userlogin():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    user = getrecord('users', email=email, password=password)
    session.clear()
    if len(user) > 0:
        print('LOGIN SUCCESS')
        session['email'] = email
        return redirect(url_for('main'))
    print('LOGIN FAILED')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
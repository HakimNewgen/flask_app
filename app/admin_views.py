from app import app
from flask import render_template, request, redirect


@app.route('/dash')
def dashboard():
    return render_template('admin/admin_top.html')

@app.route('/sign_up', methods= ['GET', 'POST'])
def sign_up():
    if request.methods == 'POST':
        req = requests.form
        username = req.email
        password - req.password
        print(username, password)

    else:
        render_template('/')



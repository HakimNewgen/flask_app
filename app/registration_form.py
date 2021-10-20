from app import app
from flask import render_template



@app.route('/form')
class RegistationForm():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def ValidateForm(self, user, password):
        if self.user == "":
            return false
        elif self.password == "":
            return false
        else:
            return True

def registration_form():
    return render_template('admin_template.html')

from app import app
from flask import render_template


@app.route('/dash')
def dashboard():
    return render_template('/admin/admin_template.html')


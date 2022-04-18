from flask import Blueprint, render_template, request, redirect
from database.db_session import create_session
from database.models import Admin
import logging

logger = logging.getLogger(__name__)

admin_login_blueprint = Blueprint(
    'admin_login',
    __name__,
    template_folder='templates'
)

admin_panel_blueprint = Blueprint(
    'admin_panel',
    __name__,
    template_folder='templates'
)


@admin_login_blueprint.route('/admin-login', methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        session = create_session()
        data = session.query(Admin).filter(Admin.username == request.form['username']).one()
        try:
            assert data.password == request.form['password']
        except AssertionError:
            return redirect('/admin-login')
        return redirect('/admin-panel')
    return render_template('admin_login.html')


@admin_panel_blueprint.route('/admin-panel', methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        session = create_session()
    return render_template('admin_panel.html')

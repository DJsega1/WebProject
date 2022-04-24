from flask import Blueprint, render_template, request, redirect
from database.db_session import create_session
from database.models import *
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
        data = session.query(Admin).filter(Admin.username == request.form['username']).all()
        try:
            assert data[0].password == request.form['password']
        except Exception:
            return redirect('/admin-login')
        return redirect('/admin-panel')
    return render_template('admin_login.html')


@admin_panel_blueprint.route('/admin-panel', methods=["GET", "POST"])
def admin_login():
    session = create_session()
    if request.method == 'POST':
        item = Item()
        item.article = request.form['article']
        item.name = request.form['name']
        item.description = request.form['description']
        item.amount = request.form['amount']
        item.color = request.form['color']
        item.type = request.form['type']
        item.material = request.form['material']
        item.sex = request.form['sex']
        session.add(item)
        session.commit()
        session.close()
        return redirect('/admin-panel')
    kwargs = {
        "material_list": [i.name for i in session.query(Material).all()],
        "color_list": [i.name for i in session.query(Color).all()],
        "type_list": [i.name for i in session.query(Type).all()],
        "sex_list": [i.name for i in session.query(Sex).all()]
    }
    session.close()
    return render_template('admin_panel.html', **kwargs)

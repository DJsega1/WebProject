from flask import Flask, render_template
from database import db_session
from blueprints import admin, index, men, women

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yald21'

if __name__ == '__main__':
    db_session.global_init("database/database.sqlite")
    app.register_blueprint(admin.admin_login_blueprint)
    app.register_blueprint(admin.admin_panel_blueprint)
    app.register_blueprint(index.index_blueprint)
    app.run(port=8080, host='localhost')

from flask import Flask, render_template
from database import db_session
from admin import admin_login_blueprint, admin_panel_blueprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    params = {
        "title": "Магазин одежды LOGO"
    }
    return render_template('index.html', **params)


if __name__ == '__main__':
    db_session.global_init("database/database.sqlite")
    app.register_blueprint(admin_login_blueprint)
    app.register_blueprint(admin_panel_blueprint)
    app.run(port=8080, host='localhost')

from flask import Flask, render_template
from database import db_session

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    params = {
        "title": "Магазин одежды LOGO"
    }
    return render_template('index.html', **params)


if __name__ == '__main__':
    db_session.global_init("database/database.sqlite")
    app.run(port=8080, host='localhost')

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    params = {
        "title": "Магазин одежды LOGO"
    }
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='localhost')

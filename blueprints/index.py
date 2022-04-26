from flask import Blueprint, render_template, request, redirect
from database.db_session import create_session
from sqlalchemy import desc
from database.models import *

index_blueprint = Blueprint(
    'index',
    __name__,
    template_folder='templates'
)


@index_blueprint.route('/', methods=["GET"])
def index():
    session = create_session()
    query = session.query(Item).filter(Item.amount > 0).order_by(desc(Item.sold)).limit(10)
    params = {
        "title": "Магазин одежды LOGO",
        "popular_items": query
    }
    session.close()
    return render_template('index.html', **params)

import os
from flask import Blueprint, render_template, request, redirect
from database.db_session import create_session
from database.models import *
import logging

logger = logging.getLogger(__name__)

men_blueprint = Blueprint(
    'men',
    __name__,
    template_folder='templates')


@men_blueprint.route('/men', methods=["GET"])
def index():
    session = create_session()
    query = session.query(Item).filter(Item.sex == 1).all()
    params = {
        "title": "Мужская одежда LOGO",
        "men_items": query
    }
    session.close()
    return render_template('men.html', **params)

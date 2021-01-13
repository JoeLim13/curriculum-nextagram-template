import peeweedbevolve # new; must be imported before models
from flask import Blueprint, render_template, flash, redirect, url_for, request
from models.user import User
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/', methods=['POST'])
@csrf.exempt
def create():
    user = User(username=request.form['username'],
                password=request.form['password'],
                email=request.form['email'])
    if user.save():
        flash("User has been succesfully added!")
        return redirect(url_for('users.new'))
    else:
        return render_template('users/new.html', username=request.form['username'], errors=user.errors)
    


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass

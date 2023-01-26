import lib
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

import controllers.User as contrUser

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_score = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(200), default="")

@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    return contrUser.CreateUser(data, User, db)
    
@app.route('/all-users')
def all_users():
    return contrUser.AllUsers(User)

@app.route('/ranking')
def showRanking():
    return contrUser.Ranking(10, User)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return contrUser.Login(data, User)

@app.route('/update-result', methods=['POST'])
def method_name():
    data = request.get_json()
    return contrUser.UpdateResult(data, User, db)
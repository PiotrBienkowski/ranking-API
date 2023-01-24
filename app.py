import lib
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_sore = db.Column(db.Integer, default=0)
    amount_of_floors = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(200), default="")
    score_hash = db.Column(db.String(200), default="")

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/sign_up')
def sign_up():
    return render_template('signUp.html')
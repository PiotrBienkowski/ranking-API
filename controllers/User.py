from flask import Flask, jsonify, request, render_template

import models.UserModel

def CreateUser(data, UserClass, db):
    name = data.get('name')
    password_hash = data.get('password_hash')
    return models.UserModel.createUser(name, password_hash, UserClass, db)

def AllUsers(UserClass):
    users_json = jsonify(models.UserModel.allUser(UserClass))
    return users_json

def Ranking(limit, UserClass):
    if limit < 0:
        limit = 0
    users_json = jsonify(models.UserModel.showRanking(limit, UserClass))
    return users_json

def Login(data, UserClass):
    name = data.get('name')
    password_hash = data.get('password_hash')
    return jsonify(models.UserModel.authUserByName(name, password_hash, UserClass))

def UpdateResult(data, UserClass, db):
    user_id = data.get("user_id")
    password_hash = data.get("password_hash")
    result = data.get("result")
    points = data.get("points")
    return jsonify(models.UserModel.updateResult(user_id, password_hash, result, points, UserClass, db))
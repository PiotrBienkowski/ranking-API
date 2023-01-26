from flask import Flask, jsonify, request, render_template

def createUser(name, password_hash, UserClass, db):
    new_user = UserClass(
        name = name,
        password_hash = password_hash
    )

    user = UserClass.query.filter_by(name=name).first()
    if user:
        return jsonify("error: 001")
    else:
        db.session.add(new_user)
        db.session.commit()
        return jsonify("user created")

def authUserByName(name, password_hash, UserClass):
    user = UserClass.query.filter_by(name=name).first()
    if user:
        if user.password_hash == password_hash:
            return user.id
        else:
            return False
    else:
        return False

def authUserById(user_id, password_hash, UserClass):
    user = UserClass.query.filter_by(id=user_id).first()
    if user:
        if user.password_hash == password_hash:
            return True
        else:
            return False
    else:
        return False

def allUser(UserClass):
    users = UserClass.query.all()
    tab = []
    for user in users:
        tab.append((user.id, user.name, user.password_hash))
    return tab

def showRanking(limit, UserClass):
    users = UserClass.query.order_by(UserClass.max_score.desc()).all()
    tab = []
    for user in users:
        tab.append((user.id, user.name, user.max_score, user.level))
    return tab[:limit]

def updateResult(user_id, password_hash, result, points, UserClass, db):
    if not authUserById(user_id, password_hash, UserClass):
        return False
    else:
        user = UserClass.query.filter_by(id=user_id).first()
        if int(result) > int(user.max_score):
            user.max_score = result
        user.level = user.level + int(points)
        db.session.commit()
        return True


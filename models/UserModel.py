from flask import Flask, jsonify, request, render_template
import lib

def createUser(name, password_hash, UserClass, db):
    new_user = UserClass(
        name = name,
        password_hash = password_hash
    )

    user = UserClass.query.filter_by(name=name).first()
    if user:
        return {
            "status": False, 
            "info": "User with that name already exists.",
            "timestamp": lib.get_timestamp()
        }
    else:
        db.session.add(new_user)
        db.session.commit()
        return {
            "status": True, 
            "info": "User created.",
            "timestamp": lib.get_timestamp()
        }

def authUserByName(name, password_hash, UserClass):
    user = UserClass.query.filter_by(name=name).first()
    if user:
        if user.password_hash == password_hash:
            return {
                "status": True, 
                "user_id": user.id,
                "timestamp": lib.get_timestamp()
            }
            
        else:
            return {"status": False, "timestamp": lib.get_timestamp()}
    else:
        return {"status": False, "timestamp": lib.get_timestamp()}

def authUserById(user_id, password_hash, UserClass):
    user = UserClass.query.filter_by(id=user_id).first()
    if user:
        if user.password_hash == password_hash:
            return {"status": True, "timestamp": lib.get_timestamp()}
        else:
            return {"status": False, "timestamp": lib.get_timestamp()}
    else:
        return {"status": False, "timestamp": lib.get_timestamp()}

def allUser(UserClass):
    users = UserClass.query.all()
    tab = []
    for user in users:
        tmp = {
            "user_id": user.id,
            "name": user.name,
            "password_hash": user.password_hash,
            "timestamp": lib.get_timestamp()
        }
        tab.append(tmp)
    return tab

def showRanking(limit, UserClass):
    users = UserClass.query.order_by(UserClass.max_score.desc()).all()
    tab = []
    for user in users:
        tmp = {
            "user_id": user.id,
            "name": user.name,
            "max_score": user.max_score,
            "level": user.level,
            "timestamp": lib.get_timestamp()
        }
        tab.append(tmp)
    return tab[:limit]

def updateResult(user_id, password_hash, result, points, UserClass, db):
    if not authUserById(user_id, password_hash, UserClass):
        return {"status": False, "timestamp": lib.get_timestamp()}
    else:
        user = UserClass.query.filter_by(id=user_id).first()
        if int(result) > int(user.max_score):
            user.max_score = result
        user.level = user.level + int(points)
        db.session.commit()
        return {"status": True, "timestamp": lib.get_timestamp()}
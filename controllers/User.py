from flask import Flask, jsonify, request, render_template

def CreateUser(data, UserClass, db):
    name = data.get('name')
    password_hash = data.get('password_hash')
    
    new_user = UserClass(
        name = name,
        password_hash = password_hash
    )

    user = UserClass.query.filter_by(name=name).first()

    if user:
        return jsonify("error 001")
    else:
        db.session.add(new_user)
        db.session.commit()

        return jsonify(data)

def all_users(UserClass):
    users = UserClass.query.all()
    tab = []
    for user in users:
        tab.append((user.name, user.password_hash))

    users_json = jsonify(tab)
    return users_json

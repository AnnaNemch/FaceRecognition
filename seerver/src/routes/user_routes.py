from app import app, bcrypt, jwt
from flask import request, json, jsonify, current_app
from src.services.database import session
from src.models.User import User, UserSchema
from flask_jwt_extended import create_access_token

@app.route('/api/user/login', methods=['POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    db_session = session()
    found_user = db_session.query(User).filter_by(email=email).first()
    db_session.close()

    if bcrypt.check_password_hash(found_user.password, password):
        access_token = create_access_token(identity={
            'first_name': found_user.first_name, 'last_name': found_user.last_name, 'email': found_user.email
        })
        result = jsonify({"token": access_token})
    else:
        # TODO :: add enum for statuses, send 401 status
        result = jsonify({"error": "Invalid username and password"})
    return result


@app.route('/api/user/register', methods=["POST"])
def register():

    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    # phone = request.get_json()['phone'] TODO :: uncomment
    password = bcrypt.generate_password_hash(
        request.get_json()['password']
    ).decode('utf-8')

    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                phone="phone",
                password=password
                )
    db_session = session()
    session.add(user)
    session.flush()
    session.commit()

    new_user = UserSchema().dump(user).data
    session.close()
    return jsonify({"result": new_user}), 201


@app.route('/api/guest', methods=["DELETE"])
def delete_user():
    return 'DELETE user'


@app.route('/api/guest-data')
def get_guest_data():
    return 'Guest Data'

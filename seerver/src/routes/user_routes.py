from app import app, bcrypt
from flask import request, json, jsonify, current_app
from src.services.database import session
from src.models.User import User, user_schema


@app.route('/api/auth')
def authorize():
    return 'Authorization'


@app.route('/api/user/register', methods=["POST"])
def register():

    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    phone = request.get_json()['phone']
    password = bcrypt.generate_password_hash(
        request.get_json()['password']
    ).decode('utf-8')

    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password
                )
    db_session = session()
    session.add(user)
    session.flush()
    session.commit()

    response = jsonify({'result': user_schema.jsonify(user)})
    response.status_code = 200 # or 400 or whatever
    return response


@app.route('/api/user', methods=["DELETE"])
def delete_user():
    return 'DELETE user'


@app.route('/api/guest-data')
def get_guest_data():
    return 'Guest Data'

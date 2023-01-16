from flask import Flask, request
import json
from userAuth import login, logout, user, signup, reset_password
app = Flask(__name__)


@app.route('/login', methods=['GET'])
def api_login():
    default_value = 'None'
    name = request.form.get('input_name', default_value)
    password = request.form.get('pass', 'None')
    response = login.login(name, password)
    return json.dumps({'response': response})


@app.route('/logout', methods=['GET'])
def api_logout():
    default_value = 'None'
    userID = request.form.get('userID', default_value)
    response = logout.logout(userID)
    return json.dumps({'response': response})


@app.route('/userAuth/user/isUsernameValid', methods=['GET'])
def api_checkUser():
    default_value = 'None'
    username = request.form.get('username', default_value)
    response = user.isUsernameValid(username)
    return json.dumps({'response': response})


@app.route('/userAuth/user/isLoggedIn', methods=['GET'])
def api_loggedin():
    default_value = 'None'
    userID = request.form.get('userID', default_value)
    userIP = request.form.get('userIP')
    response = user.isLoggedIn(userID, userIP)
    return json.dumps({'response': response})


@app.route('/userAuth/user/signup', methods=['GET'])
def api_signup():
    default_value = 'None'
    username = request.form.get('username', default_value)
    password = request.form.get('password')
    userIP = request.form.get('userIP')

    response = signup.signup(username, password, userIP)

    return json.dumps({'response': response})


@app.route('/userAuth/user/resetPassword', methods=['GET'])
def api_resetPassword():
    default_value = 'None'
    username = request.form.get('username', default_value)
    oldpassword = request.form.get('oldpassword', default_value)
    newpassword = request.form.get('newpassword')

    if not reset_password.checkUserID(username):
        return json.dumps({'response': 'USER_NOT_FOUND'})

    if not reset_password.checkPassword(username, oldpassword):
        return json.dumps({'response': 'WRONG_PASSWORD'})

    if reset_password.resetPassword(username, newpassword):
        return json.dumps({'response': 'SUCCESS'})

    return json.dumps({'response': False})


if __name__ == '__main__':
    app.run(debug=True)

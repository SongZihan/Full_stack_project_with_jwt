from flask import Flask, jsonify, render_template, request,abort
import json

from libs.auth import jwt_login, login_required

app = Flask(__name__)



@app.route('/',methods=["GET"])
def index_page():
    return render_template('index.html')


@app.route('/get_something',methods=["GET"])
def hello_world():
    """
    This is a test api.
    :return: Dict
    """
    msg = 'Hello Vue.js'
    data = 'This is data'
    return jsonify({"msg":msg,"data":data})

user = {
    "username": '123456',
    "password": '654321',
    "userData": "Hello World"
}

@app.route('/login',methods=["POST"])
def login():
    # 사용자 데이터 확인
    user_data = json.loads(request.data)
    print(user_data)
    # 사용자 신원 확인 후 클라이언트에 토큰 반환
    if user_data['username'] == user["username"] and user_data['password'] == user['password']:
        jwt_token = jwt_login(user_data['username'])
        return jsonify({"msg": "success login","jwt_token": jwt_token})
    else:
        # 거절
        abort(400)

@app.route('/test_login',methods=['GET'])
@login_required
def test_login():

    return jsonify({'msg':"You Are already login"})



if __name__ == "__main__":
    app.run(host="localhost")

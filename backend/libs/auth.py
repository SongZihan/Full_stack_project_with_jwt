from datetime import datetime, timedelta
from flask import abort

import jwt
from flask import request

from config.base_setting import SECRET_WORD


def jwt_login(username):
    """
    사용자 이름 데이터를받은 후 암호화 된 jwt 토큰을 반환합니다.
    :param username: 사용자 이름
    :return: jwt token
    """
    now = datetime.utcnow()
    # 2 시간 후에 만료됩니다.
    exp_datetime = now + timedelta(hours=2)
    # 조립 jwt
    encoded_jwt = jwt.encode({
        'username': username,
        # 만료 시간
        'exp': exp_datetime,
        # Is_valid는 유효 여부, false 인 경우 유효 기간 내에도 재 로그인으로 판단됩니다.
        'is_valid':True
    }, SECRET_WORD, algorithm='HS256')

    return encoded_jwt.decode("utf-8")


def login_required(func):
    def wrapper(*args, **kw):
        # 토큰 디코딩을 시도한다.디코딩되지 않으면 거부 명령이 반환된다.
        try:
            token = request.headers.get('Authorization', default=None).encode('utf-8')
            decode_token = jwt.decode(token,SECRET_WORD, algorithms=['HS256'])
        except Exception as err:
            return abort(400)
        else:
            # 비교를 위해 숫자 시간을 데이터 시간 유형으로 변환 https://blog.csdn.net/weixin_41789707/article/details/83009235
            jwt_time = datetime.fromtimestamp(decode_token['exp'])
            if jwt_time < datetime.utcnow():
                return abort(400)
            elif not decode_token['is_valid']:
                return abort(400)
            else:
                # msg는 데코 레이팅 된 함수가 반환하는 매개 변수이다.
                msg = func(*args, **kw)
                return msg

    return wrapper

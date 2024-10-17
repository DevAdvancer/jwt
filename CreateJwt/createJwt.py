import jwt
import datetime


def create_jwt(payload, secret, algorithm="HS256"):
	payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
	token = jwt.encode(payload, secret, algorithm=algorithm)
	return token if isinstance(token, str) else token.decode('utf-8')

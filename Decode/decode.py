import jwt


def decode_jwt(token, secret, algorithm="HS256"):
	try:
		decoded_payload = jwt.decode(token, secret, algorithms=[algorithm])
		return decoded_payload
	except jwt.ExpiredSignatureError:
		return "Token has expired"
	except jwt.InvalidTokenError:
		return "Invalid token"

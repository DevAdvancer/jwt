import jwt


def verify_jwt(token, secret, algorithm="HS256"):
	try:
		decoded_payload = jwt.decode(token, secret, algorithms=[algorithm])
		return {
			"valid": True,
			"payload": decoded_payload
		}
	except jwt.ExpiredSignatureError:
		return {
			"valid": False,
			"error": "Token has expired"
		}
	except jwt.InvalidTokenError:
		return {
			"valid": False,
			"error": "Invalid token"
		}

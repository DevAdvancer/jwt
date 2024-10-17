from CreateJwt import create_jwt
from Decode import decode_jwt
from Verify import verify_jwt


def main():
	secret_key = "your_secret_key"

	print("Choose an option:")
	print("1: Encode a new JWT")
	print("2: Decode an existing JWT")
	print("3: Verify an existing JWT")

	choice = input("Enter your choice (1, 2, or 3): ")

	if choice == "1":
		user_id = input("Enter user_id: ")
		username = input("Enter username: ")

		payload = {
			"user_id": user_id,
			"username": username
		}

		token = create_jwt(payload, secret_key)
		print(f"Encoded JWT: {token}")

	elif choice == "2":
		token = input("Enter the JWT to Decode: ")
		decoded_data = decode_jwt(token, secret_key)
		print(f"Decoded Payload: {decoded_data}")

	elif choice == "3":
		token = input("Enter the JWT to verify: ")
		verification_result = verify_jwt(token, secret_key)
		if verification_result["valid"]:
			print(f"Valid JWT. Payload: {verification_result['payload']}")
		else:
			print(f"JWT Verification Failed: {verification_result['error']}")

	else:
		print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
	main()

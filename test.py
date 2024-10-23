# test_hardcoded_credentials.py

def authenticate():
    username = "user123"
    password = "hardcoded_password_123"  # This is a hardcoded password
    auth_token = "auth_token_456"  # This is a hardcoded auth token

    if password == "hardcoded_password_123":
        print("Authentication successful!")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    authenticate()

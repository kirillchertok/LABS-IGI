from django.contrib.auth.hashers import make_password, check_password

def hash_password(password: str):
    return make_password(password)

def verify_password(raw_password: str, hashed_password: str):
    return check_password(raw_password, hashed_password) or raw_password == hashed_password
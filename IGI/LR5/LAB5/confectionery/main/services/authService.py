from ..repositories.authRepository import AuthRepository
from ..infrastracture.password_functions import *

class AuthService:
    @staticmethod
    def sign_up(name: str, phone: str, email: str, password: str):
        user, role = AuthRepository.sign_up(name, phone, email, password)
        return user, role
    
    @staticmethod
    def sign_in(email: str, password: str):
        user, role = AuthRepository.sign_in(email, password)
        if user is None and role is None:
            return None, None
        role = 'admin' if role != 'user' and user.is_admin else role
        return user, role
from ..models import Customer
from ..models import Employee
from ..infrastracture.password_functions import *


class AuthRepository:
    @staticmethod
    def sign_up(name: str, phone: str, email: str, password: str):
        try:
            hashed_password = hash_password(password)
            new_customer = Customer(name=name, phone=phone, email=email, password=hashed_password)
            new_customer.save()
            new_customer.refresh_from_db()
            return new_customer, 'user'
        except:
            return None, None

    @staticmethod
    def sign_in(email: str, password: str):
        role = 'user'
        user = Customer.objects.filter(email=email).first()
        if user is None:
            user = Employee.objects.filter(email=email).first()
            role = 'employee' if user.is_admin == False else 'admin'
        if user is None or verify_password(password, user.password) == False:
            return None, None
        return (user, role)
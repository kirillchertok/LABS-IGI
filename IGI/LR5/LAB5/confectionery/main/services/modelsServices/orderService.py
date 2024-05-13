from ...repositories.orderRepository import OrderRepository
from datetime import datetime

class OrderService:
    @staticmethod
    def get_all_orders():
        return OrderRepository.get_all()
    
    @staticmethod
    def get_all_users_orders(user):
        return OrderRepository.get_users(user)

    @staticmethod
    def get_one_order_by_id(id: int):
        return OrderRepository.get_one_by_id(id)
    
    @staticmethod
    def create_order(email: str, products: list[str], date: datetime, adress: str, discount_code: str):
        return OrderRepository.create(email, products, date, adress, discount_code)
    
    @staticmethod
    def update_order(id: int, products: list[str], date: datetime, adress: str, discount_code: str):
        return OrderRepository.update(id, products, date, adress, discount_code)
    
    @staticmethod
    def cancel_order(id: int):
        return OrderRepository.delete(id)
from ...repositories.productRepository import ProductRepository
from datetime import datetime

class ProductService:
    @staticmethod
    def get_all_products():
        return ProductRepository.get_all()
    
    @staticmethod
    def get_one_product_by_id(id: int):
        return ProductRepository.get_one_by_id(id)
    
    @staticmethod
    def get_all_py_param(param: str):
        return ProductRepository.get_all_by_param(param)
    
    @staticmethod
    def get_all_products_by_type(type: str):
        return ProductRepository.get_all_by_type(type)
    
    @staticmethod
    def create_product(name: str, price: float, description: str, amount: int, type: str):
        return ProductRepository.create(name, price, description, amount, type)
    
    @staticmethod
    def update_product(id: int , name: str, price: int, description: str, amount: int, type: str):
        return ProductRepository.update(id, name, price, description, amount, type)
    
    @staticmethod
    def delete_product(id: int):
        return ProductRepository.delete(id)
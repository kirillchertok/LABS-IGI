from ...repositories.discountRepository import DiscountRepository

class DiscountService:
    @staticmethod
    def get_all_discounts():
        return DiscountRepository.get_all()
    
    @staticmethod
    def get_one_discount_by_id(id: int):
        return DiscountRepository.get_one_by_id(id)
    
    @staticmethod
    def get_all_discounts_by_param(param: str):
        return DiscountRepository.get_all_by_param(param)
    
    @staticmethod
    def add_discount(code: str, amount_of_money: int):
        return DiscountRepository.create(code, amount_of_money)
    
    @staticmethod
    def update_discount_inf(code: str, amount_of_money: int):
        return DiscountRepository.update_all(code, amount_of_money)
    
    @staticmethod
    def change_discount_status(id: int):
        return DiscountRepository.update_status(id)
    
    @staticmethod
    def delete_one_discount_by_id(id: int):
        return DiscountRepository.delete(id)
    
    @staticmethod
    def check_discount_code(code: str):
        return DiscountRepository.check(code)
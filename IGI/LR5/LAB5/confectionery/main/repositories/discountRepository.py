from ..models import Discount

class DiscountRepository:
    @staticmethod
    def get_all():
        try:
            return Discount.objects.all()
        except:
            return None
        
    @staticmethod
    def get_one_by_id(id: int):
        return Discount.objects.filter(id=id).first()    
        
    @staticmethod
    def get_all_by_param(param: str):
        try:
            return Discount.objects.order_by(f'-{param}')
        except:
            return None

    @staticmethod
    def check(code: str):
        try:
            discount = Discount.objects.filter(code=code).first()
            if discount is None:
                return False
            else:
                return True
        except:
            return None    

    @staticmethod
    def create(code: str, amount_of_money: int) :
        try:
            try:
                discount = Discount(code=code, amount=amount_of_money, is_active=True)
            except Exception as e:
                print(f"Тип исключения: {type(e).__name__}, сообщение: {str(e)}")
            discount.save()
            return discount
        except:
            return None
        
    @staticmethod
    def update_all(code: str, amount_of_money: int):    
        try:
            discount = DiscountRepository.get_one_by_id(id)
            discount.code=code
            discount.amount=amount_of_money
            discount.save()
            return discount
        except:
            return None

    @staticmethod
    def update_status(id: int):    
        try:
            discount = DiscountRepository.get_one_by_id(id)
            discount.is_active=False if discount.is_active else True
            discount.save()
            return discount
        except:
            return None       
         
    @staticmethod
    def delete(id: int) :
        try:
            discount = DiscountRepository.get_one_by_id(id)
            if discount is None:
                return None
            discount.delete()
        except:
            return None              
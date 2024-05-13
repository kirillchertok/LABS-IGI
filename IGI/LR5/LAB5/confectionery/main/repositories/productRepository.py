from ..models import Product,ProductType

class ProductRepository: 
    @staticmethod
    def get_all():
        try:
            return Product.objects.all()
        except:
            return None
        
    @staticmethod
    def get_one_by_id(id: int):
        return Product.objects.filter(id=id).first()    
        
    @staticmethod
    def get_all_by_param(param: str):
        try:
            return Product.objects.order_by(f'-{param}')
        except:
            return None   

    @staticmethod
    def get_all_by_type(type: str):
        try:
            product_type = ProductType.objects.filter(type=type).first()
            return Product.objects.filter(type=product_type)
        except:
            return None 

    @staticmethod
    def create(name: str, price: float, description: str, amount: int, type: str) :
        try:
            product_type = ProductType.objects.filter(type=type).first()
            if product_type is None:
                return None
            try:
                product = Product(name=name, price=price, description=description, amount=amount, type=product_type, buyed=0)
            except Exception as e:
                print(f"Тип исключения: {type(e).__name__}, сообщение: {str(e)}")
            product.save()
            return product
        except:
            return None
        
    @staticmethod
    def update(id: int , name: str, price: int, description: str, amount: int, type: str):    
        try:
            product = ProductRepository.get_one_by_id(id)
            product.name = name
            product.price = price
            product.description = description
            product.amount = amount
            product.type = ProductType.objects.filter(type=type).first()
            product.save()
            return product
        except:
            return None    
    @staticmethod
    def delete(id: int) :
        try:
            product = ProductRepository.get_one_by_id(id)
            if product is None:
                return None
            product.delete()
            return product
        except:
            return None          
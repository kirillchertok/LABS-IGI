from ..models import ProductType

class ProductTypeRepository:
    @staticmethod
    def get_all():
        try:
            return ProductType.objects.all()
        except:
            return None
        
    @staticmethod
    def get_one_by_id(id: int):
        try:
            return ProductType.objects.filter(id=id).first()
        except:
            return None
        
    @staticmethod
    def get_all_by_param(param: str):
        try:
            return ProductType.objects.order_by(f'-{param}')
        except:
            return None 
        
    @staticmethod
    def create(new_type: str):
        try:
            type = ProductType(type=new_type)
            type.save()
            return type
        except:
            return None
        
    @staticmethod
    def update(id: int, new_type: str):
        try:
            type = ProductTypeRepository.get_one_by_id(id)
            type.type = new_type
            type.save()
            return type
        except:
            return None
        
    @staticmethod
    def delete(id: int):
        try:
            type = ProductTypeRepository.get_one_by_id(id)
            if type == None:
                return None
            type.delete()
        except:
            return None
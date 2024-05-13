from ...repositories.productTypeRepository import *

class ProductTypeService:
    @staticmethod
    def get_all_types():
        return ProductTypeRepository.get_all()
    
    @staticmethod
    def get_all_types_by_param(param: str):
        return ProductTypeRepository.get_all_by_param(param)
    
    @staticmethod
    def get_one_type_by_id(id: int):
        return ProductTypeRepository.get_one_by_id(id)
    
    @staticmethod
    def update_type(id: int, new_type: str):
        return ProductTypeRepository.update(id, new_type)
    
    @staticmethod
    def create_type(type: str):
        return ProductTypeRepository.create(type)
    
    @staticmethod
    def delete_type(id: int):
        return ProductTypeRepository.delete(id)
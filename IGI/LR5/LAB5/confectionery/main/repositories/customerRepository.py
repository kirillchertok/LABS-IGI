from ..models import Customer

class CustomerRepository:
    @staticmethod
    def get_all():
        try:
            return Customer.objects.all()
        except:
            return None
        
    @staticmethod
    def get_one_by_id(id: int):
        return Customer.objects.filter(id=id).first()

    @staticmethod
    def get_one_by_email(email: str):
        return Customer.objects.filter(email=email).first()     
        
    @staticmethod
    def get_all_by_param(param: str):
        try:
            return Customer.objects.order_by(f'-{param}')
        except:
            return None    
        
    @staticmethod
    def update(email: str, name: str, phone: str, new_email: str, password: str):    
        try:
            customer = CustomerRepository.get_one_by_email(email)
            customer.name=name
            customer.email=new_email
            customer.phone=phone
            customer.password=password
            customer.save()
            return customer
        except:
            return None

    @staticmethod
    def change_password(id:int, password: str):    
        try:
            customer = CustomerRepository.get_one_by_id(id)
            customer.password=password
            customer.save()
            return customer
        except:
            return None        
         
    @staticmethod
    def delete(id: int):
        try:
            customer = CustomerRepository.get_one_by_id(id)
            if customer is None:
                return None
            customer.delete()
            return customer
        except:
            return None
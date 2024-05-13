from ...repositories.customerRepository import CustomerRepository

class CustomerService:
    @staticmethod
    def get_all_users():
        return CustomerRepository.get_all()
    
    @staticmethod
    def get_one_user_by_id(id: int):
        return CustomerRepository.get_one_by_id(id)
    
    @staticmethod
    def get_all_users_by_param(param: str):
        return CustomerRepository.get_all_by_param(param)
    
    @staticmethod
    def get_one_user_by_email(email: str):
        return CustomerRepository.get_one_by_email(email)
    
    @staticmethod
    def update_user_inf(email: str, name: str, phone: str, new_email: str, password: str):
        return CustomerRepository.update(email ,name, phone, new_email, password)
    
    @staticmethod
    def change_user_password(id: int, new_password: str):
        return CustomerRepository.change_password(id, new_password)
    
    @staticmethod
    def delete_one_user_by_id(id: int):
        return CustomerRepository.delete(id)
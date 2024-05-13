from ..models import Employee

class EmployeeRepository:
    @staticmethod
    def get_all():
        try:
            return Employee.objects.all()
        except:
            return None
        
    @staticmethod
    def get_one_by_id(id: int):
        return Employee.objects.filter(id=id).first()

    @staticmethod
    def get_one_by_email(email: str):
        return Employee.objects.filter(email=email).first()     
        
    @staticmethod
    def get_all_by_param(param: str):
        try:
            return Employee.objects.order_by(f'-{param}')
        except:
            return None    
        
    @staticmethod
    def update(email: str, name: str, phone: str, new_email: str, password: str):    
        try:
            employee = EmployeeRepository.get_one_by_email(email)
            employee.name=name
            employee.email=new_email
            employee.phone=phone
            employee.password=password
            employee.save()
            return employee
        except:
            return None   
         
    @staticmethod
    def delete(id: int):
        try:
            employee = EmployeeRepository.get_one_by_id(id)
            if employee is None:
                return None
            employee.delete()
            return employee
        except:
            return None   
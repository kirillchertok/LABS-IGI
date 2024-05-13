from ...repositories.employeeRepository import EmployeeRepository

class EmployeeService:
    @staticmethod
    def get_all_employees():
        return EmployeeRepository.get_all()
    
    @staticmethod
    def get_one_employee_by_id(id: int):
        return EmployeeRepository.get_one_by_id(id)
    
    @staticmethod
    def get_one_employee_by_email(email: str):
        return EmployeeRepository.get_one_by_email(email)
    
    @staticmethod
    def get_all_employees_by_param(param: str):
        return EmployeeRepository.get_all_by_param(param)
    
    @staticmethod
    def update_employee_inf(email: str, name: str, phone: str, new_email: str, password: str):
        return EmployeeRepository.update(email, name, phone, new_email, password)
    
    @staticmethod
    def delete_one_employee_by_id(id: int):
        return EmployeeRepository.delete(id)
from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employees(self, new_employee):
        self.employees.append(new_employee)

        

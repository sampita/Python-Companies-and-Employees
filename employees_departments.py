# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
class Employee:
    def __init__(self, name, job_title, start_date):
        self.employee_name = name
        self.job_title = job_title
        self.start_date = start_date

# Create a Company type that employees can work for. A company should have a business name, address, and industry type.
class Company:
    def __init__(self, name, address, industry):
        self.business_name = name
        self.address = address,
        self.industry = industry
        self.employees = list()
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        
    def employees_report(self, business_name, industry, employees):
        print(f'{self.business_name} is in the {self.industry} industry and has the following employees:')
        for employee in self.employees:
            print(employee.employee_name)
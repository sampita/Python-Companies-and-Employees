from employees_departments import Employee, Company

# Using the classes from employees_departments.py, create two companies, and 5 people who want to work for them.
company_one = Company("Bill's Pet Rocks", "24 8th Ave S", "Pets")
company_two = Company("Willie's Wet Willies", "4228 Wedgewood Ave", "Joke Shop")

employee_one = Employee("Joe Shep", "Rock Wrangler", "1/15/2020")
employee_two = Employee("Jisie David", "CEO", "6/1/2018")
employee_three = Employee("Rose Wisoztky", "Store Manager", "8/29/2019")
employee_four = Employee("Santa Claus", "Toy Builder", "1/01/2020")
employee_five = Employee("Keith Richards", "Custodian", "12/01/2019")

# print(company_one.business_name)

# Assign 2 people to be employees of the first company.

company_one.employees.append(employee_one)
company_one.employees.append(employee_three)

# for employee in company_one.employees:
# print(company_one.employees)

# Assign 3 people to be employees of the second company.
company_two.employees.append(employee_two)
company_two.employees.append(employee_four)
company_two.employees.append(employee_five)

# for employee in company_two.employees:
#     print(employee.employee_name)

# Output a report to the terminal the displays a business name, and its employees.

company_one.employees_report(company_one.business_name, company_one.industry, company_one.employees)

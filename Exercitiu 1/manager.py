from employee import Employee

class Manager(Employee):

    mgr_count = 0
    
    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.department = "433C_" + department
        self.tasks = tasks
        Manager.mgr_count += 1

    def display_employee(self):
        print("Department : ", self.department)

    # Functii de testare
    def is_tech_department(self):
        tech_dept = ['IT', 'Web Dev', 'Cybersecurity', 'Software Dev', 'Data Analytics']
        return any(dep in self.department for dep in tech_dept)

    def is_paid_more_than(self, other_employee):
        if not isinstance(other_employee, Employee):
            return False
        return self.salary > other_employee.salary
        
    def get_annual_salary(self):
        return self.salary * 12
        




man1 = Manager('Alex', 8000, 'Do nothing', 'IT')
emp1 = Employee('Mihai', 3000)

man1.display_employee()
emp1.display_employee()

print(f"Employee count accessed from Employee class: {emp1.empCount}")
print(f"Employee count accessed from Manager class: {man1.empCount}")
print(f"Manager count: {man1.mgr_count}")

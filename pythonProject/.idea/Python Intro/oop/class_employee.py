class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.new_salary = 0

    def raise_amount(self, amount):
        self.new_salary = self.salary + (self.salary * amount / 100)

    def display_information(self):
        # print("Name:", self.name)
        # print("position:",self.position)
        # print("Salary:",self.salary)
        # print("After Raise:", self.new_salary)
        print(f"Name : {self.name}, Position : {self.position}, Salary : {self.salary}, New Salary : {self.new_salary}")


emp = Employee("Sristy", "Intern", 10000)
emp.raise_amount(10)
emp.display_information()
emp_1 = Employee("Ashikur", "dgdg", 2000)
emp_1.raise_amount(300)
emp_1.display_information()

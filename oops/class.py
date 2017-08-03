# Python Object Oriented Programming

import datetime

class employee:

  num_of_emp = 0 # This is a class variable, this is mentioned outside any function
  raise_amount = 1.04 # This is another class variable

  # Initialize the class
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@outlook.com'
    employee.num_of_emp += 1


  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)


  @classmethod # class method in Python.
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    else:
      return True





emp1 = employee('Ankit', 'Bhatia', 50000) # emp1 is an instance
emp2 = employee('Aayush', 'Aggarwal', 90000000) # This is another instance

print employee.set_raise_amount(1.5)

print emp1.email
print emp2.pay
print emp2.email
print emp2.fullname() # 'fullname()' is a method
print emp1.fullname() # Here we call the method on the instance i.e. emp1, thats why we don't need to pass any argument
print employee.fullname(emp2) # When we call the method on the class i.e employee, we have to pass in the argument i.e. emp1 or emp2

print employee.num_of_emp

print employee.raise_amount
print emp1.pay
print emp2.raise_amount

# Calling static method 'is_workday(day)' defined above
my_date = datetime.date(2015,12,28)
print employee.is_workday(my_date)


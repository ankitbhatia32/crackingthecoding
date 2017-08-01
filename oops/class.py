# Python Object Oriented Programming

class employee:
  # Initialize the class
  def __init__(self, first, last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@outlook.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)


emp1 = employee('Ankit', 'Bhatia', 50000)
emp2 = employee('Aayush', 'Aggarwal', 90000000)

print emp1.email
print emp2.pay
print emp2.email
print emp2.fullname()
print emp1.fullname() # Here we have call the method on the instance i.e. emp1, thats why we don't need to pass any argument
print employee.fullname(emp2) # When we call the method on the class i.e employee, we have to pass in the argument i.e. emp1 or emp2


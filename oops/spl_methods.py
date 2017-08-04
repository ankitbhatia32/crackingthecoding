# Special methods in Python


class Employee:

  raise_amt = 1.04

  def __init__(self, first, last, pay): # __init__ is also a kind of Dunder method
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@company.com'
    self.pay = pay

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)

  # Dunder/Magic methods used in Python. There are many Dunder methods that can be used in Python
  def __repr__(self):
    return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

  def __str__(self):
    return '{} - {}'.format(self.fullname(), self.email)

  def __add__(self, other):
    return self.pay + other.pay

  def __len__(self):
    return len(self.fullname())


emp_1 = Employee('Ankit', 'Bhatia', 50000)
emp_2 = Employee('Aayush', 'Aggarwal', 60000)


print str(emp_1)
print repr(emp_2)
print(emp_1 + emp_2)
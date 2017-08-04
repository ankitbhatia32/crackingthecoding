# Inheritance example in Python

class Employee:

  raise_amt = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@company.com'
    self.pay = pay

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)


# New class inherited from 'Employee class' above
class developer(Employee):

  raise_amt = 1.10

  def __init__(self, first, last, pay, prog_lang):
    Employee.__init__(self, first, last, pay) # Inheriting 'first, name, pay' from the 'Employee' class above
    # In Python 3 inheriting above like line we should use: super().__init__(first, last, pay). It's not valid in Python 2
    self.prog_lang = prog_lang


# Another class inherited from 'Employee class'
class manager(Employee):

  def __init__(self, first, last, pay, employees = None):
    Employee.__init__(self, first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)

  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_emps(self):
    for emp in self.employees:
      print '-->' + emp.fullname()


dev_1 = developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = developer('Parteek', 'Singh', 60000, 'Java')
ev_2 = developer('Aayush', 'Aggarwal', 60000, 'Angular')

mng_1 = manager('Shashank', 'Garg', 80000, [dev_1])

print mng_1.email

mng_1.add_emp(dev_2) # We can new employees for a manager
mng_1.remove_emp(dev_1) # We can remove employee for a manager i.e. mng_1

mng_1.print_emps()

# This is a built function in Python telling if 'mng_1' is an instance of 'developer' class. O/P here is False
print isinstance(mng_1, developer)
# This is also a built in function in Python telling if 'developer' is a subclass of 'Employee' class. O/P will be True
print issubclass(developer,Employee)


# print(dev_1.email)
# print(dev_1.prog_lang)









# print(dev_1.raise_amt)
# dev_1.apply_raise()
# print(dev_1.raise_amt)
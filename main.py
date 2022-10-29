# # Creating Class means creating template so that we can reuse them with objects.
# class Employee:
#     # The constructor is a method that is called when an object is created. This method is defined in the class and can be used to initialize basic variables. If you create four objects, the class constructor is called four times.
#     def __init__(self, fname, lname, salary):
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary


# manish = Employee("manish", "bhusal", 23000)
# milan = Employee("milan", "bhusaal", 50000)

# # print(manish.fname)
# # print(milan.salary)

# # print(manish.salary)
# # manish.salary = 30000
# # print(manish.salary)
# # print(manish.__dict__)

from main1 import Atm

manish = Atm()
manish.menu()
manish.create_pin()
manish.deposit_money()
manish.check_balance()
manish.withdraw_money()
manish.check_balance()

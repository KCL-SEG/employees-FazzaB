"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, monthlySalary, hoursWorked, hourWage, commission, bonus, numContractsLanded, comissionPerContract):
        self.name = name
        self.contract_type = contract_type
        self.monthlySalary = monthlySalary
        self.hoursWorked = hoursWorked
        self.hourWage = hourWage
        self.commission = commission
        self.bonus = bonus
        self.numContractsLanded = numContractsLanded
        self.comissionPerContract = comissionPerContract

    def get_pay(self):
        pay = 0
        if self.contract_type == "salary":
            if self.commission == "bonus":
                pay = self.monthlySalary + self.bonus
            elif self.commission == "contract":
                pay = self.monthlySalary + (self.numContractsLanded * self.comissionPerContract)
            else:
                pay = self.monthlySalary
        else:
            if self.commission == "bonus":
                pay = (self.hoursWorked * self.hourWage) + self.bonus
            elif self.commission == "contract":
                pay = (self.hoursWorked * self.hourWage) +  (self.numContractsLanded * self.comissionPerContract)
            else:
                pay = (self.hoursWorked * self.hourWage)
        return pay
    def __str__(self):
        pay = self.get_pay()
        summary=""
        if self.contract_type == "salary":
            if self.commission == "bonus":
                summary = self.name + " works on a monthly salary of " + str(self.monthlySalary) + " and receives a bonus commission of " + str(self.bonus) +"."
            elif self.commission == "contract":
                summary = self.name + " works on a monthly salary of " + str(self.monthlySalary) + " and receives a commission for " + str(self.numContractsLanded) + " contract(s) at " + str(self.comissionPerContract) + "/contract."
            else:
                summary = self.name + " works on a monthly salary of " + str(self.monthlySalary) + "."
        else:
            if self.commission == "bonus":
                summary = self.name + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.hourWage) + "/hour and receives a bonus commission of " + str(self.bonus) +"."
            elif self.commission == "contract":
                summary = self.name + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.hourWage) + "/hour" + " and receives a commission for " + str(self.numContractsLanded) + " contract(s) at " + str(self.comissionPerContract) + "/contract."
            else:
                summary = self.name + " works on a contract of " + str(self.hoursWorked) + " hours at " + str(self.hourWage) + "/hour."
        return (summary + " Their total pay is " + str(pay) +".")

#name, contract_type, monthlySalary, hoursWorked, hourWage, commission, bonus, numContractsLanded, comissionPerContract
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','salary',4000,0,0,'0',0,0,0)
string = str(billie)
print(string)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','hourly',0,100,25,'0',0,0,0)
string = str(charlie)
print(string)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','salary',3000,0,0,'contract',0,4,200)
string = str(renee)
print(string)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly',0,150,25,'contract',0,3,220)
string = str(jan)
print(string)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','salary',2000,0,0,'bonus',1500,0,0)
string = str(robbie)
print(string)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly',0,120,30,'bonus',600,0,0)
string = str(ariel)
print(string)

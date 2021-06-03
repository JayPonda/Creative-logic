import datetime


class User:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_user_details(self):
        return {'name': self.name, 'age' : self.age, 'gender': self.gender}



class Bank(User):
    
    def __init__(self, name, age, gender, history = None):
        super().__init__(name, age, gender)
        self.balance = 0
        self.history = []
        self.operation = 0
        self.block = 0
        self.update_history('open the account', self.balance, self.balance)

    
    def update_history(self, operation_details, pamount, qamount):
        self.operation += 1
        self.history.append((self.operation, operation_details, pamount, qamount, datetime.datetime.now()))
            
            

    def deposite(self, amount):
        temp = self.balance
        self.balance += amount
        print("deposite amount: your account balance has been updated as {} to {}".format(temp, self.balance))
        self.update_history('deposite amount', temp, self.balance)

      
    def blocked(self, amount):
        if self.balance - amount - self.block >= 0:
            self.block = amount
            print("{} money is blocked so you can not use this money. main blance is {}".format(amount, self.balance))
            self.update_history('blocked amount', self.balance, self.balance)
        else:
            print("{} money can not blocked . main blance is {}".format(amount, self.balance))
            self.update_history('blocked amount/fail', self.balance, self.balance)
            

    def unblocked(self,amount):
        if self.block - amount >= 0:
            self.block -= amount
            print("{} money is unblocked so you can use this money. main blance is {}".format(amount, self.balance))
            self.update_history('unblocked amount', self.balance, self.balance)


    def blocked_transfer(self, other, amount):
        try:
            other
        except NameError:
            print('receiver is not in memory ... transfer failed')
            self.obj1.update_history('transfer amount to other/failed', self.balance, other.balance)
        else:
            temp1 = self.block
            temp2 = other.balance
            if self.block - amount >=0:
                self.block -= amount
                other.balance += amount
                self.balance -= amount
                print("your account balance has been updated as {} to {}".format(temp1, self.balance))
                self.update_history('blocked_transferd amount to other', self.balance, self.balance)
                print("your account balance has been updated as {} to {}".format(temp2, other.balance))
                other.update_history('transferd amount from other', temp2, other.balance)
            else:
                print("your account has not enaugh money to transfer...\nrequest canceled")
                self.update_history('blocked_transfer amount to other/faild', self.balance, self.balance)

    def withdraw(self, amount):
        temp = self.balance
        if temp - amount - self.block>= 0:
            self.balance -= amount
            print("your account balance has been updated as {} to {}".format(temp, self.balance))
            self.update_history('withdraw amount', temp, self.balance)
        else:
            print("your account has not enaugh money to withdraw...\nrequest canceled")
            self.update_history('withdraw amount/faild', temp, self.balance)

    def transfer(self, other, amount):
        try:
            other
        except NameError:
            print('receiver is not in memory ... transfer failed')
            self.obj1.update_history('transfer amount to other/failed', self.balance, other.balance)
        else:
            temp1 = self.balance
            temp2 = other.balance
            if self.balance - amount - self.block>=0:
                self.balance -= amount
                other.balance += amount
                print("your account balance has been updated as {} to {}".format(temp1, self.balance))
                self.update_history('transferd amount to other', temp1, self.balance)
                print("your account balance has been updated as {} to {}".format(temp2, other.balance))
                other.update_history('transferd amount from other', temp2, other.balance)
            else:
                print("your account has not enaugh money to transfer...\nrequest canceled")
                self.update_history('transfer amount to other/faild', temp1, self.balance)

    def show_balance_details(self):
        print("your account has {} money...".format(self.balance))
        self.update_history('show balance details', self.balance, self.balance)
        

    def log(self):
        print('....'*30)
        print(":\n: Account log of user: {}  (up to {})".format(super().show_user_details()['name'], datetime.datetime.now()))
        print(":\n: Start log")
        print(": {}.  {}  {}  {}  {}".format( 'no'.rjust(5,' '), 
                                            'operation'.ljust(40, ' '), 
                                            'from_prize'.ljust(10, ' '),
                                            'to_prize'.ljust(10, ' '),
                                            'time'))

        for i in self.history:
            print(": {}.  {}  {}  {}  {}".format( str(i[0]).rjust(5,' '), 
                                                i[1].ljust(40, ' '), 
                                                str(i[2]).ljust(10, ' '),
                                                str(i[3]).ljust(10, ' '),
                                                i[4]))
        print(": Blocked amount: ", self.block)
        print(": End log\n:")
        print('....'*30 + "\n")

        
# create users
user1 = User('user1', 21, 'male')
user2 = Bank('user2', 35, 'femail', [])
user3 = Bank('user3', 53, 'mail', [])


# operations

# print(user1.show_user_details())
# print(user1.__dict__)
# print(help(User))
# print(user2.__dict__)
# a//b = a + b = total balance

user2.deposite(500)                # U2 500

user3.deposite(400)                # U3 400

user2.balance                       # U2 500
user2.withdraw(200)                 # U2 300
user2.show_balance_details()        # U2 300
user2.blocked(200)                  # U2 100//200
user2.withdraw(101)                 # U2 100//200 - 101//0 /faild      

user3.deposite(800)                 # U3 1200 
user3.withdraw(1000)                # U3 200
user3.transfer(user2, 210)          # U3 200 - 210/fail  
user3.withdraw(300)                 # U2 200 - 300 /fail

user2.withdraw(101)                 # U2 100//200 - 101//200 /fail
user2.withdraw(50)                  # U2 100//200 - 50//0 = 50//200 
user2.unblocked(150)                # U2 200//50
user2.transfer(user3, 50)           # U2 200//50 - 50//0 = 150//50
                                    # U3 200 + 50
user3.transfer(user2, 210)          # U3 250 - 210 = 40
                                    # U2 150//50 + 210//0 = 360//50
user3.blocked(50)                   # U3 40//0 - 0//50/FAILD 

user2.blocked_transfer(user3, 100)  # U2 360//50 - 0//100/faild
user2.blocked_transfer(user3, 50)   # U2 360//50 - 0//50 = 360//0
                                    # U3 40 + 50 = 90

user3.log()                         
user2.log()                         

""" output be like...
deposite amount: your account balance has been updated as 0 to 500
deposite amount: your account balance has been updated as 0 to 400    
your account balance has been updated as 500 to 300
your account has 300 money...
200 money is blocked so you can not use this money. main blance is 300
your account has not enaugh money to withdraw...
request canceled
deposite amount: your account balance has been updated as 400 to 1200 
your account balance has been updated as 1200 to 200
your account has not enaugh money to transfer...
request canceled
your account has not enaugh money to withdraw...
request canceled
your account has not enaugh money to withdraw...
request canceled
your account balance has been updated as 300 to 250
150 money is unblocked so you can use this money. main blance is 250
your account balance has been updated as 250 to 200
your account balance has been updated as 200 to 250
your account balance has been updated as 250 to 40
your account balance has been updated as 200 to 410
50 money can not blocked . main blance is 40
your account has not enaugh money to transfer...
request canceled
your account balance has been updated as 50 to 360
your account balance has been updated as 40 to 90
........................................................................................................................
:
: Account log of user: user3  (up to 2021-03-19 11:07:02.398175)
:
: Start log
:    no.  operation                                 from_prize  to_prize    time
:     1.  open the account                          0           0           2021-03-19 11:07:02.377526
:     2.  deposite amount                           0           400         2021-03-19 11:07:02.384786
:     3.  deposite amount                           400         1200        2021-03-19 11:07:02.386084
:     4.  withdraw amount                           1200        200         2021-03-19 11:07:02.387082
:     5.  transfer amount to other/faild            200         200         2021-03-19 11:07:02.389078
:     6.  withdraw amount/faild                     200         200         2021-03-19 11:07:02.391074
:     7.  transferd amount from other               200         250         2021-03-19 11:07:02.394064
:     8.  transferd amount to other                 250         40          2021-03-19 11:07:02.395061
:     9.  blocked amount/fail                       40          40          2021-03-19 11:07:02.396058
:    10.  transferd amount from other               40          90          2021-03-19 11:07:02.398054
: Blocked amount:  0
: End log
:
........................................................................................................................

........................................................................................................................
:
: Account log of user: user2  (up to 2021-03-19 11:07:02.412713)
:
: Start log
:    no.  operation                                 from_prize  to_prize    time
:     1.  open the account                          0           0           2021-03-19 11:07:02.377526
:     2.  deposite amount                           0           500         2021-03-19 11:07:02.384786
:     3.  withdraw amount                           500         300         2021-03-19 11:07:02.385783
:     4.  show balance details                      300         300         2021-03-19 11:07:02.386084
:     5.  blocked amount                            300         300         2021-03-19 11:07:02.386084
:     6.  withdraw amount/faild                     300         300         2021-03-19 11:07:02.386084
:     7.  withdraw amount/faild                     300         300         2021-03-19 11:07:02.392107
:     8.  withdraw amount                           300         250         2021-03-19 11:07:02.392107
:     9.  unblocked amount                          250         250         2021-03-19 11:07:02.393066
:    10.  transferd amount to other                 250         200         2021-03-19 11:07:02.393066
:    11.  transferd amount from other               200         410         2021-03-19 11:07:02.395061
:    12.  blocked_transfer amount to other/faild    410         410         2021-03-19 11:07:02.396058
:    13.  blocked_transferd amount to other         360         360         2021-03-19 11:07:02.397054
: Blocked amount:  0
: End log
:....................................................................................................................
"""

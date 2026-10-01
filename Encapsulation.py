class BankAccount:
    bname="SBI"
    def __init__(self,name,accno,IFSC,bal):
        self.name=name##public
        self._accno=accno##protected
        self.__bal=bal#private
    def getter(self):
        print("Account balance:",self.__bal)
    def display(self):
        print("BankAccount:",self.bname)
        print("Name:",self.name)
        print("Acc No:",self.accno)
        print("Balance:",self.bal)
s =BankAccount("Rajesh",1234,"SBI233",50000)
s1=BankAccount("Raju",1234,"Sbi3567",68876976)
print(s.name)
print(s._accno)
s.getter()

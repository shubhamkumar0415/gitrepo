class bank:
    def __init__(self,amount=0):
        self._amount = amount
    @property
    def amount(self):
        print("getting amount")
        return self._amount
    @amount.setter
    def amount(self,amount):
        print("setting amount",amount)
        self._amount = amount

    @amount.deleter
    def amount(self):
        print("deleting amount")
        del self._amount


obj = bank(30)
print(obj.amount)
obj.amount=50
print(obj.amount)
del obj.amount
# print(obj.amount)
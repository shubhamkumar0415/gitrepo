class bank:
    def __init__(self,amount1=0,amount2=0):
        self._amount1 = amount1
        self._amount2 = amount2

    def get_amt1(self):
        print("getting amount 1")
        return self._amount1
    def set_amt1(self, amount1):
        print("setting amount 1",amount1)
        self._amount1 = amount1
    def del_amt1(self):
        print("deleting amount 1 which was ",self._amount1)
        del self._amount1


    def get_amt2(self):
        print("getting amount 2")
        return self._amount2
    def set_amt2(self, amount2):
        print("setting amount 2",amount2)
        self._amount2 = amount2
    def del_amt2(self):
        print("deleting amount 2 which was ",self._amount2)
        del self._amount2

    amount1 = property(get_amt1,set_amt1,del_amt1,)
    amount2 = property(get_amt2,set_amt2,del_amt2,)

obj = bank(20)
print(obj.amount1)
obj.amount1=100
del obj.amount1

print(obj.amount2)
obj.amount2 = 200
del obj.amount2

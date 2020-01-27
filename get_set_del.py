class test:
    def __init__(self, val2=0,val3=0):
        self._val1 = val2
        self.a=val3


    def getter(self):
        print("getting value")
        return self._val1

    def setter(self, val):
        print("setting value", val)
        self._val1 = val

    def deleter(self):
        print("deleting value")
        del self._val1

    def gettera(self):
        print("getting value")
        return self.a

    def settera(self, val4):
        print("setting value", val4)
        self.a= val4

    def deletera(self):
        print("deleting value")
        del self.a

    val = property(getter,setter , deleter, )
    val1=property(gettera,settera,deletera,)

obj = test(10,13)
print(obj.val)
obj.val = 122
del obj.val
print(obj.val1)
obj.val1 = 122
del obj.val1

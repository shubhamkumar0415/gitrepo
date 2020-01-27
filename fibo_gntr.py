class fib:
    def __init__(self,limit):
        self.limit=limit
        self.a=0
        self.b=1
    def fibprint(self):
        
        for item in range(0,self.limit):
            x=self.a
            self.a,self.b=self.b,self.a + self.b
            yield x
abc=fib(10)
for i in abc.fibprint():
    print(i)
import sys
print(sys.version)
    
        

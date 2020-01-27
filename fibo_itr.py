class fib:
    def __init__(self,limit):
        self.limit=limit
    def __iter__(self):
        self.a=0
        self.b=1
        self.c=0
        return  self
    def __next__(self):
        if(self.limit <= self.c):
            raise StopIteration
        self.c=self.c +1
        
        x=self.a
        self.a,self.b=self.b,self.a + self.b
        return x
abc=fib(10)
for i in abc:
    print(i)
        
        

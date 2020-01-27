class fib:
    def __init__(self, limit):
        self.limit=limit
        self.a = 0
        self.b = 1
    def fibprint(self):
        
        while(1):
            x=self.a
            self.a, self.b=self.b, self.a + self.b
            yield x
abc=fib(10)
for i in range(10):
    print(next(abc.fibprint()))
    


class test:
    def __init__(self,val):
        self.val=val
        
    def __iter__(self):
        self.initial=10
        return self

    
    def __next__(self):
        if self.val <= self.initial:
            raise StopIteration
        x=self.initial
        self.initial+=1
        
        return x
a=test(15)
for i in a:
    print(i)

        

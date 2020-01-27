def map1(func,*args):
    for i in zip(*args):
        yield func(*i)
def fun(a,b):
    return a+b
l=list(map1(fun,[1,2,3],[4,5,6,7]))
print(l)


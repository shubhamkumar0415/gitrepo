def map1(fun,argvs,*argv):
    for a in zip(argvs,*argv):
        yield(fun(*a))
def fun1(a,b,c):
    return a+b+c
l1=[1,2,3]
l2=[4,5,6]
l3=[6,7,8]
l=list(map1(fun1,l1,l2,l3))
print(l)

    
    

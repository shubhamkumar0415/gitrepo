l=[1,2,3,4,5]
def odd(x):
    if x%2==0:
        return(True)
    else:
        return False
m=[x for x in l if(odd(x))]
print(m)
k= [[x*y for x in l] for y in m]
print(k)


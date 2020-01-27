l=[["shubham",21],["ravi",23],["ram",22],["rajat",19]]
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if(l[j][1]>l[j+1][1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)   
    

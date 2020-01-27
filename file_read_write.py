file=input()
tx=open(file,'r')
fx=open("bcd.txt",'w')
print("both file opened")
c=tx.readline()
while(c):
    if('s' in c):
        fx.write(c)
        print(c)
    c=tx.readline()
tx.close()
fx.close()
print("work done")
    

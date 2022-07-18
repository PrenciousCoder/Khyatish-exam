def sequence():
     global z
     n=2
     z=1
     s=str(Fib(0))

     for i in range(1,n+1,1):
        z=1
        s=s+", "+ str(Fib(i))
     print(s)

def Fib(i):
    global z
    print("z="+str(z)+", i="+ str(i))
    z=z+1

    if (i<2):
        return i
    else:
        return Fib(i-1)+Fib(i-2)

z=0
sequence()

     
    

    
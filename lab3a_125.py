def divisor(num):
    for i in range(1,num):
        if num%i==0:
            print(i,end=" ")
      
num=int(input("enter number"))
print("divisor are",end="")
divisor(num)

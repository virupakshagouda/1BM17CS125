def find(list1,b):
        print(list1)
        if b in list1: 
                return True
        else :
                 return False
list1=[]
while True:
    a=int(input("Enter  the elements ,Enter -1 to exit"))
    if(a!=-1):
          list1.append(a)
    else :
          break
b=int(input("Enter key to search"))
print(find(list1,b))

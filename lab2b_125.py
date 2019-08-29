  
def rev1(str):
    list1=str1.split(" ");
    list1.reverse()    
    a=" "
    s2=a.join(list1)
    print(s2)

def revstring(str1):
    list1=str1.split(" ");
    list2=""
    for i in list1:
        list2+=i[::-1]
        list2+=" "
    print(list2)

str1=input("Enter the string : ");
rev1(str1)
revstring(str1)
    

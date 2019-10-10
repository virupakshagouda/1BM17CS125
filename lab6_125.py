a=input("enter string")

class validate:
    c1=0;c2=0;c3=0;
    for i in a:
        if i=='(':
            c1+=1
        elif i==')':
            c1-=1
        elif i=='{':
            c2+=1
        elif i=='}':
            c2-=1
        elif i=='[':
            c3+=1
        elif i==']':
            c3-=1
    if c1==0 and c2==0 and c3==0:
        print("valid parenthesis")
    else:
        print("invalid parenthesis")
        

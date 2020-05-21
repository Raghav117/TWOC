n = int(input("Enter the number strings:")) 
  
str = [] 
for i in range(n):          
    a=input()
    str.append(a) 

c=0
for i in range(len(str[0])):
    for j in range(len(str)):
        if(len(str[j])==i or str[0][i]!=str[j][i]):
            print(str[0][:i])
            c=1
            break
    if c==1:
        break

if c==0:
    print(str[0])

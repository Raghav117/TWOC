def integer(n,index):
    tmp = ord(n[index])
    # print(tmp)
    index2 = index
    while(index+1<len(n) and tmp<ord(n[index+1])):
        index+=1

    n1 = n[:index2] + n[index]
    n2 = n[index2+1:index] + n[index2] +n[index+1:]
    n2 = ''.join(sorted(n2))
    # print(n2)
    x=n1+n2
    
    return x




n = input("Enter number : ")
# index=3
# index2=7
# n1 = n[:index] + n[index2] + n[index+1:index2] + n[index] +n[index2+1:]
# print(n1)  
i=len(n)-2


while i>=0:
    if ord(n[i])<ord(n[i+1]):
        # print(i)
        print(integer(n,i))
        break
        
    i-=1
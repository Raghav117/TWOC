def integer(lst):

    index =  0

    for ele in lst:
        if ele>0:
            index+=1
            if index!=ele:
                return index

    return index+1


lst = [] 
  
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)


lst = sorted(lst, key=float)
print(integer(lst))

lst = [] 
stack = []
n = int(input("Enter number of elements : ")) 
# k = int(input("Enter number of elements to be know : ")) 
k=3

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)
    if len(stack)<k:
        stack.append(ele)
    else:
        if stack[k-1]<ele:
            stack.pop()
            stack.append(ele)
    
    stack = sorted(stack,reverse=True)

mul=1

for i in stack:
    mul*=i


print(mul)
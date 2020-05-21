lst = [] 
smaller = []
s=0
l=0
larger = []
  
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)

s=lst[0]
l=lst[n-1]

for i in range(n-1, -1,-1):
    
    if l<=lst[i]:
        l=lst[i]

    larger.append(l)
larger.reverse()

# print(larger)

for i in range(0,n,1):
    if s>lst[i]:
        s=lst[i]
    smaller.append(s)

for i in range(n):
    if (lst[i]>smaller[i] and lst[i]<larger[i]):
        print(lst[i])
        break


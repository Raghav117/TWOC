str = input("Enter your string: ")
str=str.upper()
print(str)
lst =[];

for i in range(0,26):
    lst.append(0)
    # print(i,lst[i])

for i in str:
    lst[ord(i)-65]+=1
    # print(lst[ord(i)-65])

# even = 0
odd = 0

for i in range(0,26):
    if lst[i]%2!=0:
        odd+=1

if len(str)%2!=0:
    odd-=1

if odd>=0:
    print(odd)
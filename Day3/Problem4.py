list = []

n = int(input("Enter number of elements "))

for i in range(0,n):
    element = input()
    
    list.append(element)

print("List is : "+ str(list))

reoe = []

for i in list:
    if i not in reoe:
        reoe.append(i)
        
print("List after removing duplicates: " + str(reoe))
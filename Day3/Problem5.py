list1 = []
list2 = []

n = int(input("Enter the number of elements of list1 "))

for i in range(0,n):
    element1 = input()
    
    list1.append(element1)
    
n = int(input("Enter the number of elements of list2 "))

for i in range(0,n):
    element2 = input()
    
    list2.append(element2)    
    
print("Original list 1 : " + str(list1))
print("Original list 2 : " + str(list2))

add = list1
for i in range(0,len(list2)):
    add.append(list2[i])
    
print("Combined list : " + str(add))

rep = []

for i in add:
    if i not in rep:
        rep.append(i)
        
print("Intersection : " + str(rep))
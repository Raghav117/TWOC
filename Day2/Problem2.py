n = int(input("Enter number of inputs "))

m1 = 0
m2 = 1
count = 0

if n <= 0:
    print("Enter + integer")
elif n == 1:
    print("Fibonacci sequence upto",n)
    print(m1)
else:
    print("Fibonacci sequence upto",n)
    while count < n:
        print(m1)
        new = m1 + m2
        m1 = m2
        m2 = new

        count += 1

    

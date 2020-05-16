a = int(input("Enter Integer "))

def evenenenenenen(a):
    if (a%2==0):
        print("evenenenenenenen")
    else:
         print("Odd")

def prime(a):
    if (a>1):
        for i in range(2,a):
            if (a % i) == 0:
                print(a," is not a prime number")
                break
        else:
            print(a," is a prime number")

    else:
        print(a," is not prime number")

def palinDrome(a):
    return a == a[::-1]


def armstrong(a):
    s = 0

    t = a
    while t > 0:
        rem = t%10
        s += rem**3
        t //=10
    
    if a == s:
        print(a," is a armstrong number")
    else:
        print(a," is not Armstrong number")

evenenenenenen(a)
prime(a)

x = palinDrome(str(a))
if a:
    print(a,"is palinDrome")
else:
    print(a,"is not palinDrome ")

armstrong(a)




a = int(input("Enter 1st Score "))
b = int(input("Enter Player2 Score "))
c = int(input("Enter Player3 Score "))

def strike(x):
    rate = (x*100)/60

    return rate

def sixes(x):
    maxim = x/6

    return int(maxim)

print("Strike rate of 1st: " + str(strike(a)))
print("Strike rate of Player2: " + str(strike(b)))
print("Strike rate of Player3: " + str(strike(c)))

print("maximum number of sixes each player could have hit: " + str(sixes(a)))
print("maximum number of sixes each player could have hit: " + str(sixes(b)))
print("maximum number of sixes each player could have hit: " + str(sixes(c)))
Cost = int(input("Enter Cost Price "))
Sl = int(input("Enter Sling Price "))

Profit = Sl-Cost
profit_per = (Profit/Cost)*100

inc_profit_per = ((5*profit_per)/100) + profit_per

new_sp = Cost + (inc_profit_per/100)*Cost

print(new_sp)
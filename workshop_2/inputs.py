balance = int(input("Balance: "))
sandwich = int(input("Sandwich Price: "))
sandwich_count = int(input("Sandwich Count: "))
groceries = int(input("Groceries Price: "))

print(f"Balance: {balance}")
print(f"Sandwich: {sandwich}")
print(f"Groceries: {groceries}")

print(f"I am buying {sandwich_count} sandwich that costs {sandwich * sandwich_count} bucks, I have {balance} bucks")

balance -= (sandwich * sandwich_count)
print(f"Now I have {balance}$")

print(f"I have groceries to buy that costs {groceries} bucks, now I have {balance}")
balance -= groceries
print(f"At the end I have left {balance}$")
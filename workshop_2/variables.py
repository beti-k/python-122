PI = 3.14
balance = 150
sandwich = 9
groceries = 65
sandwich_count = 1 # snake_case

# print("Balance")
# print("Balance " + str(balance))
print(f"Balance: {balance}")
print(f"Sandwich: {sandwich}")
print(f"Groceries: {groceries}")

print(f"I am buying {sandwich_count} sandwich that costs {sandwich * sandwich_count} bucks, I have {balance} bucks")

# balance = balance - (sandwich * sandwich_count)
# short-hand assignment operator
balance -= (sandwich * sandwich_count)
print(f"Now I have {balance}$")

print(f"I have groceries to buy that costs {groceries} bucks, now I have {balance}")
balance -= groceries
print(f"At the end I have left {balance}$")

# print("I am buying a sandwich that costs 6 bucks, I have 100 bucks")

# print("After buying I have")
# print(100 - 6)

# print("I have groceries to buy that costs 50 bucks, now I have 94")
# print("now I have ")
# print(94 - 50)
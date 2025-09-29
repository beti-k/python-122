def string_to_integer(s):
    try:
        num = int(s)
        return num
    except ValueError:
        return "Invalid input! Please enter numbers only."

# Examples:
print(string_to_integer("123"))  
print(string_to_integer("hello")) 
try:
    age = int(input("How old are you? "))

    if age <= 0:
        print("Invalid input! Age must be a positive number.")
    else:
        if age < 18:
            print(f"You are {age} years old. You are a minor.")
        else:
            print(f"You are {age} years old. You are an adult.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
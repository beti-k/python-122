name_1 = "Lizi"
name_2 = 'Luka'
name_3 = """Anna"""
name_4 = '''Gio'''


def greet_user(name):
    if name.strip() == "":
        return "Invalid input! Name cannot be empty."
    return f"Hello, {name}!"


print(greet_user(name_1))
print(greet_user(name_2))
print(greet_user(""))     
print(greet_user("   "))  


print("Hello\n\tWorld!")
print("He said: \"Hi!\"")
print('She replied: "Hello!"')


print(len(name_1))
print(len(" "))
print(len("\t"))
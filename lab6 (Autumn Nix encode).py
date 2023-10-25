# Autumn Nix's encode file

def encode(password):
    split_password = []
    split_password.extend(password)
    new_password = str()
    for element in split_password:
        element = int(element)
        if element >= 7:
            if element == 7:
                element = 0
            elif element == 8:
                element = 1
            elif element == 9:
                element = 2
        else:
            element += 3
        element = str(element)
        new_password += element
    return new_password

print("Menu")
print("-------------")
print("1. Encode")
print("2. Decode")
print("3. Quit")
print()
option = int(input("Please enter an option: "))
if option == 1:
    password = str(input("Please enter your password to encode: "))
    encode(password)
    print("Your password has been encoded and stored!")
elif option == 2:
    pass
elif option == 3:
    pass

def encode(password):
    output = ""



    for value in password:
         current_val= str((int(i) + 3) % 10)
        output += current_val
    return output
def display_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")


while True:
    display_menu()
    choice = int(input("Please enter an option:"))

    if choice == 1:
        password = input("Please enter your password to encode:")
        print("Your password has been encoded and stored!")
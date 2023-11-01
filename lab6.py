def encode(password):
    output = ""

    for i in password:
        current_val= str((int(i) + 3) % 10)
        output += current_val
    return output
def display_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
def decode_password(new_pas):
    decode = ""
    for i in new_pas:
        decode_dig = str((int(i)-3)%10)
        decode += decode_dig
    return decode

while True:
    display_menu()
    choice = int(input("Please enter an option:"))

    if choice == 1:
        password = input("Please enter your password to encode:")
        print("Your password has been encoded and stored!")
    #this was done by michael veksler
    if choice == 2:
        new_pas = encode(password)
        old_pas = decode_password(new_pas)
        print(f"The encoded password is {new_pas}, and the original password is {old_pas}")
    if choice == 3:
        break



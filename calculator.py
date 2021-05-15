import os, ctypes

if os.name =='nt':
	ctypes.windll.kernel32.SetConsoleTitleW(f"WHY DID I MAKE A CALCULATOR?")

signs = ['Add', 'Subtract', 'Multiply', 'Divide']
symbol = (input("How do you want to combine your numbers?\n"))
sign, output = "0", "0"

if symbol not in signs:
    print("That is not a valid choice.")
    exit()

else:
    first = int(input(f"What is the first number you would like to {symbol}?\n"))
    second = int(input("And the second one?\n"))

if symbol == "Add":
    output = first + second
    sign = "+"

elif symbol == "Subtract":
    output = first - second
    sign = "-"

elif symbol == "Multiply":
    output = first * second
    sign = "*"

elif symbol == "Divide":
    output = first / second
    sign = "/"

else:
    print("wtf are you doing, you think that this program is that complex to understand what you just put there?\n")

print(f"Your answer is: {first} {sign} {second} = {output}\n")

import os, ctypes

if os.name =='nt':
	os.system('cls')
	ctypes.windll.kernel32.SetConsoleTitleW(f"WHY DID I MAKE A CALCULATOR?")

signs = ['+', '-', '*', '/']
symbol = (input("What operator are you using today? ( +, -, *, / ) "))
output = "0"

if symbol not in signs:
	print("That is not a valid choice.")
	exit()

else:
	first = int(input(f" _ {symbol} _ = _ "))
	second = int(input(f"{first} {symbol} _ = _ "))

if symbol == "+":
	output = first + second

elif symbol == "-":
	output = first - second

elif symbol == "*":
	output = first * second

elif symbol == "/":
	output = first / second
 
print(f"{first} {symbol} {second} = {output}")

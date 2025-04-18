letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
password = ""
#choose random letters from letters list
rndm_letters = random.choices(letters, k=nr_letters)

#choose random numbers from numbers list
rndm_numbers = random.choices(numbers, k=nr_numbers)

#choose random symbols form symbols list
rndm_symbols = random.choices(symbols, k=nr_symbols)

# Combine these three to make a one password sequence
password_seq = rndm_letters + rndm_numbers + rndm_symbols

# make password complex by shuffling elements
random.shuffle(password_seq)

# Now make a string of these elements
for i in password_seq:
    password += i

print(f"Here is your password: {password}")
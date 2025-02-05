from art import logo
print(logo)

should_continue = True

# Save data into dictionary {name: price}
bidder = {}

while should_continue:
    # Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    # add name and bid in dictionary
    bidder[name] = bid

    # Whether if new bids need to be added
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if new_bid == 'no':
        should_continue = False
    else:
        print("\n" * 20)

# Compare bids in dictionary
highest = 0
winner = "No one"
for key in bidder:
    if bidder[key] > highest:
        highest = bidder[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest}")

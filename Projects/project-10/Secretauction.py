bids={}
print("Welcome to the secret auction program")
loop=True

def find_highest_bidder(bidsl):
    high=0
    winner=""
    for key in bidsl:
        if bidsl[key]>high:
            high=bidsl[key]
            winner=key

    print(f"winner:{winner} and bid:{high}")

while loop:
    name=input("What is your name?")
    cost=float(input("What is your bid?"))
    bids[name]=cost
    while True:
        continues=input("Are there any other bidders (y/n)")
        if continues=="y":
            print("\n" * 20)
            break
        elif continues=="n":
            loop=False
            break
        else:
            print("Enter the correct character.")

find_highest_bidder(bids)

print("Welcome to the trip calculator!")
bill=float(input("what was the total bill?"))
tip=int(input("how much tip would you like to give? 10 , 12 or 15"))
people=int(input("How many people to split the bill?"))
a=(bill*tip)/100
b=(a+bill)/people
print(f"Each person should pay $ {round(b,3)}")

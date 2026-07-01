#input-output-basic-project
print("Welcom to the Band Name Generator.")
city= input("Which city did you grow up in?")
pet= input("What is the name of a pet")
print("Your band name could be:" + city +" " + pet)
print(len(city))
print(len(pet))
temp=city
city=pet
pet=temp
print(city +" " + pet)


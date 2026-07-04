import random
alfabe = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
ozel_karakterler = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
sayilar= ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_alfabe=input("kaç adet harf olsun")
number_karekter=input("kaç adet karekter olsun")
number_sayi=input("kaç adet sayı olsun")

password_list=[]

for a in range(0,int(number_alfabe)):
    password_list.append(random.choice(alfabe))
for a in range(0,int(number_karekter)):
    password_list.append(random.choice(ozel_karakterler))
for a in range(0,int(number_sayi)):
    password_list.append(random.choice(sayilar))

random.shuffle(password_list)
password= ""
for a in password_list:
    password += a
print(password)



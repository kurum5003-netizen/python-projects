print("welcome to treasure ısland.\n your miison is find to trasure")
yon1=input("left or right")
if yon1=="left":
    yon2=input("swim or wait")
    if yon2=="wait":
         yonb3=input('which "door"(red/blue/yellow')
         if yonb3=="yellow":
             print("you win")
         elif yonb3=="red":
             print("you lose")
         elif yonb3=="blue":
             print("you lose")
         else:
             print("geçersiz seçim")
    else:
        print("you lose")
else:
    print("you lose")

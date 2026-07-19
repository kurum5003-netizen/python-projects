tank= {
    "water":300,
    "coffee":100,
    "milk":200
}
expresso= {
    "water":50,
    "coffee":18,
    "price":150
}
latte= {
    "water":200,
    "coffee":24,
    "milk":150,
    "price":250
}
capuccino= {
    "water":250,
    "coffee":25,
    "milk":100,
    "price":300
}

def tank_control(tankk,icicek):
    if tankk["water"]<icicek["water"]:
        print("yeterli kaynak yok")
        return False
    if tankk["coffee"]<icicek["coffee"]:
        print("yeterli kaynak yok")
        return False
    if "milk" in icicek:
        if tankk["milk"]<icicek["milk"]:
            print("yeterli kaynak yok")
            return False

    return True

def tank_set(tankk, icicek):
    tankk["water"] -= icicek["water"]
    tankk["coffee"] -= icicek["coffee"]

    if "milk" in icicek:
        tankk["milk"] -= icicek["milk"]
def jeton_op(penny1,nickel1,dime1,quarter1,icicek):
    total=0
    total+=penny1*1
    total+=dime1*10
    total+=quarter1*25
    total+=nickel1*5
    if total==icicek["price"]:
        print("ücret tam")
        return True
    elif total>icicek["price"]:
        print(f"fazla ücret verdiniz para üstünüz:{total-icicek['price']}")
        return True
    else:
        print("üzgünüm eksik ücret verdiniz")
        return False

def report():
    print(f"Water: {tank['water']}ml")
    print(f"Milk: {tank['milk']}ml")
    print(f"Coffee: {tank['coffee']}gr")

def coffe_machine():
    print("Hoşgeldiniz!!")
    while True:
        choice=input("ne içmek istersiniz 'latte','expresso','capuccino' and çıkmak için 'q'").lower()
        if choice=="latte":
            a=tank_control(tank,latte)
            if not a:
                break
            penny= int(input("kaç adet penny var?"))
            nickel= int(input("kaç adet nickel var?"))
            dime= int(input("kaç adet dime var?"))
            quarter= int(input("kaç adet quarter var?"))
            b= jeton_op(penny,nickel,dime,quarter,latte)
            if not b:
                c=input("başka içicek içmek istermiisniz 'y/n'")
                if c=="y":
                    continue
                else:
                    break
            print("içicek hazırlanıyor...")
            tank_set(tank,latte)
            print("afiyet olsun!!!")
            continue
        elif choice=="expresso":
            a = tank_control(tank, expresso)
            if not a:
                break
            penny = int(input("kaç adet penny var?"))
            nickel = int(input("kaç adet nickel var?"))
            dime = int(input("kaç adet dime var?"))
            quarter = int(input("kaç adet quarter var?"))
            b = jeton_op(penny, nickel, dime, quarter, expresso)
            if not b:
                c = input("başka içicek içmek istermiisniz 'y/n'")
                if c == "y":
                    continue
                else:
                    break
            print("içicek hazırlanıyor...")
            tank_set(tank, expresso)
            print("afiyet olsun!!!")
            continue
        elif choice=="capuccino":
            a = tank_control(tank, capuccino)
            if not a:
                break
            penny = int(input("kaç adet penny var?"))
            nickel = int(input("kaç adet nickel var?"))
            dime = int(input("kaç adet dime var?"))
            quarter = int(input("kaç adet quarter var?"))
            b = jeton_op(penny, nickel, dime, quarter, capuccino)
            if not b:
                c = input("başka içicek içmek istermiisniz 'y/n'")
                if c == "y":
                    continue
                else:
                    break
            print("içicek hazırlanıyor...")
            tank_set(tank, capuccino)
            print("afiyet olsun!!!")
            continue
        elif choice=="q":
            break
        elif choice=="rapor":
            report()
            continue
        else:
            print("geçersiz işlem")

coffe_machine()






import random
deck = [
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"
]
def oyuncukontrol(odeste):
    total = 0
    for o in odeste:
        if o=="J" or o=="Q" or o=="K":
            total +=10
        else:
            total += o
    if total>21:
        print(total)
        print("deste 21 i aştı kaybettiniz")
        return False,total
    else:
        print(total)
        return True,total

def computerkontrol(cdeste):
    total = 0
    for c in cdeste:
        if c=="J" or c=="Q" or c=="K":
            total +=10
        else:
            total += c
    if total>21:
        print(total)
        print("deste 21 i aştı oyuncu kazandı")
        return False,total
    else:
        print(total)
        return True,total

def kazanan(total1,total2):
    if total1==total2:
        print("berabere")
    elif total1>total2:
        print("oyuncu kazandı")
    else:
        print("computer kazandı")

def game():
    random.shuffle(deck)
    a1=deck.pop()
    a2=deck.pop()
    a3=deck.pop()
    a4=deck.pop()
    oyuncud=[a1,a2]
    computerd=[a3,a4]
    b=input("oyuna başlamak için 'y' basın iptal etmek için 'x' e basın")
    if b=="y":
        print(f"oyuncu:{oyuncud[0]},{oyuncud[1]}")
        print(f"computer:{computerd[0]},?")
        oyunadevam1,total1=oyuncukontrol(oyuncud)
        if not oyunadevam1:
            return

        while True:
            choice=input("hit OR pass").lower()
            if choice=="hit":
                oyuncud.append(deck.pop())
                print(oyuncud)
                oyunadevam2,total1=oyuncukontrol(oyuncud)
                if not oyunadevam2:
                    return

            elif choice=="pass":
                print(f"computer:{computerd[0]},{computerd[1]}")
                oyunadevam3,total3=computerkontrol(computerd)
                if not oyunadevam3:
                    return
                while total3 < 17:
                    computerd.append(deck.pop())
                    print(computerd)
                    oyunadevam4 ,total3 = computerkontrol(computerd)
                    if not oyunadevam4:
                        return

                kazanan(total1,total3)
                return
            else:
                print("geçersiz işlem")

    else:
        return
game()

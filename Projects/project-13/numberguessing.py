import random

HARD_LIFE=5
EASY_LIFE=10

def set_difficulty():
    while True:
        choice = input("zor mod için 'z' ye kolay mod  için 'e' basın")
        if choice=="z":
            return HARD_LIFE
        elif choice=="e":
            return EASY_LIFE
        else:
            print("lütfen geçerli karekter girin")


def game(mode,number):
    if mode==5:
        print("zor modasınız can hakkınız:5")
    else:
        print("kolay modasınız can hakkınız:10")
    while mode>0:
        tahmin=int(input("tahmininiz nedir?"))
        if tahmin>number:
            print("tahmininiz yukarda")
            mode-=1
            print(f"kalan can:{mode}")
        elif tahmin<number:
            print("tahmininiz aşağıda")
            mode-=1
            print(f"kalan can:{mode}")
        else:
            print("TEBRİKLER!!! ")
            return

    print(f"Canınız bitti. Doğru sayı {number} idi.")

print("Sayı tahmin oyununa hoşgeldiniz!!")
numrandom=random.randint(1,100)
mode_choice=set_difficulty()
game(mode_choice,numrandom)






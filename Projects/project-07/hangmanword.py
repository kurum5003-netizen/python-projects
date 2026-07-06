import random
import hangmanword

t_tahmin=random.choice(hangmanword.wordlist)

placeholder= " "
word_length=len(t_tahmin)

for p in range(word_length):
    placeholder += "-"
print(placeholder)
gameover=False
corect_letters=[]
live =3
while not gameover:
    print("6 hakkınız var bol şans")
    guess=input("harf tahmin edin").lower()

    display = ""

    for letter in t_tahmin:
        if letter == guess:
            print("doğru tahmin tebrikler")
            display +=letter
            corect_letters.append(letter)
        elif letter in corect_letters:
            display += letter
        else:
            display += "-"

    if guess not in corect_letters:
        live -= 1
        print("yanlış tahmin")
        print(f"kalan canınız : {live}")
        if live == 0:
            gameover=True
            print("canınız bitti")

    print(display)

    if "-" not in display:
        gameover=True
        print("kazandınız")


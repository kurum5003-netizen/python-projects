alphabet=['a','b','c','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

direction=input("decode or encode").lower()
text=input("type your message").lower()
shift=int(input("type the shift number"))

def encrypt (text_origin, shift_no):
    text2=""
    for letter in text_origin:
        shift_amounts=alphabet.index(letter) + shift_no
        shift_amounts=shift_amounts % len(alphabet)
        text2+=alphabet[shift_amounts]

    print(f"encode:{text2}")

def decrypt (text_origin, shift_no):
    text2=""
    for letter in text_origin:
        shift_amounts=alphabet.index(letter) - shift_no
        shift_amounts = shift_amounts % len(alphabet)
        text2 += alphabet[shift_amounts]

    print(f"decode:{text2}")

#decrypt ve encrypt birleşimi
def caesar (text_origin, shift_no, direction):
    text2=""
    if direction=="decode":
        shift_no*=-1

    for letter in text_origin:
        if letter in alphabet:
            shift_amount = (alphabet.index(letter) + shift_no) % len(alphabet)
            text2 += alphabet[shift_amount]
        else:
            text2 += letter
    if direction=="encode":
        print(f"encode:{text2}")
    else:
        print(f"decode:{text2}")

caesar(text, shift, direction)

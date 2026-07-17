import random
data = [
    {
        "name": "Cristiano Ronaldo",
        "followers": 655,
        "description": "Football player",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "followers": 505,
        "description": "Football player",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "followers": 420,
        "description": "Singer and actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "followers": 393,
        "description": "Media personality",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "followers": 395,
        "description": "Actor and wrestler",
        "country": "United States"
    },
    {
        "name": "Ariana Grande",
        "followers": 376,
        "description": "Singer",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "followers": 357,
        "description": "Media personality",
        "country": "United States"
    },
    {
        "name": "Beyoncé",
        "followers": 311,
        "description": "Singer",
        "country": "United States"
    },
    {
        "name": "Khloé Kardashian",
        "followers": 302,
        "description": "Media personality",
        "country": "United States"
    },
    {
        "name": "Nike",
        "followers": 307,
        "description": "Sportswear brand",
        "country": "United States"
    },
    {
        "name": "Justin Bieber",
        "followers": 295,
        "description": "Singer",
        "country": "Canada"
    },
    {
        "name": "Taylor Swift",
        "followers": 284,
        "description": "Singer",
        "country": "United States"
    },
    {
        "name": "Virat Kohli",
        "followers": 274,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Jennifer Lopez",
        "followers": 248,
        "description": "Singer and actress",
        "country": "United States"
    },
    {
        "name": "Nicki Minaj",
        "followers": 227,
        "description": "Rapper",
        "country": "Trinidad and Tobago"
    },
    {
        "name": "Neymar Jr",
        "followers": 230,
        "description": "Football player",
        "country": "Brazil"
    },
    {
        "name": "Zendaya",
        "followers": 177,
        "description": "Actress",
        "country": "United States"
    },
    {
        "name": "Shakira",
        "followers": 92,
        "description": "Singer",
        "country": "Colombia"
    },
    {
        "name": "Vin Diesel",
        "followers": 104,
        "description": "Actor",
        "country": "United States"
    },
    {
        "name": "Emma Watson",
        "followers": 73,
        "description": "Actress",
        "country": "United Kingdom"
    }
]

def game():
    random.shuffle(data)
    score=0
    person1=data.pop()
    person2=data.pop()
    while True:
        print(f"COMPARE A:{person1["name"]} , a {person1["description"]} , from {person1["country"]}")
        print("VS")
        print(f"B:{person2["name"]} , a {person2["description"]} , from {person2["country"]}")
        choice = input("Who has more followers?").lower()
        if choice == "a":
            if person1["followers"] > person2["followers"]:
                score+=1
                if len(data) == 0:
                    print(f"You finished the game! Score: {score}")
                    return
                person2=data.pop()
                print(f"YOU'RE RİGHT! SCORE: {score}")
            else:
                print("you Lose")
                if score > 0:
                    print(f"finally score {score}")
                return
        elif choice == "b":
            if person2["followers"] > person1["followers"]:
                score+=1
                if len(data) == 0:
                    print(f"You finished the game! Score: {score}")
                    return
                person1=person2
                person2=data.pop()
                print(f"YOU'RE RİGHT! SCORE: {score}")
            else:
                print("you Lose")
                if score > 0:
                    print(f"finally score {score}")
                return



game()

def calculate_love_score(name1, name2):
    namemerge = (name1 + name2).lower()

    timet = timer = timeu = timee = 0
    lovet = lover = loveu = lovee = 0

    for letter in namemerge:
        if letter == 't':
            timet += 1
        elif letter == 'r':
            timer += 1
        elif letter == 'u':
            timeu += 1
        elif letter == 'e':
            timee += 1

    timetotal = timet + timer + timeu + timee

    for letter in namemerge.lower():
        if letter == 'l':
            lovet += 1
        elif letter == 'o':
            lover += 1
        elif letter == 'v':
            loveu += 1
        elif letter == 'e':
            lovee += 1

    lovetotal = lovet + lover + loveu + lovee

    print("Love Score = " + str(timetotal) + str(lovetotal))


calculate_love_score("Angela Yu", "Jack Bauer")

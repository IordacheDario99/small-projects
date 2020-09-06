films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}

while True:
    choice = input("What movie would to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())
        # Check user age
        if age >= films[choice][0]:
            # Check seats available
            if films[choice][1] > 0:
                print("Enjoy the movie!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("No more seats available")
        else:
            print("You are not old enough!")
    else:
        print("We don't have that movie...")
known_users = ["Drio","Andrei","Danciu","David","Bogdan","Georgiana","Gaby","Laur"]

while True:
    print("My name is Travis, the security robot.")
    user_input_name = input("What is your name? : ").strip().capitalize()

    if user_input_name in known_users :
        print("Welcome {}!".format(user_input_name))
        answer = input("Would you like to be removed from the database? [Y/N]").strip().upper()
        if answer != "Y" and answer!="N":
            print("Invalid answer, please try again!")
        elif answer == "Y":
            known_users.remove(user_input_name)
            print("You have been removed form the database!\nGood by!")
            break
        elif answer == "N":
            print("OK!")
    else:
        print("{} is not recognised as a valid user!".format(user_input_name))
        answer = input("Would you like to be introduced into the database? [Y/N]").strip().upper()
        if answer != "Y" and answer!="N":
            print("Invalid answer, please try again!")
        elif answer == "Y":
            known_users.append(user_input_name)
            print("You have been added to the database!\nWelcome!")
        elif answer == "N":
            print("OK!\nGood by!")
            break

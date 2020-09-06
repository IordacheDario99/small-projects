from random import choice

questions = ["Why do the farts smell?", "Why do we need to fart?","Why is impolite to fart"]
question = choice(questions)
answer = input(question).strip().title()
while answer != "just because":
    answer = input("Why? ").strip().lower()
print("Oh...Okay.")

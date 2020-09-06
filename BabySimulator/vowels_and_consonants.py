user_input = input ("Enter the word: ").strip ().lower ()
vowels = []
consonants = []

for word in user_input :
    if word in "aeiou" :
        vowels.append (word)
    elif word in "bcdefghjklmnpqrstvxz" :
        consonants.append (word)

print(vowels)
print(consonants)

students = {
    "male":["Ion", "Alin","Gigel","Costel"],
    "female":["Ioana","Maria","Camelia","Georgiana"]
}
for keys in students.keys():
    for name in students[keys]:
        if "A" in name.upper():
            print(name)


words = ["calota","vulpe","lup","urs","apa","miere"]
stuff = [[w.upper(), w.lower() ]for w in words]
print(stuff)
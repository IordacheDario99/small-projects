#ask user for name
name = input("What is your name?: ")
#ask user for age
age = input("what is your age?: ")
#ask user for location
state = input("What state are you from?: ")
city = input("What city are you from?: ")
#ask user what they enjoy
love = input("What are you passionate about, what do you love to do?: ")
#create output text
string = "Your name is {} and you are {}yo, you live in {},{} and you love {}"
output = string.format(name, age, state, city, love)
#print output to screen
print(output)
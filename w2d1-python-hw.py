# Exercise #1
# Accept two user ages as inputs and give us the difference between them. 
# (The Answer should always be a positive output)

age1 = int(input("What is your age? "))
age2 = int(input("What is your age? "))

age_difference = abs(age1 - age2)
print("The age difference between the two users is:", age_difference)


# Exercise #2
# Accept 3 user inputs for variables named noun, verb and adjective. 
# Print out a formatted string using the outputs.

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

show_me = f"The {adjective} {noun} {verb}"
print(show_me)


# Exercise #3
# Take in a users input for their age, if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, 
# else print seniors

age = int(input("What is your age? "))

if age <18:
    print("Kids")
elif age >= 18 and age <= 65:
    print("Adults")
else:
    print("Seniors")


# Exercise #4
# Take in a number from a user input, output the number squared.

user_input = input("Enter a number: ")
number = (user_input)
result = number ** 2

print(result)

# Exercise #5
# Check the below variables' length. 
# If the length of the word is greater than 5 output True, if it is less than 5, output False

words = ["panini", "bulbasaur", "pie", "dolphin", "dog"]

for word in words:
    if len(word) >5:
        print(True)
    else:
        print(False)
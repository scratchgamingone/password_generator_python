#password generator
import random

#lists of letters, numbers and special characters
list_of_lower_letter = ["a","b","c","d","e","f","g","h",
                        "i","j","k","l","m","n","o","p",
                        "q","r","s","t","u","v","w","x",
                                "y","z"]
list_of_upper_letter = ["A","B","C","D","E","F","G","H",
                        "I","J","K","L","M","N","O","P",
                        "Q","R","S","T","U","V","W","X",
                                "Y","Z"]
list_of_numbers = ["1","2","3",
                   "4","5","6",
                   "7","8","9",
                    "0"]
list_of_special_characters = ["!","@","#","$",
                              "%","^","&","*",
                              "(",")","_","-",
                                    "+","="]

#will now ask user to enter in how many letters, numbers and spcecial characters they want
while True:
    try:
        amount_of_lower_letters = int(input("Enter amount of lower letters you want: "))
        if amount_of_lower_letters < 0:
            print("Number cannot be a negative.")
            continue  # ask again
        break  # valid input and non-negative
    except ValueError:
        print("Please enter a valid number.")


while True:
    try:
        amount_of_upper_letters = int(input("Enter amount of upper letters you want: "))
        if amount_of_upper_letters < 0:
            print("Number cannot be a negative.")
            continue  # ask again
        break  # valid input and non-negative
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        amount_of_numbers = int(input("Enter amount of numbers you want: "))
        if amount_of_numbers < 0:
            print("Number cannot be a negative.")
            continue  # ask again
        break  # valid input and non-negative
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        amount_of_special_characters = int(input("Enter amount of special characters you want: "))
        if amount_of_special_characters < 0:
            print("Number cannot be a negative.")
            continue  # ask again
        break  # valid input and non-negative
    except ValueError:
        print("Please enter a valid number.")
lower_letters = random.choices(list_of_lower_letter,k=amount_of_lower_letters)
#print(lower_letters) #debugging
upper_letters = random.choices(list_of_upper_letter,k=amount_of_upper_letters)
#print(upper_letters) #debugging
numbers = random.choices(list_of_numbers,k=amount_of_numbers)
#print(numbers) #debugging
special_characters = random.choices(list_of_special_characters,k=amount_of_special_characters)
#print(special_characters) #debugging


outputted_list_for_password = lower_letters+upper_letters+numbers+special_characters
random.shuffle(outputted_list_for_password) #shuffle the list
shuffled_password_list = outputted_list_for_password
final_password = ''.join(shuffled_password_list)
print("Outputted password:\n",final_password)

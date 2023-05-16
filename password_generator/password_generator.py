import string
import random
import json

def gen_pass(min_len,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    
    character = letters
    if numbers:
        character+= digits
    if special_characters:
        character+= special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    while not meet_criteria or len(pwd) < min_len:
        nc = random.choice(character)
        pwd += nc
        if nc in digits:
            has_number = True
        if nc in special:
            has_special = True
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = has_special and meet_criteria
    return pwd


min_len = int(input("enter the mininum length of your password: "))
has_numbers = input("do you want to include numbers: ").lower() == 'y'
has_specials = input("do you want to include special characters: ").lower() == 'y'
pwd = gen_pass(min_len,has_numbers,has_specials)
print("your genearated password is password is: ",pwd)

# add the generated password to the json file

with open("passwords.json","w") as f:
    json.dump(pwd,f)
    f.close()
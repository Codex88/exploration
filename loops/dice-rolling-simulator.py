from random import randint

roll = "Y"

while roll == "Y":
    print(randint(1, 6))
    roll = input("Would you like to reroll? [Y/N]: ").upper()

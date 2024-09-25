#for outer in range(1, 5):
#    print(outer)
#    for inner in range(1, 5):
#        print("\t", inner)

#for char in "CAT":
#    for x in range(3):
#        print(char)

from random import randint
num_dice = int(input("how many dice are you rolling?:"))
num_sides = int(input("how many sides for each die?:"))

while True:
    result ="|"
    for die in range(num_dice):
        rand = randint(1, num_sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (q to quit)")
    if reply == "q":
        print("Thank you for the game")
        break
   
#for num_dice in range(1,4):
#    print(num_dice)
#for num_sides in range(1,7):
#    print(num_sides)

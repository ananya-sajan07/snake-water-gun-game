import random

# Snake Water Gun game
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Checking for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Checking for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Checking for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

# Converting choices to full words for display
def full_word(letter):
    if letter == 's':
        return "snake"
    elif letter == 'w':
        return "water"
    elif letter == 'g':
        return "gun"

randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
print(f"Computer chose {full_word(comp)}")
print(f"You chose {full_word(you)}")

a = gameWin(comp, you)

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

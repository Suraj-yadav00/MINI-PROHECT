import random
import time
snakes={99:4,70:54,52:40,24:10}#high->low
ladders={6:25,11:45,60:84,46:90}#low->high

def roll_dice():
    return random.randint(1,6)
def move_player(currpos,roll):
    print("You rolled a",roll,"!")
    time.sleep(1)
    currpos += roll

    if currpos in snakes:
        print("Oh no! It's a snake bite! Go back from",currpos,"to",snakes[currpos])
        currpos=snakes[currpos]

    elif currpos in ladders:
        print("Yay Climbed a ladder from",currpos,"to",ladders[currpos])
        currpos=ladders[currpos]
    else: 
        print("Your current position is",currpos)
    return currpos

print("Let's start the Game! Reach position 100 to win")
currpos=0

while currpos < 100:
    user_choice=input("\n Press Enter to roll the dice or type 'q' to quit :").lower()
    if user_choice=="q":
        print("Game Over! Your final position was:",currpos)
        break
    roll=roll_dice()
    currpos=move_player(currpos,roll)
if currpos>=100:
    print("Congratulations! You won")
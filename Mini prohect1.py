import random
target=random.randint(1,100)
while True:
    choice=(input("Enter your choice or Quit(Q):"))
    if(choice=="Q"):
        break
    choice=int(choice)
    if(choice==target):
        print("Congrats! You get it right..")
        break

    elif(choice<target):
        print("Your number is too small,Enter a bigger choice..")


    else:
        print("Your number is too big,Enter a smaller choice..")

    print("GAME OVER !")    
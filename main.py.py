#
import random
'''
1 for snake
 -1 for water
 0 for gun'''
computer = random.choice([ -1,0,1])
youstr = input("Enter your choice : ")
youdict ={"s":1,"w":-1,"g":0}
reversedict ={ 1: "snack", -1: "water", 0:"gun"}

you = youdict[youstr]
#By now we have 2 numbers you and computer
#using reversedict to know  who is chose which number
print(f"you chose:  {reversedict[you]} \ncomputer chose:  {reversedict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1):
        print("You win !")
    
    elif(computer == -1 and you == 0):
        print("you lose !")
    elif(computer == 1 and you == -1):
        print("you lose !")

    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you ==1):
        print("you lose")
    else:
        print("Something went wrong!")
'''
1 for rock
-1 for paper
0 for scissors
'''
import random
 
computer = random.choice([1,-1,0])
you = input("Enter r/p/s")
youdict = {"r" : 1,
           "p" : -1,
           "s" : 0}
younum = youdict[you]
reverse = {1 : "rock",
           -1 : "paper",
           0 : "scissors"}
print(f"Computer Chose \"{reverse[computer]}\" and You chose \"{reverse[younum]}\"")
if(computer == younum):
    print("no one win")
else:
    if(computer == 1 and younum == -1):
        print("comp win")
    elif(computer == 1 and younum == 0):
        print("You won")
    elif(computer == -1 and younum == 1):
        print("comp win")
    elif(computer == -1 and younum == 0):
        print("You won")
    elif(computer == 0 and younum == -1):
        print("comp win")
    elif(computer == 0 and younum == 1):
        print("You won")
    else:
        print("somthing wrong")
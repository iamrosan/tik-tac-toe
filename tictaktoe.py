from os import system, name
from time import sleep

#clearing the screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# sleep(0.2)
clear()


print("""Tic Tak Toe Game!!!!
Before the game start:
turn 1 will be of Player 'O'
turn 2 will be of Player 'X'
""")
# number_used = []
dictt ={
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9
}
count = 0
def check():
    global count
    if dictt[1]==dictt[2]==dictt[3]=="X" or dictt[4]==dictt[5]==dictt[6]=="X" or dictt[7]==dictt[8]==dictt[9]=="X" or dictt[1]==dictt[5]==dictt[9]=="X" or dictt[3]==dictt[5]==dictt[7]=="X" or dictt[1]==dictt[4]==dictt[7]=="X" or dictt[2]==dictt[5]==dictt[8]=="X" or dictt[3]==dictt[6]==dictt[9]=="X":
        print("Player X won !!!!")
        count=1
    if dictt[1]==dictt[2]==dictt[3]=="O" or dictt[4]==dictt[5]==dictt[6]=="O" or dictt[7]==dictt[8]==dictt[9]=="O" or dictt[1]==dictt[5]==dictt[9]=="O" or dictt[3]==dictt[5]==dictt[7]=="O" or dictt[1]==dictt[4]==dictt[7]=="O" or dictt[2]==dictt[5]==dictt[8]=="O" or dictt[3]==dictt[6]==dictt[9]=="O":
        print("Player O won !!!!")
        count = 1

def show(n,ch):
    #clearing the screen
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    # sleep(1)
    clear()
    dictt[n]= ch
    check()
    for i in range(1,10):
        print(dictt[i],end=" ")
        if i%3==0:
            print()
        
    

for i in range(1,10):
    if count==1:
        break
    n=int(input("Enter your choice? "))
    #even for PlayerX
    if i%2==0: 
        show(n,"X")
    #odd for playerO
    else:
        show(n,"O")

if count == 0:
    print("The game is draw.")
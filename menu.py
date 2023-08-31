import random,os
from hangman import gameEngine
'''with open("welcome.txt") as f:
    for i in f:
        print(i,end="")'''
while True:
    os.system("cls" if os.name=='nt' else "clear")
    with open("welcome.txt") as f:
        for i in f:
            print(i,end="")
    print("Enter 1 for Single Player Mode")
    print("Enter 2 for Two Player Mode")
    choice=input()
    if choice=='1':
        with open("wordlist.txt") as f:
            lines=f.readlines()
            word=random.choice(lines).strip()
        gameEngine(word)
    elif choice=='2':
        user_input=input("Enter Secret word ")
        gameEngine(user_input)
    else:
        print("Invalid choice Enter again")

import os
from time import sleep
def gameEngine(secret_word):
    secret_word=secret_word.lower()

    lst1=list(secret_word)

    size=len(lst1)

    lst2=["_" if x!=" " else " " for x in lst1]
   # os.system('cls' if os.name == 'nt' else 'clear')
    #print(" ".join(lst2))

    guessed_letters=[]
    a=10

    while a>0:
        sleep(1.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" ".join(lst2) )
        guess=input('Enter the alphabet : ')
        guess=guess.lower()
        if len(guess)==1 and guess not in guessed_letters:
            guessed_letters.append(guess)
            if(guess in lst1):
                for i in range(0,size):
                    if(secret_word[i]==guess):
                        ind1=i
                        lst2[ind1]=guess
                
                if(lst1==lst2):
                    print("You got it Right")
                    print("""
                    ´´´´´´¶¶¶¶
                    ´´´´´¶´´´´¶¶
                    ´´´´´¶´´´´´¶
                    ´´´´´´¶´´´´¶
                    ´´´´´´¶´´´¶
                    ´´´´¶¶¶¶¶¶¶¶¶¶¶¶
                    ´´´¶´´´´´´´´´´´´¶
                    ´´¶´´´´´´´´´´´´¶
                    ´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶
                    ´¶´´´´´´´´´´´´´´´¶
                    ´¶´´´´´´´´´´´´´´´¶
                    ´´¶´´´¶¶¶¶¶¶¶¶¶¶¶
                    ´´´¶´´´´´´´´´´´¶
                    ´´´´¶¶¶¶¶¶¶¶¶¶¶


                    """)
                    break
            else:
                a=a-1
                print("Try again ",a," tries left")
            
        elif len(guess)!=1:
            print("Enter only one character")
        else:
            print("Letter already Guessed")
            
            
    if(lst1!=lst2):
        print('Better luck next time\nThe word was:',secret_word,"\n\n ¯\_(ツ)_/¯ ")
    sleep(5)
        


import sqlite3
import re


# Connection is made to the database
con=sqlite3.connect('Words.sqlite')
cur=con.cursor()

#Function to print the graphic image of the Hangman based on the number of chances left.
def Hang(count):
    if count==0:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|     _|_')
        print('|      |')
        print("|     / \\")
        print("|")
        print("|")
        print("|____")

    if count==1:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|     _|_')
        print('|      |')
        print("|     / ")
        print("|")
        print("|")
        print("|____")

    if count==2:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|     _|_')
        print('|      |')
        print("|       ")
        print("|")
        print("|")
        print("|____")

    if count==3:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|     _|_')
        print('|       ')
        print("|       ")
        print("|")
        print("|")
        print("|____")

    if count==4:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|     _|')
        print('|       ')
        print("|       ")
        print("|")
        print("|")
        print("|____")

    if count==5:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|      | ')
        print('|       ')
        print("|       ")
        print("|")
        print("|")
        print("|____")

    if count==6:
        print("________")
        print('|/     |')
        print('|     (_)')
        print('|        ')
        print('|       ')
        print("|       ")
        print("|")
        print("|")
        print("|____")

    if count==7:
        print("________")
        print('|/     |')
        print('|       ')
        print('|        ')
        print('|       ')
        print("|       ")
        print("|")
        print("|")
        print("|____")

#Function to decide if the user wants to play again or not.
def PlayAgain():
    chance=input("Do you want to play again? Y or N : ")
    chance=chance.upper()

    if chance=="Y":
        print('\n')
        return "yes"
    elif chance=="N":
        print('\n')
        return "no"
    else:
        print("Please Enter a valid value")
        print('\n')
        PlayAgain()

#Start of the Main Program
#Asks for user to enter the name
name=input("Enter your name: ")

#Print Instructions
print("Welcome",name+".","Instructions for the game: You can enter the values from A-Z. Any other value will be considered invalid. You will get 7 chances to guess the complete word. If you fail to guess in these 7 chances, your friend will Hang.")
print("We wish you All the very Best for the Game")
print("\n")

#Fetch the word from the db.
allwords=cur.execute("Select * from WordList")

#Iterator on the words in the wordlist
for word in allwords:
    cell=word[1]
    cell=cell.upper()
    reqWord=list()
    userinput=list()
    wrongvalues=list()
    count=7

    """
    Create a list of alphabets in the given word and simultaneously add _ symbol in the list
    which stores the corrct values entered by the user
    """

    for letter in cell:
        reqWord.append(letter)
        userinput.append("_")


    # Prints the word letter by letter in a single line
    print("Word:",end=" ")
    for letter in userinput:
        print(letter,end=" ")

    print("\n")

    #Loops till the user have more than 0 chances left.
    while count>0:

        inp=input("Please Enter a character:")
        inp=inp.upper()

        if len(inp)>1 or len(inp)==0:
            print("Please enter a valid value")
            continue

        else:
            #Checks if the letter is actually present in the word to be guessed.
            if inp in reqWord:
                ind=0
                for letter in reqWord:
                    if letter==inp:
                        #Replaves _ with the correct letter in the userinput list.
                        userinput[ind]=inp
                    print(userinput[ind],end=" ")
                    ind=ind+1
                print('\n')

            else:
                print("Sorry, that is a Wrong Letter")
                count=count-1
                Hang(count)
                wrongvalues.append(inp)
                print("List of Wrong Values:",wrongvalues)
                print("Remaining Counts:",count)
                print('\n')

        if reqWord==userinput:
            print("******** Congratulations! You win. ********")
            break

    if count==0:
        Hang(count)
        print("You are out of chances. You Lost the game.")
    print('\n')

    play = PlayAgain()
    if play=="yes":
        continue
    else:
        break


print("********** GAME ENDED **************")

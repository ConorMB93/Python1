'''
******************
*                *
* H A N G M A N  *
*                *
* by Conor Byrne *
*                *
******************
'''

import random

LIVES = 7
correctList = []
wrongList = []
hangmanPic = ['''
     +---+
     |   |
         |
         |
         |
         |
  ========= ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''',  '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  ========= ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  ========= ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  ========= ''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========= ''']



# imorts file of words for dictionary
def wordlist():
    file = "dictionary.rtf"
    with open(file) as f:
        return f.readlines()  # a list


# selects random word
def random_word(myWordList):
    randWord = random.choice(myWordList)
    return randWord

# checks user input is a string
def guessInput(turn):
    while True:
        print("")
        guess = input("Enter your " + turn + " guess. ")

        if len(guess) > 1:
            print("Please enter a single letter!")

        elif len(guess) <= 0:
            print("Please enter a single letter!")

        # test for string
        elif not guess.isalpha():
            print("Please enter a letter ONLY!.")

        else:
            return guess


# guess funtion

def Guess(secretWord):
    positionDict = {1: "st", 2: "nd", 3: "rd"}
    k = 1
    frame = 0
    lives = LIVES

    while True:
        if k in positionDict:
            turn = str(k) + positionDict[k]
        else:
            turn = str(k) + 'th'

        guess = guessInput(turn)

        # if guess is wrong!

        if guess not in secretWord:

            wrongList.append(guess)
            print("WRONG!")
            print("")
            print(hangmanPic[frame])
            print("")
            frame += 1
            lives -= 1
            k += 1


            if lives > 0:
                print("You have", lives, "LIVES remaining.")
                print("Try again.")
            else:

                print("You are out of lives.")
                print("GAME OVER!")
                print("The answer was:", secretWord)
                break
        else:
            correctList.append(guess)
            correctList.sort()
            k += 1
            checkList = []
            for letter in secretWord:
                if letter not in checkList:
                    checkList.append(letter)
            checkList.sort()

            if correctList != checkList:

                if guess in secretWord:
                    print("CORRECT!")
                    print("")
                    tab = ""
                    for i in range(len(secretWord)):
                        if secretWord[i] in correctList:
                            tab += secretWord[i] + " "
                        else:
                            tab += "_ "

                    print("")
                    print(tab)

            else:
                print("YOU WIN!")
                break


def main():
    print("************************")
    print("*                      *")
    print("*    H A N G M A N     *")
    print("*                      *")
    print("************************")
    print("")
    myWordList = wordlist()
    rand = random_word(myWordList)
    # file as added characters that must be removed
    rand = rand[:-2]
    secretWord = rand
    Guess(secretWord)


main()

### FUNCTIONS ###

# checks the number of times a letter appears in a word
def nbLettersInWord(letter, word) :
    nbLetters = 0
    for eachLetter in word :
        if (eachLetter == letter) :
            nbLetters += 1
    return nbLetters

# return the word cut by an index
def cutTheWord(index, word) :
    wordToString = "".join(word)
    return list(wordToString[index+1:len(word)])

###

# the word to guess
theWord = "frigo"
theWord = theWord.upper()
theWord = list(theWord.upper())

# the letters already used
usedLetters = list()

# the usable letters
import string
alphabetList = list(string.ascii_uppercase)
usableLetters = list(string.ascii_uppercase)

# the empty word
emptyWord = ""

for eachLetter in theWord :
    emptyWord += "_ "
emptyWordList = emptyWord.split()

chances = 10

# START OF THE GAME
print("\n\033[1;35mTHE \033[1;36mHANGMAN'S \033[1;33mGAME")

print("\n\n\033[0;34mThis is the word to guess : \n\033[1;37m")
print(emptyWord)
print("\n\033[0;34mYou have \033[1;34m10 chances.")

while (chances > 0) :
    letter = input("\n\033[0;34mEnter a letter : ").upper()

    # check if the letter is in the list of the usable letters
    while (letter not in usableLetters) :

        if (letter not in alphabetList) :
            print("\033[1;31mERROR : You must enter a letter, not a number or a special character.")
        else :
            print("\033[1;30mYou have already used this letter, try another one.")
        letter = input("\n\033[0;34mPlease enter a letter : ").upper()

        # check if the user entered a single letter
        while (len(letter) > 1) :
            print("\033[1;31mERROR : You must enter ONE letter.")
            letter = input("\n\033[0;34mPlease enter ONE letter : ").upper()

    usableLetters.remove(letter)
    usedLetters.append(letter)
    chances -= 1

    # check if the letter is in the word to guess
    letterIndex = list()
    cutWord = list()
    if (letter in theWord) :
        # if YES -> check how many this letter is in this word
        nbOfLetters = nbLettersInWord(letter, theWord)
        # stock (all) the index of the letter in a variable or a list
        if (nbOfLetters > 1) :
            for i in range(nbOfLetters) :
                if (i == 0) :
                    letterIndex.append(theWord.index(letter))
                else :
                    letterIndex.append(cutWord.index(letter) + letterIndex[i-1] + 1) # index of the another letter + index of the previous letter + 1
                if (i < nbOfLetters-1) :
                    cutWord = cutTheWord(letterIndex[i], theWord)
        else :
            letterIndex.append(theWord.index(letter))
        # display of the new word
        for i in range(len(emptyWordList)) :
            if i in letterIndex :
                emptyWordList[i] = theWord[i]
        emptyWord = " ".join(emptyWordList)
        print("\nThis is the right letter ! Look at the word now : \033[1;37m\n")
        print(emptyWord)
    else :
        print("\033[1;30mThis letter is not in this word, try another one.") 
        print("\n\033[0;34mThe word : \033[1;37m\n")  
        print(emptyWord) 
        print()

    # display of the remaining usable letters
    print("\n\033[1;36m" + str(chances) + " chances \033[0;34mleft")
    print("\n\033[0;34mThe letters you've already used :\033[0;37m")
    print(usedLetters)

    if ("".join(emptyWord.split()) == "".join(theWord)) :
        break


emptyWord = emptyWord.split()
emptyWord = "".join(emptyWord)

if (emptyWord == "".join(theWord)) :
    print("\n\033[1;33mYou're right ! \033[0;34mThe word was \033[1;37m" + "".join(theWord))
else :
    print("\n\033[1;35mOh no ! \033[0;34mYou hadn't enough time to find the word...\nThe word was \033[1;37m" + "".join(theWord))
print()
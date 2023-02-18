### FUNCTIONS ###

# checks the number of times a letter appears in a word
def nbLettersInWord(letter, word) :
    nbLetters = 0
    for eachLetter in word :
        if (eachLetter == letter) :
            nbLetters += 1
    return nbLetters

# returns the word cut by an index
def cutTheWord(index, word) :
    wordToString = "".join(word)
    return list(wordToString[index+1:len(word)])

wordList = ["freeze", "table", "cocktail", "camera", "computer", "strawberry", "banana", "three", "forty", "gorgeous", "cat", "dog", "desk", "car", "dance", "foot", "turtle", "french", "spanish", "phone", "eight"]

# returns one word of a list
def randomWord(indexList) :
    import random
    randomNb = random.randint(0, len(wordList)-1)
    while (randomNb in indexList) :
        randomNb = random.randint(0, len(wordList))
    return wordList[randomNb]
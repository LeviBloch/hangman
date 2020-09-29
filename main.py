secretPhrase = "bruh moment"

lettersGuessed = []
correctGuesses = []
incorrectGuesses = []

maxIncorrectGuesses = round(len(secretPhrase) * 1.5)


def printSecretPhrase():
    output = ""

    for letter in secretPhrase:
        if letter in correctGuesses:
            output += letter
        elif letter == " ":
            output += " "
        else:
            output += "_"

    print(output)

# main loop
while len(incorrectGuesses) <= maxIncorrectGuesses:
    printSecretPhrase()
    print("Enter a guess: ")
    guess = input()
    if len(guess) > 1 or len(guess) < 1:
        print ("please guess one letter")
        continue

    guess = guess.lower()

    for letter in secretPhrase:
        if letter == guess:
            correctGuesses.append(guess)

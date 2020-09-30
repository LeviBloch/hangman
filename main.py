from playsound import playsound

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
    print("Incorrect guesses: " + str(incorrectGuesses))
    print("Enter a guess: ")
    guess = input()
    if len(guess) > 1 or len(guess) < 1:
        print ("please guess one letter")
        continue

    guess = guess.lower()

    for letter in secretPhrase:
        if letter == guess:
            correctGuesses.append(guess)
    if guess not in correctGuesses:
        incorrectGuesses.append(guess)
        playsound('C:/Users/Levi/Documents/GitHub/hangman/Wrong3.mp3')



print("god you're terrible at this game, die")
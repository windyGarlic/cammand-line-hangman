import getpass

'''	
Hangman game
Written by: Jordan Swebeck
04/02/2023
'''

global playerWord
global numberOfGuesses
global guesses
global correct
numberOfGuesses = 0
guesses = []
correct = False


def checkLetter():
	global playerLetter
	global playerWord
	global numberOfGuesses
	global correct

	correct = False
	for letters in playerWord:
		if playerLetter == letters:
			correct = True
		if letters in guesses:
			print(letters)
		else:
			print("-")
	if correct == False:
		numberOfGuesses += 1
	if numberOfGuesses == 6:
		print("Game over.\nThe word was:\n" + playerWord)
		input("Press any button to start another game.")
		start()
	print("Guesses: "+str(numberOfGuesses) + "/6")
	guess()


def guess():
 	global playerLetter
 	global guesses
 	
 	print("\nYou can start a new game at anytime by typing 'new'.")
 	playerLetter = input("Player 2 guess: ")
 	guesses.append(playerLetter)
 	if playerLetter == "new":
 		start()
 	print (guesses)
 	checkLetter()


def start():
	global playerWord

	playerWord = getpass.getpass(prompt="\n\nPlayer 1 submit the word you would like to use.\n(Note the password will appear invisible to prevent cheating.)\n:")
	guess()


input("\n\n\n\n\nWelcome to 2 player Hangman. Press any button to get started.\n\n")
start()

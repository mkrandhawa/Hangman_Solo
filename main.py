import random  # this library is needed to choose a random word from the given list
import time  # this library will be used to delay the displaying of the hangman pattern


# this function is for solo game!
def solo(words_list):
    hangman_list = [" \n"
                    " \n"
                    " \n"
                    " \n"
                    " \n"
                    " \n"
                    " \n"
                    "_____\n",
                    "         \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |       \n"
                    "  |        \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |     | \n"
                    "  |        \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    \|/  \n"
                    "  |        \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    \|/  \n"
                    "  |    / \  \n"
                    "__|__\n",
                    "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |    ___ \n"
                    "  |    \|/  \n"
                    "  |    / \  \n"
                    "__|__\n"
                    ]
    word = random.choice(words_list)  # randomly choosing a word from the given list
    word = word.lower()  # converting the chosen word into lowercase
    word_length = len(word)  # calculating the length of the chosen word
    count = 0  # this variable will be used to display the hangman pattern
    a = 0  # this counter will be used to print the hangman pattern from the list
    l1 = []  # list for the letters for the main word
    l2 = []  # list for the letter for of user guess
    guesses_list = []  # this list will store all the guesses
    letter_guessed = ""
    print("_" * word_length)

    while count < 10:
        user_guess = input("Guess the word: ")
        user_guess = user_guess.lower().strip()
        guess_length = len(user_guess)

        if guess_length == 1 or guess_length == word_length:
            # it checks if the letter entered by the user is in the list or not
            # if it is in the list the counter will not be updated and the user will have to insert a different letter
            if user_guess not in guesses_list:
                guesses_list.append(user_guess)  # appending all the letters to the list
                # it first checks if the word that has been entered by the user is same as the one he needs to guess
                if user_guess == word:
                    print("You guessed it right! The secret word was", word)  # it gets printed if it is true if false next line will be executed
                    play_again() # recalling the function play_again to give the user the choice to play again

                # checking if the letter that has been given is in the word
                if user_guess in word:
                    if user_guess in letter_guessed:
                        print("You already guessed that letter! Try again")
                    else:
                        letter_guessed += user_guess  # concatenating the letter to the string)
                else:
                    # if the letter is not in the word the counter increases
                    time.sleep(0.5)
                    print(hangman_list[a])
                    if a == 7:
                        print("Last chance play it carefully!")
                    elif a == 8:
                        print("It is over! You are hanged!!")
                        print("The word was ", word)
                        exit()
                    a = a+1
            else:
                print("You have already used", user_guess, "Try again!")

            # iterating through all the letters in the word to be guessed
            for letter in word:
                # checking if the letter_guessed is not same as the word to be guessed
                if letter in letter_guessed:  # if the letter is part of the letter guessed string
                    print(letter, end="")  # prints all the guessed letters on one line
                else:
                    print("_", end="")  # print the _ instead of the letter. All the dashes will be printed on one line
            # this section will check if the word that has been guessed is same to the one to be guessed
            # if it is same then it will exit otherwise it will continue
            for i in word:
                if i not in l1:
                    l1.append(i)
            for j in letter_guessed:
                if j not in l2:
                    l2.append(j)
            # sorting the list that contains not repeated letters of main word
            l1 = sorted(l1)
            # sorting the list that contains not repeated letters of guessed word
            l2 = sorted(l2)
            if l1 == l2:
                print("\nYou guessed the word! It was", word)
                play_again()
            print("")
        else:
            print("You can enter only a single letter or the full word!")
            count += 1


def play_again():
    user_input = input("Do you want to play again? Y=yes or N=no ")
    user_input = user_input.lower().strip()
    if user_input == "y":
        solo(word_list)
    else:
        exit()


print("********************************************* HANGMAN *************************************************")
print("")
time.sleep(0.75)
print("Are you ready? Let's GOOOOOOOOOO")
print("")
time.sleep(0.75)

word_list = ["Hello", "world","television", "computer", "engineer", "fundamentals", "chemicals", "architecture",
             "python", "algorithm", "negation", "processor", "memory"]
print(solo(word_list))


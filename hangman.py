import random
import time
import sys

f = open("countries_capitals", "r")
lines = f.readlines()

r = random.randint(0,184)
secret_word = lines[r]
secret_word_list = []
secret_word_list_dash = []
not_in_word = []
abc = []
abcdef = []
country = ""
write = False
writecountry = True
for i in secret_word:
    if i == "|":
        write = True
    if write:
        secret_word_list.append(i.upper())
for i in secret_word:
    if i == "|":
        writecountry = False
    if writecountry:
        country += i

for i in secret_word_list:
    if i != "|" and i != " " and i != "\n":
        abc.append(i)
        abcdef.append(i)
        secret_word_list_dash.append("_")


print(secret_word_list_dash)
guesscount = 0
life = 5
print("You have: " + str(life) + " lives! Use them wisely! ")
start_time = time.time()


def hangman0():
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

def hangman1():
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')

def hangman2():
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')

def hangman3():
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')

def hangman4():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')

def hangman5():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

def letter_guess():
    global guesscount
    while secret_word_list_dash != abc and guesscount < life:
        x = input("Enter a letter here: ")
        x = x.upper()
        if x in not_in_word or x in secret_word_list_dash:
            print("\nThis letter was already used! \n")
            letter_guess()
        if x not in abc and (life - guesscount) == 2:
            not_in_word.append(x)
            print("You have " + str(life-guesscount-1) +" life left")
            print("The following letters are no in the secret word" + str(not_in_word))
            print(secret_word_list_dash)
            print("\nHint: The capital of " + country)
            guesscount += 1
            break
        if x not in abc and (life-guesscount) != 2:
            not_in_word.append(x)
            guesscount += 1
            print("You have " + str(life-guesscount) +" lives left")
            print("The following letters are no in the secret word" + str(not_in_word))
            print(secret_word_list_dash)

        while x in abc:
            y = abc.index(x)
            abc[y] = secret_word_list_dash[y]
            secret_word_list_dash[y] = x
            print("The following letters are not in the secret word" + str(not_in_word))
            print(secret_word_list_dash)
        break

def word_guess():
    guessword = input("Enter your guess for the secret word here: ")
    guessword = guessword.upper()
    if guessword == "".join(abcdef):
        print("You win!")
        print("The secret word was the capital of " + secret_word)
        elapsed_time = time.time() - start_time
        print ("\nYou have finished the game in " + str(int(elapsed_time)) + " seconds")
        highscore()
        sys.exit()
    else:
        hangman5()
        print("That's not the secret word! You died! ")
        print("The secret word was the capital of " + secret_word)
        elapsed_time = time.time() - start_time
        print ("\nYou have failed the game in " + str(int(elapsed_time)) + " seconds")
        sys.exit()

def win():
    if secret_word_list_dash == abcdef:
        print("You win! ")
        print("The secret word was the capital of " + secret_word)
        elapsed_time = time.time() - start_time
        print("\nYou have finished the game in " + str(int(elapsed_time)) + " seconds")
        highscore()
        sys.exit()
    if guesscount == life:
        hangman5()
        print("Out of lives. You died")
        print("The secret word was the capital of " + secret_word)
        elapsed_time = time.time() - start_time
        print("\nYou have failed the game in " + str(int(elapsed_time)) + " seconds")
        sys.exit()

def highscore():
    elapsed_time = time.time() - start_time
    x = input("Enter you name here: ")
    y = 0
    l = x + " " + str(int(elapsed_time)) + " seconds!\n"
    f = open("hangmanhighscore.txt", "a+")
    f.write(l)
    f = open("hangmanhighscore.txt", "r")
    print(f.read())
    file = open('hangmanhighscore.txt', "r").readlines()
    scores_tuples = []
    for line in file:
        name, score = line.split()[0], int(line.split()[1])
        scores_tuples.append((name, score))
    scores_tuples.sort(key=lambda t: t[1], reverse=False)
    print("HIGHSCORES\n")
    for i, (name, score) in enumerate(scores_tuples[:5]):
        print("{}. Score:{} - Player:{}".format(i + 1, score, name))
    f.close()

while True:
    if guesscount == 0:
        hangman0()
    guessletter = input("\nWould you like to guess a letter or a word? ")
    if guessletter == "letter":
        letter_guess()
    if guessletter == "word":
        word_guess()
        break
    if guesscount == 1:
        hangman1()
    if guesscount == 2:
        hangman2()
    if guesscount == 3:
        hangman3()
    if guesscount == 4:
        hangman4()
    win()
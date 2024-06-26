import requests, os
from ascii_art import logo, hanged_man

if __name__ == '__main__':
    request = requests.get("https://random-word-api.herokuapp.com/word")
    chosen_word = request.json()[0]
    guess_word = []
    for n in range(len(chosen_word)):
        guess_word.append("_")
    lives = 6
    already_tried = []
    game_over = False

    print(logo)
    print("Where every letter matters.")

    while not game_over:
        guess_letter = ""
        if len(already_tried)>0:
            print("You've already tried: " + ','.join(already_tried))

        while guess_letter == "":
            guess_letter = input("Enter the letter to guess:\n")
        guess_letter = guess_letter[0].lower()
        
        if os.name == 'nt': 
            os.system('cls')
        else:
            os.system('clear')

        if(guess_letter in guess_word):
            print("You already guessed letter " + guess_letter + ".")
        elif(guess_letter in chosen_word):
            for index, char in enumerate(chosen_word):
                if guess_letter == char: guess_word[index] = char
            print("Good guess!")
        else:
            lives -= 1
            print("Letter " + guess_letter + " is not in the word.")
            already_tried.append(guess_letter)

        display = ''.join(guess_word)
        
        game_over = '_' not in guess_word or lives == 0
        print(hanged_man[6-lives])
        print(display)

    if lives == 0: 
        print('You lose!')
        print("The right word was " + chosen_word + "!")
    else: 
        print("You've won!")
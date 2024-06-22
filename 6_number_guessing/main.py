import random, os, art

difficulties = {
    "easy":10,
    "hard":5,
}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def choose_difficulty():
    """
    PLay initial lines and lets the user select the difficulty according to our global dict values.
    """

    print("Welcome to the number guessing name!")
    print("I'm thinking of a number between 1 and 100...")
    diff = ""
    while diff not in ("easy", "hard"):
        diff = input("Choose the difficulty (easy or hard):\n").lower()

    return difficulties[diff]

def compare_guess(guess_num, winner_num):
    """
    Compares guess against winner number, printing according messages and returning the amount of turns to substract.
    """

    if guess_num > winner_num: 
        print("Too high!")
        return 1
    elif guess_num < winner_num: 
        print("Too low!")
        return 1
    
    print(f"Correct! The number I was thinking is {winner_num}!")
    return 0    

def game():
    """
    Main game function.
    """
    
    clear()

    print(art.logo)

    tries = choose_difficulty()
    number = random.randint(1, 100)
    guess = 0
    while guess != number and tries > 0:
        if guess != 0:
            print("Guess again.")

        print(f"You have {tries} attempts to guess the number.")
        
        guess = 0
        while guess <= 0 or guess > 100:
            try:
                guess = int(input("Make a guess: "))
            except ValueError:
                guess = 0

        tries -= compare_guess(guess, number)

    if tries > 0:
        print("Game over! You win.")
    else:
        print(f"Game over! You lose. The number I was thinking is {number}.")

if __name__ == "__main__":
    play_again = "yes"
    while play_again == "yes":
        game()

        play_again = ""
        while play_again not in ("yes", "no"):
            play_again = input("Do you want to play again? (yes/no)\n").lower()
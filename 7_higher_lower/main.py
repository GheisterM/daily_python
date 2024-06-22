import random, os, art
from game_data import data

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_subject(exclude_list):
    """
    Retrieves one new subject excluding the ones on provided list.
    """
    subject = None
    if(len(exclude_list)>0): 
        subject = exclude_list[0]
    else: 
        return random.choice(data)

    while subject in exclude_list:
        subject = random.choice(data)

    return subject

def show_subject(letter, subject):
    """
    Shows subject data, preceded by the option letter.
    """
    print(letter + ": " + subject['name'] + ", a " + subject['description'] + " from " + subject["country"] + ".")

def check_result(subject_a, subject_b, score):
    if(subject_a["follower_count"] > subject_b["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, wrong guess. Final score: {score}")

    return score

def game():
    clear()
    streak = 0
    subjects = {}
    exclusion = []
    playing = True
    subjects["A"] = get_subject(exclusion)
    while playing:
        print(art.logo)
        print(art.compare)
        exclusion.append(subjects["A"])
        show_subject("A", subjects["A"])

        print(art.vs)

        subjects["B"] = get_subject(exclusion)
        exclusion.append(subjects["B"])
        show_subject("B", subjects["B"])

        selection = ""
        while selection not in ("A", "B"):
            selection = input("Who has more followers? (A or B): ").upper()

        opposite = "A" if selection == "B" else "B"
        clear()

        new_score = check_result(subjects[selection], subjects[opposite], streak)
        if new_score == streak:
            playing = False
        else:
            streak = new_score
            # Restart exclusion list and add Subject A to prevent any repeat on next iteration
            exclusion = [subjects["A"]]

            subjects["A"] = subjects["B"]

    return streak

if __name__ == "__main__":
    highest_score = 0
    replay = "yes"
    while replay == "yes":
        new_score = game()
        if new_score > highest_score:
            highest_score = new_score

        replay = ""
        print(f"Highest score: {highest_score}")
        while replay not in ("yes", "no"):
            replay = input (f"Do you want to play again? (yes/no): ").lower()
import random, src, os

card_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
card_types = ["hearts", "diamonds", "spades", "clubs"]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def calculate_total(hand: list, game_finish: bool, source: str, do_print: bool = True):
    values = [x["value"] for x in hand]
    wildcard = 0
    while 'A' in values:
        wildcard += 1
        values.remove('A')
    for special_char in ['J', 'Q', 'K']:
        while special_char in values:
            values.remove(special_char)
            values.append(10)

    total = sum(values)
    if total == 10 and len(values) == 1 and wildcard == 1:
        return 0

    if source == 'You': source = source + " have"
    else: source = source + " has"

    if not game_finish:
        w_line = "." if wildcard == 0 else f" and {wildcard} wildcard(s)."
        if do_print: print(f"{source} {total}" + w_line)
        total += wildcard
    else:
        while wildcard > 0:
            w_value = ""
            if do_print:
                while w_value not in ("1", "11"):
                    w_value = input(f"{source} {wildcard} wildcard(s) left, please select a value for the next one (1 or 11):\n")
            else:
                if total + 11 > 21:
                    w_value = 1
                else:
                    w_value = 11
            total += int(w_value)
            wildcard -= 1
        
    return total

def hand_art(hand: list[dict]):
    final_str = ""
    for line in range (0, 6):
        for card in hand:
            final_str += src.cards_art[card["type"]].format(str(card["value"]).rjust(2)).splitlines()[line]
        final_str += "\n"

    return final_str

def host_art(hand: list[dict]):
    final_str = ""
    for line in range (0, 6):
        final_str += src.cards_art[hand[0]["type"]].format(str(hand[0]["value"]).rjust(2)).splitlines()[line]
        for n in range(1, len(hand)):
            final_str += src.blank_card.splitlines()[line]
        final_str += "\n"

    return final_str

def draw(c_list):
    c_type = random.choice(card_types)
    c_value = random.choice(c_list[c_type])
    result = {"type":c_type, "value":c_value}
    return result

def game():
    card_list = {}
    for t in card_types:
        card_list[t] = card_values[:]
    clear()
    print(src.logo)
    player_cards = []
    host_cards = []
    for n in range(0, 2):
        player_cards.append(draw(card_list))
        card_list[player_cards[-1]["type"]].remove(player_cards[-1]["value"])
        host_cards.append(draw(card_list))
        card_list[host_cards[-1]["type"]].remove(host_cards[-1]["value"])

    game_over = False
    current_total = 0
    host_total = calculate_total(host_cards, game_over, "host", False)
    while not game_over:
        print(hand_art(player_cards))
        current_total = calculate_total(player_cards, game_over, "You")
        print(host_art(host_cards))
        print(f"Host has {host_cards[0]['value']}.")
        if current_total > 21 or current_total == 0 or host_total == 0:
            game_over = True
            break

        answer = ""
        while answer not in ('y', 'n'):
            answer = input("Do you want to draw another card? (y/n)\n")

        if answer == 'y':
            player_cards.append(draw(card_list))
            card_list[player_cards[-1]["type"]].remove(player_cards[-1]["value"])
        else:
            game_over = True

        clear()
    
    if host_total > 0 and current_total > 0:
        while host_total < 17:
            host_cards.append(draw(card_list))
            card_list[host_cards[-1]["type"]].remove(host_cards[-1]["value"])
            host_total = calculate_total(host_cards, False, "host", False)
            print("Host draws another card.")

    if current_total == 0 and host_total == 0:
        print(hand_art(player_cards))
        print(hand_art(host_cards))
        print(f"You both have Blackjack, it's a draw!")
    elif current_total == 0:
        print(hand_art(player_cards))
        print(f"You have Blackjack, you win!")
    elif host_total == 0:
        print(hand_art(player_cards))
        print(hand_art(host_cards))
        print(f"Host has Blackjack, you lose!")
    elif current_total > 21:
        clear()
        print(hand_art(player_cards))
        print(f"You have {current_total}, you lose!")
    else:
        print(hand_art(player_cards))
        current_total = calculate_total(player_cards, game_over, "You")
        print(f"You have {current_total}.")
        print(hand_art(host_cards))
        host_total = calculate_total(host_cards, game_over, "host", False)
        print(f"Host has {host_total}.")
        player_diff = abs(21 - current_total)
        host_diff = abs(21 - host_total)
        if player_diff < host_diff:
            print("You win!")
        elif player_diff > host_diff:
            print("You lose!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    answer = 'y'
    while answer == 'y':
        game()
        answer = ""
        while answer not in ('y', 'n'):
            answer = input("Do you want to play again? (y/n)\n")
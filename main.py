import random

# Global variables
card_list = []
player_dict = {}

def initialize():
    global card_list, player_dict
    card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    player_dict = {}

def initialize_player():

    player_name = ""

    for player_num in range(4):
        if player_num == 0:
            player_name = "Player"
            player_type = 'human'
        else:
            player_name = f"AI {player_num}"
            player_type = 'ai'

        player_dict[player_name] = {
            'card': get_card(2), 
            'pass': False, 
            'boom': False, 
            'score': 0, 
            'player': player_type,
            'five_card_trick': False
        }

        calc_card(player_name)

def get_card(num_cards):
    global card_list
    player_card_list = []

    for _ in range(num_cards):
        if card_list:
            random_index = random.randint(0, len(card_list) - 1)
            player_card_list.append(card_list.pop(random_index))
        else:
            print("No cards left in the deck!")
            break

    return player_card_list

def calc_card(player_name):
    """Calculate the total value of a player's cards and check for Five Card Trick."""
    total = 0
    aces = 0

    # Calculate the score considering the cards
    for card in player_dict[player_name]['card']:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)

    # Handle Ace as 1 or 11
    for _ in range(aces):
        total += 11 if total + 11 <= 21 else 1

    # Check for bust
    if total > 21:
        player_dict[player_name]['score'] = total
        player_dict[player_name]['boom'] = True
    else:
        player_dict[player_name]['score'] = total

    # Check for Five Card Trick
    if len(player_dict[player_name]['card']) == 5 and total <= 21:
        player_dict[player_name]['five_card_trick'] = True
        print(f"Player {player_name} achieved a Five Card Trick!")
    else:
        player_dict[player_name]['five_card_trick'] = False

def ai_round(player_name):
    if player_dict[player_name]['score'] < 17:
        player_dict[player_name]['card'].extend(get_card(1))
        calc_card(player_name)
        if player_dict[player_name]['boom']:
            return True
        return False
    else:
        player_dict[player_name]['pass'] = True
        return True

def get_winner():

    highest_score = 0
    winners = []
    skip = False

    for player_name, player_data in player_dict.items():
        print(f"{player_name} total score: {player_data['score']} card: {player_data['card']}")

        # Prioritize Five Card Trick over score
        if player_data['five_card_trick'] == True and not skip:
            winners = [player_name for player_name, player_data in player_dict.items() if player_data['five_card_trick'] == True]
            skip = True
        elif player_data['score'] > highest_score and player_data['score'] <= 21 and not skip:
            highest_score = player_data['score']
            winners = [player_name]
        elif player_data['score'] == highest_score and player_data['score'] <= 21 and not skip:
            winners.append(player_name)

    if winners:
        print(f"The winner(s): {', '.join(winners)}")
    else:
        print("No winners this round!")

def start_round():
    all_passed = False
    while not all_passed:
        all_passed = True

        for player_name, player_data in player_dict.items():
            
            if not player_data['pass'] and not player_data['boom'] and not len(player_data['card']) == 5:
                if player_data['player'] == 'human':
                    print(f"Player {player_name} cards: {player_data['card']}")
                    choice = input(f"Player {player_name}, do you want to pass? (y/n): ").strip().lower()
                    while choice not in ['y', 'n']:
                        choice = input("Invalid choice. Please enter 'y' or 'n': ").strip().lower()

                    if choice == 'n':
                        player_data['card'].extend(get_card(1))
                        calc_card(player_name)

                        all_passed = False
                    else:
                        player_data['pass'] = True
                else:
                    if not ai_round(player_name):
                        all_passed = False

# Test function to simulate different game scenarios
def test_game_scenarios():
    global card_list, player_dict

    # Scenario 1: Five Card Trick wins
    print("\n--- Scenario 1: Five Card Trick Wins ---")
    initialize()
    player_dict = {
        "Player": {"card": ["2", "3", "4", "5", "6"], "pass": False, "boom": False, "score": 0, "player": "human", "five_card_trick": False},
        "AI 1": {"card": ["K", "Q"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
    }
    for player_name in player_dict:
        calc_card(player_name)
    get_winner()

    # Scenario 2: Normal win by highest score
    print("\n--- Scenario 2: Highest Score Wins ---")
    initialize()
    player_dict = {
        "Player": {"card": ["10", "K"], "pass": False, "boom": False, "score": 0, "player": "human", "five_card_trick": False},
        "AI 1": {"card": ["9", "Q"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
    }
    for player_name in player_dict:
        calc_card(player_name)
    get_winner()

    # Scenario 3: Tie between players
    print("\n--- Scenario 3: Tie ---")
    initialize()
    player_dict = {
        "Player": {"card": ["10", "K"], "pass": False, "boom": False, "score": 0, "player": "human", "five_card_trick": False},
        "AI 1": {"card": ["10", "K"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
    }
    for player_name in player_dict:
        calc_card(player_name)
    get_winner()

    # Scenario 4: Bust (no winners)
    print("\n--- Scenario 4: All Bust ---")
    initialize()
    player_dict = {
        "Player": {"card": ["10", "K", "5"], "pass": False, "boom": False, "score": 0, "player": "human", "five_card_trick": False},
        "AI 1": {"card": ["K", "Q", "3"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
    }
    for player_name in player_dict:
        calc_card(player_name)
    get_winner()

    # Scenario 5: Mixed outcomes (Five Card Trick, highest score, and bust)
    print("\n--- Scenario 5: Mixed Outcomes ---")
    initialize()
    player_dict = {
        "Player": {"card": ["2", "3", "4", "5", "6"], "pass": False, "boom": False, "score": 0, "player": "human", "five_card_trick": False},
        "AI 1": {"card": ["10", "K"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
        "AI 2": {"card": ["10", "K", "5"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
    }
    for player_name in player_dict:
        calc_card(player_name)
    get_winner()

    # Scenario 6: Two Players with Five Card Trick
    print("\n--- Scenario 6: Two Players with Five Card Trick ---")
    initialize()
    player_dict = {
        "Player": {"card": ["2", "3", "4", "5", "6"], "pass": False, "boom": False, "score": 0, "player": "human", "five_card_trick": False},
        "AI 1": {"card": ["10", "K"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
        "AI 2": {"card": ["10", "K", "5"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
        "AI 3": {"card": ["A", "2", "3", "4", "5"], "pass": False, "boom": False, "score": 0, "player": "ai", "five_card_trick": False},
    }
    for player_name in player_dict:
        calc_card(player_name)
    get_winner()

# Run all test scenarios

def main():
    initialize()
    initialize_player()
    start_round()
    get_winner()

if __name__ == "__main__":
    test = False  # Set to True for testing, False for the actual game.
    if test:
        test_game_scenarios()
    else:
        main()
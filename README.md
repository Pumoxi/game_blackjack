# Five Card Blackjack Game

Welcome to the **Five Card Blackjack Game**, a Python-based card game where players compete to score the highest without exceeding 21! This game includes an exciting twist: achieving a *Five Card Trick* (drawing five cards without exceeding 21) can win the game outright.

---

## Features
- **Single Player Mode**: Play as "Player" against AI opponents.
- **AI Opponents**: Three AI players with distinct strategies.
- **Core Mechanics**:
  - Draw cards to get as close to 21 as possible.
  - Avoid busting by exceeding 21.
  - Achieve a *Five Card Trick* for a special win.
- **Multiple Scenarios**: Test game logic with predefined scenarios.
- **Customizable Gameplay**: Adjust settings for testing or gameplay.

---

## How to Play
1. **Start the Game**:
   - Run the script in a Python environment.
   - By default, the game starts in normal mode.
2. **Gameplay**:
   - For human players, choose to "pass" or "draw" a card.
   - AI players decide automatically based on their scores.
   - Round continues until all players either pass, bust, or achieve a *Five Card Trick*.
3. **Win Conditions**:
   - Highest score under or equal to 21 wins.
   - *Five Card Trick* (five cards totaling 21 or less) takes priority.

---

## Requirements
- Python 3.6 or later

---

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:Pumoxi/game_blackjack.git
   ```

2.	Navigate to the project directory:

    ```bash
    cd game_blackjack
    ```

3.	Run the script:

    ```bash
    python main.py
    ```

## Test Mode

Enable **Test Mode** to run predefined game scenarios and validate game mechanics:
1.	Open main.py.
2.	Set the test variable to True:

    ```python
    test = True
    ```

3.	Run the script to see test cases and outcomes.

## File Structure

- main.py: Main game script, includes gameplay logic and test scenarios.

## Acknowledgments

- This game is inspired by classic blackjack, with custom rules for the Five Card Trick twist.
- The development of this project was inspired by course “Master Python by building 100 projects in 100 days”, Dr. Angela Yu.

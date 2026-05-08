"""
------------------------------------------------------------
Guess the Number - Game Logic
------------------------------------------------------------
"""

import random


# Level configuration dictionary.
# Each key is a level number, and each value is a tuple of three things:
#   - low:      the lowest number the player can guess
#   - high:     the highest number the player can guess
#   - attempts: how many guesses the player gets for that level
LEVEL_CONFIG = {
    1:  (1,  10,  5),
    2:  (1,  50,  7),
    3:  (1, 100,  8),
    4:  (1, 150,  9),
    5:  (1, 200, 10),
    6:  (1, 250, 11),
    7:  (1, 300, 12),
    8:  (1, 350, 13),
    9:  (1, 400, 14),
    10: (1, 450, 15),
    11: (1, 500, 16),
}


class GuessTheNumberGame:

    def __init__(self):
        """
        Function description: Sets up the game object with all starting values before the first level begins.
        """

        # Statistics — these track the player's overall performance across all games
        self.total_guesses = 0
        self.total_levels_won = 0
        self.total_invalid = 0
        self.total_games_played = 1

        # Level tracking
        self.current_level = 1

        # carried_attempts stores any leftover guesses from the previous level,
        # which are added as a bonus to the next level's attempt count
        self.carried_attempts = 0
        self.attempts_used = 0

        # The range of numbers for the current level
        self.low = 1
        self.high = 10

        # Attempt limits
        self.base_attempts = 5
        self.max_attempts = 5

        # The number the player is trying to guess
        self.secret_number = 0

    def start_level(self):
        """
        Function description: Loads the settings for the current level and picks a new secret number.
        """

        # Pull the low, high, and base attempt values for this level
        self.low, self.high, self.base_attempts = LEVEL_CONFIG[self.current_level]

        # Add any carried_attempts from the previous level as a bonus on top of the base attempts
        self.max_attempts = self.base_attempts + self.carried_attempts

        # Reset the attempt counter for the new level
        self.attempts_used = 0

        # Pick a random secret number within the level's range
        self.secret_number = random.randint(self.low, self.high)

    def get_hint(self, guess):
        """
        Function description: Works out how close the player's guess is and returns a temperature label and a direction label.
        Inputs/parameters:
            guess: the number the player just guessed, as an integer
        Outputs:
            temperature: a string like "Warm!" or "Super Cold!" showing how close the guess is
            direction: a string of either "Too High" or "Too Low"
        """

        difference = abs(guess - self.secret_number)

        # Express the gap as a percentage of the total range so that thresholds
        # stay fair regardless of how wide the range is — 10 away on Level 1
        # is very different from 10 away on Level 11
        percentage = (difference / self.high) * 100

        # Work out whether the player guessed too high or too low
        if guess > self.secret_number:
            direction = "Too High"
        else:
            direction = "Too Low"

        # Assign a temperature label based on how close the percentage gap is
        if percentage <= 10:
            temperature = "Super Warm!"
        elif percentage <= 20:
            temperature = "Warm!"
        elif percentage <= 30:
            temperature = "Cold!"
        else:
            temperature = "Super Cold!"

        return temperature, direction

    def check_guess(self, raw_guess):
        """
        Function description: Takes the player's raw text input, validates it, checks it against the secret number, and returns a result dictionary describing what happened.
        Inputs/parameters:
            raw_guess: the text the player typed into the input field, as a string
        Outputs:
            result: a dictionary with a "status" key and a "message" key, plus "remaining_attempts" when relevant
        """

        raw_guess = raw_guess.strip()

        # --- Input validation: make sure the input is a whole number ---
        if not raw_guess.lstrip("-").isdigit():

            self.total_invalid += 1

            return {
                "status": "invalid",
                "message": "Ooopsie, not a whole number! Try again."
            }

        guess = int(raw_guess)

        # --- Range check: make sure the number is within the allowed range ---
        if guess < self.low or guess > self.high:

            self.total_invalid += 1

            return {
                "status": "invalid",
                "message": f"Out of range! Enter a number between {self.low} and {self.high}."
            }

        # Count this as a real attempt now that the input is valid
        self.attempts_used += 1
        self.total_guesses += 1

        # --- Correct guess ---
        if guess == self.secret_number:

            remaining_attempts = self.get_remaining_attempts()

            # carried_attempts carries any leftover guesses into the next level
            # so the player is rewarded for guessing efficiently
            self.carried_attempts = remaining_attempts

            self.total_levels_won += 1

            # Handle the special case where the player just beat the final level
            if self.current_level == 11:

                return {
                    "status": "game_completed",
                    "message": (
                        f"The number was {self.secret_number}.\n\n"
                        f"You beat all 11 levels!"
                    )
                }

            # Normal level win
            return {
                "status": "level_won",
                "message": (
                    f"The number was {self.secret_number}.\n\n"
                    f"You carry over {remaining_attempts} attempt(s)!"
                )
            }

        # --- Wrong guess: check how many attempts are left ---
        remaining_attempts = self.get_remaining_attempts()

        # No attempts left — game over
        if remaining_attempts == 0:

            # Reset carried_attempts so the next game starts fresh
            self.carried_attempts = 0

            return {
                "status": "game_over",
                "message": (
                    f"The number was {self.secret_number}.\n\n"
                    "Game over."
                )
            }

        # Player still has attempts remaining — give them a hint
        temperature, direction = self.get_hint(guess)

        return {
            "status": "wrong",
            "message": f"Not quite!\n{temperature} | {direction}",
            "remaining_attempts": remaining_attempts
        }

    def go_to_next_level(self):
        """
        Function description: Moves the game forward by one level and starts it.
        """

        self.current_level += 1
        self.start_level()

    def reset_game(self):
        """
        Function description: Resets everything back to Level 1 for a fresh game, while adding one to the games played counter.
        """

        self.current_level = 1

        # Clear carried_attempts so the new game starts without any bonus attempts
        self.carried_attempts = 0
        self.attempts_used = 0

        # Reset per-game stats but keep the games played count going
        self.total_guesses = 0
        self.total_levels_won = 0
        self.total_invalid = 0

        self.total_games_played += 1

        self.start_level()

    def get_remaining_attempts(self):
        """
        Function description: Calculates and returns how many attempts the player has left in the current level.
        Outputs:
            remaining: the number of attempts still available, as an integer
        """

        return self.max_attempts - self.attempts_used

    def get_stats(self):
        """
        Function description: Collects and returns the player's overall statistics as a dictionary.
        Outputs:
            stats: a dictionary containing levels completed, total guesses, invalid inputs, games played, and current carried attempts
        """

        return {
            "levels_completed": self.total_levels_won,
            "total_guesses": self.total_guesses,
            "invalid_inputs": self.total_invalid,
            "games_played": self.total_games_played,
            "current_carried_attempts": self.carried_attempts
        }

    def get_level_info(self):
        """
        Function description: Collects and returns details about the current level as a dictionary.
        Outputs:
            level_info: a dictionary with the level number, number range, attempt limits, and remaining attempts
        """

        return {
            "current_level": self.current_level,
            "low": self.low,
            "high": self.high,
            "max_attempts": self.max_attempts,
            "attempts_used": self.attempts_used,
            "remaining_attempts": self.get_remaining_attempts()
        }

    def get_debug_answer(self):
        """
        Function description: Returns the secret number for testing purposes so developers can verify the game is working correctly.
        Outputs:
            secret_number: the hidden number the player is trying to guess, as an integer
        """

        return self.secret_number

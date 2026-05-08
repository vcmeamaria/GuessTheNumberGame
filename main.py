"""
------------------------------------------------------------
Guess the Number - Main
------------------------------------------------------------

This is the starting point of the application.
It creates the game logic and GUI objects, then launches the game window.

"""

# Import the game logic class
from game_logic import GuessTheNumberGame

# Import the window/app class
from gui import GuessTheNumberGUI


def main():
    """
    Function description: Creates the game and GUI objects and starts the main application window.
    """

    # Create the game logic object
    game = GuessTheNumberGame()

    # Create the GUI object, passing in the game so the two can communicate
    app = GuessTheNumberGUI(game)

    # Start the game window and keep it open
    app.run()


# Only run main() when this file is executed directly, not when it is imported
if __name__ == "__main__":
    main()

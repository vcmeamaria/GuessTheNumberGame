"""
------------------------------------------------------------
Guess the Number - Graphical User Interface
------------------------------------------------------------

This module builds and manages the Tkinter game window
handles all screens the player sees, such as welcome, instructions, gameplay, level results, and stats, and passes player input
through to the game logic.

"""

import tkinter as tk
from tkinter import messagebox

from sound_manager import play_sound


class GuessTheNumberGUI:

    def __init__(self, game):
        """
        Function description: Sets up the main game window and shows the welcome screen.
        Inputs/parameters:
            game: a GuessTheNumberGame object that handles all the game logic
        """

        self.game = game

        self.window = tk.Tk()
        self.window.title("Guess the Number Game")
        self.window.geometry("650x700")
        self.window.configure(bg="#bfcfee")

        # These are set later when the game screen is built
        self.title_label = None
        self.attempts_label = None
        self.guess_entry = None
        self.message_label = None
        self.debug_label = None

        # Allow the player to submit a guess by pressing Enter
        self.window.bind("<Return>", lambda event: self.check_guess())

        self.show_welcome_screen()

    def run(self):
        """
        Function description: Starts the Tkinter event loop and keeps the window open until the player closes it.
        """

        self.window.mainloop()

    def clear_window(self):
        """
        Function description: Removes all widgets from the window so a new screen can be drawn cleanly.
        """

        for widget in self.window.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        """
        Function description: Draws the welcome screen with the game title and a button to start.
        """

        self.clear_window()

        title = tk.Label(
            self.window,
            text="WELCOME TO\nGUESS THE NUMBER GAME",
            font=("Serif", 26, "bold"),
            bg="#bfcfee",
            justify="center"
        )
        title.pack(pady=100)

        subtitle = tk.Label(
            self.window,
            text="Can you beat all 11 levels?",
            font=("Serif", 15),
            bg="#bfcfee"
        )
        subtitle.pack(pady=10)

        play_button = tk.Button(
            self.window,
            text="PLAY",
            font=("Serif", 16, "bold"),
            width=15,
            height=2,
            command=self.show_instructions_screen
        )
        play_button.pack(pady=40)

    def show_instructions_screen(self):
        """
        Function description: Draws the instructions screen using static labels so all content fits on one page with no scrolling.
        """

        self.clear_window()

        title = tk.Label(
            self.window,
            text="GAME INSTRUCTIONS",
            font=("Serif", 24, "bold"),
            bg="#bfcfee"
        )
        title.pack(pady=(20, 8))

        #  Intro 
        tk.Label(
            self.window,
            text="This game contains 11 difficulty levels.",
            font=("Serif", 12, "bold"),
            bg="#bfcfee"
        ).pack(anchor="w", padx=80)

        tk.Label(self.window, text="", bg="#bfcfee", height=0).pack()

        # ---- In each level ----
        tk.Label(
            self.window,
            text="In each level:",
            font=("Serif", 12, "bold"),
            bg="#bfcfee"
        ).pack(anchor="w", padx=80)

        for line in [
            "- The computer chooses a secret number.",
            "- Guess it before you run out of attempts.",
            "- The number range gets bigger as levels increase.",
            "- You will receive hints after each wrong guess.",
        ]:
            tk.Label(
                self.window,
                text=line,
                font=("Serif", 12),
                bg="#bfcfee"
            ).pack(anchor="w", padx=100)

        tk.Label(self.window, text="", bg="#bfcfee", height=0).pack()

        # ---- Hints ----
        tk.Label(
            self.window,
            text="Hints will tell you:",
            font=("Serif", 12, "bold"),
            bg="#bfcfee"
        ).pack(anchor="w", padx=80)

        for line in [
            "- If your guess is too high or too low.",
            "- If you are warm, cold, super warm, or super cold.",
        ]:
            tk.Label(
                self.window,
                text=line,
                font=("Serif", 12),
                bg="#bfcfee"
            ).pack(anchor="w", padx=100)

        tk.Label(self.window, text="", bg="#bfcfee", height=0).pack()

        # ---- Carry-over rule ----
        tk.Label(
            self.window,
            text="Attempt carry-over rule:",
            font=("Serif", 12, "bold"),
            bg="#bfcfee"
        ).pack(anchor="w", padx=80)

        tk.Label(
            self.window,
            text="If you complete a level with attempts left over, those\nremaining attempts are added to the next level.",
            font=("Serif", 12),
            bg="#bfcfee",
            justify="left"
        ).pack(anchor="w", padx=100)

        tk.Label(self.window, text="", bg="#bfcfee", height=0).pack()

        # ---- Input rule ----
        tk.Label(
            self.window,
            text="Important input rule:",
            font=("Serif", 12, "bold"),
            bg="#bfcfee"
        ).pack(anchor="w", padx=80)

        tk.Label(
            self.window,
            text="- Only whole integer numbers are valid.",
            font=("Serif", 12),
            bg="#bfcfee"
        ).pack(anchor="w", padx=100)

        tk.Label(self.window, text="", bg="#bfcfee", height=0).pack()

        # ---- Examples ----
        tk.Label(
            self.window,
            text="Examples:",
            font=("Serif", 12, "bold"),
            bg="#bfcfee"
        ).pack(anchor="w", padx=80)

        for line in [
            "✅  5          (valid)",
            "❌  5.5       (not valid)",
            "❌  'five'     (not valid)",
        ]:
            tk.Label(
                self.window,
                text=line,
                font=("Serif", 12),
                bg="#bfcfee"
            ).pack(anchor="w", padx=100)

        tk.Label(self.window, text="", bg="#bfcfee", height=0).pack()

        ready_button = tk.Button(
            self.window,
            text="READY TO PLAY!",
            font=("Serif", 14, "bold"),
            width=20,
            height=2,
            command=self.show_game_screen
        )
        ready_button.pack(pady=15)

    def show_game_screen(self):
        """
        Function description: Draws the main gameplay screen for the current level, including the number range, attempt counter, input field, and hint area.
        """

        self.clear_window()
        self.game.start_level()

        level_info = self.game.get_level_info()

        game_title = tk.Label(
            self.window,
            text="GUESS THE NUMBER GAME",
            font=("Serif", 20, "bold"),
            bg="#bfcfee"
        )
        game_title.pack(pady=25)

        self.title_label = tk.Label(
            self.window,
            text=f"LEVEL {level_info['current_level']}",
            font=("Serif", 22, "bold"),
            bg="#bfcfee"
        )
        self.title_label.pack(pady=15)

        range_frame = tk.Frame(self.window, bg="#bfcfee")
        range_frame.pack(pady=5)

        tk.Label(
            range_frame,
            text="Guess a number between ",
            font=("Serif", 13),
            bg="#bfcfee"
        ).pack(side="left")

        tk.Label(
            range_frame,
            text=str(level_info["low"]),
            font=("Serif", 13, "bold"),
            bg="#bfcfee"
        ).pack(side="left")

        tk.Label(
            range_frame,
            text=" and ",
            font=("Serif", 13),
            bg="#bfcfee"
        ).pack(side="left")

        tk.Label(
            range_frame,
            text=str(level_info["high"]),
            font=("Serif", 13, "bold"),
            bg="#bfcfee"
        ).pack(side="left")

        self.attempts_label = tk.Label(
            self.window,
            text=f"Attempts: {level_info['max_attempts']}",
            font=("Serif", 12),
            bg="#bfcfee"
        )
        self.attempts_label.pack(pady=5)

        prompt_label = tk.Label(
            self.window,
            text="Enter your guess",
            font=("Serif", 12),
            bg="#bfcfee"
        )
        prompt_label.pack(pady=(20, 5))

        self.guess_entry = tk.Entry(
            self.window,
            font=("Serif", 14),
            justify="center"
        )
        self.guess_entry.pack(pady=5)

        submit_button = tk.Button(
            self.window,
            text="Submit Guess",
            font=("Serif", 12, "bold"),
            command=self.check_guess
        )
        submit_button.pack(pady=15)

        self.message_label = tk.Label(
            self.window,
            text="",
            font=("Serif", 12),
            bg="#bfcfee",
            wraplength=500,
            justify="center"
        )
        self.message_label.pack(pady=20)

        stats_button = tk.Button(
            self.window,
            text="Show Stats",
            font=("Serif", 10),
            command=self.show_stats
        )
        stats_button.pack(pady=5)

        # The debug label is invisible until the player hovers over it —
        # it is only here to help with testing and is not meant for players
        self.debug_label = tk.Label(
            self.window,
            text="Hover here for debug answer",
            font=("Serif", 8),
            bg="#bfcfee",
            fg="#bfcfee"
        )
        self.debug_label.pack(side="bottom", pady=10)

        self.debug_label.bind("<Enter>", self.show_debug_answer)
        self.debug_label.bind("<Leave>", self.hide_debug_answer)

        self.guess_entry.focus()

    def check_guess(self):
        """
        Function description: Reads the player's input from the entry field, passes it to the game logic, and updates the screen based on the result.
        """

        raw_guess = self.guess_entry.get()
        result = self.game.check_guess(raw_guess)

        status = result["status"]

        if status == "invalid":
            play_sound("invalid")
            self.message_label.config(text=result["message"])
            self.guess_entry.delete(0, tk.END)
            return

        if status == "wrong":
            play_sound("wrong")
            self.attempts_label.config(
                text=f"Attempts: {result['remaining_attempts']}"
            )
            self.message_label.config(text=result["message"])
            self.guess_entry.delete(0, tk.END)
            return

        if status == "level_won":
            play_sound("success")
            self.show_level_result_screen(
                won=True,
                title="Correct!!!",
                message=result["message"]
            )
            return

        if status == "game_completed":
            play_sound("victory")
            self.show_level_result_screen(
                won=True,
                title="CONGRATULATIONS",
                message=result["message"]
            )
            return

        if status == "game_over":
            play_sound("game_over")
            self.show_level_result_screen(
                won=False,
                title="Out of attempts!!!",
                message=result["message"]
            )
            return

    def show_level_result_screen(self, won, title, message):
        """
        Function description: Draws the screen shown after a level ends, with different layouts for a win, a loss, and completing the final level.
        Inputs/parameters:
            won: a boolean that is True if the player guessed correctly and False if they ran out of attempts
            title: a string displayed as the large heading on the result screen
            message: a string with extra detail shown below the heading, such as what the secret number was
        """

        self.clear_window()

        # Special screen for completing all 11 levels
        if won and self.game.current_level == 11:

            final_title = tk.Label(
                self.window,
                text="CONGRATULATIONS",
                font=("Serif", 30, "bold"),
                bg="#bfcfee"
            )
            final_title.pack(pady=(100, 25))

            final_message = tk.Label(
                self.window,
                text="YOU BEAT ALL 11 LEVELS!!\nYOU ARE A LEGEND! 🤩",
                font=("Serif", 20, "bold"),
                bg="#bfcfee",
                justify="center"
            )
            final_message.pack(pady=30)

            stats_button = tk.Button(
                self.window,
                text="SHOW STATS",
                font=("Serif", 16, "bold"),
                width=20,
                height=2,
                command=self.show_stats
            )
            stats_button.pack(pady=30)

            play_again_button = tk.Button(
                self.window,
                text="Play Again",
                font=("Serif", 11),
                width=14,
                command=self.reset_game
            )
            play_again_button.pack(pady=10)

        else:

            result_title = tk.Label(
                self.window,
                text=title,
                font=("Serif", 26, "bold"),
                bg="#bfcfee"
            )
            result_title.pack(pady=80)

            result_message = tk.Label(
                self.window,
                text=message,
                font=("Serif", 14),
                bg="#bfcfee",
                justify="center"
            )
            result_message.pack(pady=20)

            if won:

                next_button = tk.Button(
                    self.window,
                    text=f"NEXT LEVEL {self.game.current_level + 1}",
                    font=("Serif", 14, "bold"),
                    width=20,
                    height=2,
                    command=self.go_to_next_level
                )
                next_button.pack(pady=30)

            else:

                play_again_button = tk.Button(
                    self.window,
                    text="PLAY AGAIN",
                    font=("Serif", 14, "bold"),
                    width=20,
                    height=2,
                    command=self.reset_game
                )
                play_again_button.pack(pady=30)

            stats_button = tk.Button(
                self.window,
                text="Show Stats",
                font=("Serif", 10),
                command=self.show_stats
            )
            stats_button.pack(pady=10)

    def go_to_next_level(self):
        """
        Function description: Tells the game logic to advance to the next level, then redraws the game screen.
        """

        self.game.go_to_next_level()
        self.show_game_screen()

    def show_stats(self):
        """
        Function description: Fetches the player's statistics from the game logic and displays them in a pop-up message box.
        """

        stats = self.game.get_stats()

        stats_message = (
            f"YOUR STATS:\n\n"
            f"Levels completed: {stats['levels_completed']}\n"
            f"Total guesses: {stats['total_guesses']}\n"
            f"Invalid inputs: {stats['invalid_inputs']}\n"
            f"Games played: {stats['games_played']}\n"
            f"Current carried attempts: {stats['current_carried_attempts']}"
        )

        messagebox.showinfo("Game Stats", stats_message)

    def reset_game(self):
        """
        Function description: Resets the game logic back to the beginning and takes the player back to the welcome screen.
        """

        self.game.reset_game()
        self.show_welcome_screen()

    def show_debug_answer(self, event):
        """
        Function description: Reveals the secret number in the debug label when the player hovers over it — used during testing only.
        Inputs/parameters:
            event: the mouse hover event passed in automatically by Tkinter
        """

        self.debug_label.config(
            text=f"Correct number: {self.game.get_debug_answer()}",
            fg="black"
        )

    def hide_debug_answer(self, event):
        """
        Function description: Hides the secret number again when the player moves the mouse away from the debug label.
        Inputs/parameters:
            event: the mouse leave event passed in automatically by Tkinter
        """

        self.debug_label.config(
            text="Hover here for debug answer",
            fg="#bfcfee"
        )

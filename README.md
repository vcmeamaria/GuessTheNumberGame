# Guess the Number Game

A GUI-based number guessing game built with Python and Tkinter. Work your way through 11 progressively harder levels, collect hints, and carry your leftover attempts forward as a reward for guessing efficiently.

---

## 1. How to Run the Game

### Requirements

- **Python 3.x** (developed on Python 3.12)
- **tkinter** - used for the graphical interface. This comes bundled with most Python installations. If it's missing, install it via your package manager.
- **winsound** - used for sound effects. This is a built-in Windows library and requires no installation. The game is designed to run on **Windows**.

### Downloading the Project

Clone the repository using Git:

```bash
git clone https://github.com/vcmeamaria/GuessTheNumberGame.git

```

Or download it as a ZIP from GitHub and extract it somewhere on your machine.

### Running the Game

Navigate to the project folder and run:

```bash
python main.py
```

That's it - the game window will open straight away.

### Sound Effects (assets folder)

The game expects a folder called `assets/` in the same directory as `main.py`, containing these four `.wav` files:

```
assets/
|--- error.wav
|--- game-over.wav
|--- success.wav
|--- victory.wav
```

If the folder or files are missing, the game will still run fine - it just falls back to a default system beep instead of the custom sounds.

---

## 2. How to Play

### What Is This Game?

The computer secretly picks a number, and your job is to guess it before you run out of attempts. Get it right and you move on to the next level. Run out of guesses and it's game over.

### The 11 Levels

The game has 11 levels. Each one increases the range of possible numbers, which makes guessing harder. The number of attempts you're given also scales up to keep things fair:

| Level | Range   | Base Attempts |
|-------|---------|---------------|
| 1     | 1–10    | 5             |
| 2     | 1–50    | 7             |
| 3     | 1–100   | 8             |
| 4     | 1–150   | 9             |
| 5     | 1–200   | 10            |
| 6     | 1–250   | 11            |
| 7     | 1–300   | 12            |
| 8     | 1–350   | 13            |
| 9     | 1–400   | 14            |
| 10    | 1–450   | 15            |
| 11    | 1–500   | 16            |

### Making a Guess

Type any whole number into the input field and press **Submit Guess** or hit **Enter**. The game will tell you whether you got it right, give you a hint, or let you know you've run out of attempts.

### The Hint System

After every wrong guess you get two hints:

- **Direction** — tells you whether your guess was `Too High` or `Too Low`.
- **Temperature** — tells you how close you are, based on how far off your guess is as a percentage of the total range:

| Temperature   | How close you are         |
|---------------|---------------------------|
|  Super Warm | Within 10% of the range   |
|  Warm        | Within 20% of the range   |
|  Cold        | Within 30% of the range   |
|  Super Cold  | More than 30% off         |

Using percentage rather than a fixed gap means the hints stay useful across all levels - being 30 away means something very different on Level 1 (range of 10) versus Level 11 (range of 500).

### Carried Attempts

If you guess the number correctly and still have attempts left over, those spare attempts are added as a **bonus** on top of the next level's base attempts. For example, if you finish a level with 3 attempts to spare, the next level starts with its usual allowance **plus 3**.

This rewards efficient guessing and gives you a bit of a buffer heading into harder levels.

### Valid and Invalid Inputs

Only **whole integers** are accepted. Anything else will trigger an error message and won't count as an attempt.

| Input  | Valid? |
|--------|--------|
| `7`    |  Yes |
| `5.5`  |  No  |
| `five` |  No  |
| `-3`   |  No (out of range) |

---



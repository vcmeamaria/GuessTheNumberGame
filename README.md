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

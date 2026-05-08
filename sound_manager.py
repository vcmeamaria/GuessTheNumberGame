"""
------------------------------------------------------------
Guess the Number - Sound Manager
------------------------------------------------------------
"""

import os
import winsound


# Maps game event names to their corresponding .wav audio files
SOUND_FILES = {
    "invalid": "assets/error.wav",
    "wrong": "assets/error.wav",
    "game_over": "assets/game-over.wav",
    "success": "assets/success.wav",
    "victory": "assets/victory.wav",
}


def play_sound(sound_name):
    """
    Function description: Plays the audio file linked to a game event, or falls back to a system beep if the file is missing.
    Inputs/parameters:
        sound_name: a string key that matches one of the entries in SOUND_FILES, e.g. "success" or "game_over"
    """

    # Look up the file path for the requested sound
    file_name = SOUND_FILES.get(sound_name)

    # Play the sound file if it exists on disk
    if file_name and os.path.exists(file_name):
        winsound.PlaySound(file_name, winsound.SND_FILENAME | winsound.SND_ASYNC)

    # Fall back to the default system beep if the file cannot be found
    else:
        winsound.MessageBeep(winsound.MB_OK)

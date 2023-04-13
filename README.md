# Carillon 404 Player
A goofy little carillon player for oakland.edu's 404 page!

## Installation
1. Download the .zip at https://github.com/ElijahTyler/Carillon-404-Player.git
2. Extract the .zip file wherever you prefer
3. Open Terminal in the project directory and type `python -m pip install -r requirements.txt`
4. Download geckodriver at https://github.com/mozilla/geckodriver/releases
5. move the `geckodriver` (Linux) or `geckodriver.exe` (Windows) file into the project directory

### Features
- Play a default bell chime : You can play a default bell chime by passing no arguments when you run the file.

- Write your own song : By passing the `--write` argument, you can write your own song to play! Use the 'cdefgabC.x' characters to write your song, and then set the BPM between 1 and 200.
  - 'cdefgabC' covers one full C major scale
  - '.' is one note of rest
  - 'x' cuts the song short without letting the last bell ring out

Before playing, you are asked if you'd like to save your song into the song bank. You're also able to overwrite songs by using the same song name. The song string will then be parsed into playable notes.

- Play songs from the song bank : By passing the `--bank` argument, you can play songs you've previously saved. You're presented with a list of all songs from the bank, and simply select a song number to play.

### Run
1. Open Terminal in the project directory and type `python carillon.py [--write|--bank|--help]`
2. ???
3. profit

Have fun! There's no limit to the song length or the number of songs in the bank, so feel free to go absolutely monkey with this!

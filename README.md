# Carillon 404 Player
A goofy little carillon player for oakland.edu's 404 page!

# A little about Elliott Tower

Oakland University is home to Elliott Tower, a 151-foot carillon tower completed in 2014. It hosts 49 bells, ranging a full 4 octaves from C2 to C6. This clock tower is a staple of the ambient sound of Oakland's campus, ringing on every quarter hour. Oakland University offers a carillon class, where students may learn to play the carillon in the tower. For those of us without the schedule space to take the class, however, Oakland's 404 page on the oakland.edu website offers a chance to play the carillon from the convenience of our screen. We are graced with a full diatonic C scale ranging from C3-C4.

## Installation
1. Download the .zip at https://github.com/ElijahTyler/Carillon-404-Player.git
2. Extract the .zip file wherever you prefer
3. Open Terminal in the project directory and type `python -m pip install -r requirements.txt`
4. Download geckodriver at https://github.com/mozilla/geckodriver/releases
5. Move the `geckodriver` (Linux) or `geckodriver.exe` (Windows) file into the project directory

### Features
- Play a default bell chime : You can play a default bell chime by passing no arguments when you run the file.

- Write your own song : By passing the `--write` argument, you can write your own song to play! Use the 'cdefgabC.x' characters to write your song, and then set the BPM between 1 and 200.
  - 'cdefgabC' covers one full C major scale
  - '.' is one beat of rest
  - ',' is a half beat of rest
  - 'x' cuts the song short without letting the last bell ring out

Before playing, you are asked if you'd like to save your song into the song bank. You're also able to overwrite songs by using the same song name. The song string will then be parsed into playable notes.

- Play songs from the song bank : By passing the `--bank` argument, you can play songs you've previously saved. You're presented with a list of all songs from the bank, and simply select a song number to play.

### Run
1. Open Terminal in the project directory and type `python carillon.py [--write|--bank|--help]`
2. ???
3. profit

Have fun! There's no limit to the song length or the number of songs in the bank, so feel free to go absolutely monkey with this!

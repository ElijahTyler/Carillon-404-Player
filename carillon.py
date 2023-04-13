from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import os, sys, json
from sys import platform
import time

maindir = os.path.dirname(os.path.abspath(__file__))


def init_firefox(headless=False):
    opts = FirefoxOptions()
    if headless:
        opts.add_argument("--headless")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--start-maximized")

    if platform == "win32":
        opts.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver_executable = os.path.join(maindir, 'geckodriver.exe')
    elif platform == "linux" or platform == "linux2":
        driver_executable = os.path.join(maindir, 'geckodriver')
    driver = webdriver.Firefox(options = opts, executable_path = driver_executable)
    return driver

def main(song_string="gbad.gabg", bpm=60): # it's 0 o'clock somewhere in the world
    print("Loading Firefox...")
    driver = init_firefox(headless=False)
    print("Loading website...")
    driver.get("https://www.oakland.edu/playmesomebells")
    print("Bells being prepared to play...")

    # find bells on webpage and set keys to each
    driver.execute_script("window.scrollTo(0, 600)")
    bells = driver.find_elements(By.CLASS_NAME, "carillonBellImage")
    letters = ['c','d','e','f','g','a','b','C']

    # compile the "keyboard" for song_string to play
    # (this little app is just a player piano, but instead
    # of having a piano you have Oakland's bells, and instead
    # of a piano roll you get to type the text)
    play_note = {}
    for i in range(8):
        play_note[letters[i]] = bells[i]

    action = ActionChains(driver)
    print(f"Playing song string {song_string}...")
    for letter in song_string:
        if letter == '.':
            time.sleep(0.3)
        elif letter == ',':
            time.sleep(0.15)
        elif letter == 'x':
            driver.close()
            quit()
        else:
            action.click(play_note[letter]).perform()
        time.sleep(60/bpm - 0.3)
    
    time.sleep(3.5) # let the bells ring out before the window closes
    driver.close()

if __name__ == "__main__":
    print(f"\n{'CARILLON BELL PLAYER':-^60}")
    print(f"{'by Eli Sepulveda':-^60}")

    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '--write':
                # dudes will be like "this song sucks"
                # bruh you wrote the string :skull:
                song_string = input("Enter song string: ")

                print("Set bpm within the bounds (0, 200]")
                bpm = int(input("Enter BPM: "))

                print("Save song to song bank? (y/n)")
                if input().lower() == 'y':
                    with open('bank.json', 'r') as f:
                        bank = json.load(f)
                    song_name = input("Enter song name: ")
                    if song_name not in bank.keys():
                        bank[song_name] = {'song_string': song_string, 'bpm': bpm}
                        with open('bank.json', 'w') as f:
                            json.dump(bank, f, indent=4)
                    else:
                        print("Song already exists in bank! Overwrite? (y/n)")
                        if input().lower() == 'y':
                            bank[song_name] = {'song_string': song_string, 'bpm': bpm}
                            with open('bank.json', 'w') as f:
                                json.dump(bank, f, indent=4)

                main(song_string, bpm)

            case '--bank':
                print("Select a song from the song bank!")
                with open('bank.json', 'r') as f:
                    bank = json.load(f)
                for i, song in list(enumerate(bank.keys())):
                    print(f"{i+1}. {song}")
                song_name = list(bank.keys())[int(input("Enter song number: "))-1]
                main(bank[song_name]['song_string'], bank[song_name]['bpm'])
            
            case '--help':
                print("Usage: python carillon.py [--write|--bank|--help]")
                print("  --write: write a song and play it")
                print("  --bank: play a song from the song bank")
                print("  --help: show this help message")

    else:
        main()

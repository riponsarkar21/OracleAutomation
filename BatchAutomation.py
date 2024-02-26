### #Check On Hand Details Report



import pyautogui as pg
import time
import subprocess

userName = "5638"
password = "ripon"


#Open dedicated Browser

firefox_shortcut_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Mozilla Firefox.lnk"

def open_firefox_dedicated_browser(shortcut_path):
    try:
        subprocess.Popen([shortcut_path], shell=True)
        print("Mozilla Firefox is now opening...")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
open_firefox_dedicated_browser(firefox_shortcut_path)


#Load The webpage
time.sleep (8)

# Login the website
pg.write (userName)
pg.press ("tab")
pg.write (password)
pg.press ("tab")
pg.press ("enter")

# Wait for the page to load 
time.sleep(2)

# Select the web element for opening oracle software for creating batch
pg.press ("tab", presses = 14)
pg.press ("enter")
time.sleep (1)
pg.press ("tab", presses = 3)
pg.press ("enter")



# Wait for the software download 
time.sleep(5)
pg.hotkey ("alt","i")
pg.press ("esc")
pg.press ("enter")


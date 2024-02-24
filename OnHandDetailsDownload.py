### #Check On Hand Details Report



import pyautogui as pg
import time

userName = "5638"
password = "ripon"


#Open dedicated Browser
time.sleep (1)
pg.hotkey ("Win","1")

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


# Check On Hand Details
time.sleep (8)
pg.hotkey ("alt", "v")
pg.press ("r")
pg.hotkey ("alt","n")
# pg.press ("enter")
time.sleep (5)
pg.write ("S")
pg.press ("tab")
time.sleep (5)
pg.press ("down", presses =5)
time.sleep (2)
pg.press ("enter")
time.sleep (1)
pg.hotkey ("ctrl", "c")
pg.press ("tab", presses = 3)
pg.press ("enter")
#--------------- ok till now
time.sleep (3)
pg.hotkey ("alt" + "m")
time.sleep (3)
pg.hotkey ("alt" + "n")
time.sleep (3)
pg.hotkey ("alt" + "i")
time.sleep (3)
pg.hotkey ("alt" + "r")
time.sleep (2)
pg.hotkey ("alt" + "p")










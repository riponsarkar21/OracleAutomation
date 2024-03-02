# OracleMoveOrderCreateAutomation
import psutil

#terminate_dedicated_browser
def terminate_dedicated_browser(target_path):

    try:
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            if 'firefox' in proc.info['name'].lower() and target_path in proc.info['exe']:
                psutil.Process(proc.info['pid']).terminate()
                print(f"Terminated Firefox process with PID {proc.info['pid']} and path {target_path}")
    except Exception as e:
        print(f"Error: {e}")
        
target_path = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

#------------------------------------------------------------------------------------------

# Open the dedicated browser
import subprocess

firefox_shortcut_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Mozilla Firefox.lnk"

def open_dedicated_browser(shortcut_path):
    try:
        subprocess.Popen([shortcut_path], shell=True)
        print("Mozilla Firefox is now opening...")
    except Exception as e:
        print(f"Error: {e}")
        
#------------------------------------------------------------------------------------------
import pyautogui as pg
import time

username = "5638"
password = "ripon"

def login_to_website(username, password):
    pg.write(username)
    pg.press("tab")
    pg.write(password)
    pg.press("tab")
    pg.press("enter")

    # Wait for the page to load
    time.sleep(2)
#------------------------------------------------------------------------------------------
# Select Create Move Order Element

def select_move_order_create():
    pg.press ("tab", presses = 12)
    pg.press ("enter")
    time.sleep (1)
    pg.press ("tab")
    pg.press ("enter")


#------------------------------------------------------------------------------------------




terminate_dedicated_browser(target_path)
time.sleep (5)
open_dedicated_browser(firefox_shortcut_path)

#Load The webpage
time.sleep (5)

login_to_website(username, password)

#Load The webpage
time.sleep (8)

# Example usage
select_move_order_create()

#Load The webpage
time.sleep (5)


#------------------------------------------------------------------------------------------
# Wait for the software download 
time.sleep(5)
pg.hotkey ("alt","i")
pg.press ("esc")
pg.press ("enter")
time.sleep (3)

#------------------------------------------------------------------------------------------
# Fill Common Data

time.sleep(5)
pg.press("tab")
time.sleep(.2)
pg.write ("Empty Bag for Packing Plant")
time.sleep(.2)
pg.press ("tab")

#---------------------------------------
time.sleep(.2)
pg.write ("Move Order Transfer")
pg.press ("tab")


#----------------------------------------
time.sleep(.2)
pg.write ("CI - RM")
pg.press ("tab")



#----------------------------------------

time.sleep(.2)
pg.write ("CI - SFLR")
pg.press ("tab", presses = 2)


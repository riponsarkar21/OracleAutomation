### import psutil

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

# Select Overtime Element

def select_overtime():
    pg.press ("tab", presses = 13)
    pg.press ("enter")
    time.sleep (1)
    pg.press ("tab")
    pg.press ("enter")


#------------------------------------------------------------------------------------------
# Create Overtime form

def prepare_overtime_form():
    pg.press ("tab", presses = 17)
    time.sleep (1)
    pg.press ("enter")
    time.sleep (4)
    pg.press ("tab", presses = 10)
    time.sleep (1)

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
select_overtime()

#Load The webpage
time.sleep (5)

# Prepare Overtime Form
prepare_overtime_form()

# Create the Overtime form. 


overtime_date = "25-Feb-2024"
employee_id = "6224"
overtime_hour = "8"
justification = "10:00 PM - 06:00 AM : Leave of Md. Ashekur Rahman"
section = "Packing"
shift = ""


pg.write (overtime_date)
time.sleep (1)
pg.press ("tab", presses = 1)
time.sleep (1)
pg.press ("tab", presses = 1)
time.sleep (1)
pg.press ("enter")
time.sleep (5)


# Create the posting

pg.write (employee_id)
time.sleep (2)
pg.press ("tab", presses = 1)
time.sleep (1)
pg.press ("tab", presses = 1)
# time.sleep (2)
pg.press ("tab", presses = 1)
# time.sleep (2)
pg.write (overtime_hour)
time.sleep (1)
pg.press ("tab", presses = 1)
pg.write (justification)
time.sleep (2)
pg.press ("tab", presses = 4)
pg.write (section)
# time.sleep (1)
# pg.press ("tab")
pg.press ("tab", presses = 3)
pg.write (shift)


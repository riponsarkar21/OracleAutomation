@echo off

REM Ensure the path to the Anaconda Prompt shortcut is correct
set SHORTCUT="C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Miniconda3 (64-bit)\Anaconda Prompt (Miniconda3).lnk"

REM Start Anaconda Prompt
start "" %SHORTCUT%
timeout /t 2 /nobreak >nul  REM Adjust timeout as necessary

REM Wait for Anaconda Prompt window to appear and become active
powershell -Command "& { Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('activate myenv{ENTER}') }"
timeout /t 2 /nobreak >nul  REM Adjust timeout as necessary

REM Send 'jupyter lab' command to Anaconda Prompt
powershell -Command "& { Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('jupyter lab{ENTER}') }"

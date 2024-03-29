@echo off

rem Set the path to your Miniconda installation
set CONDA_PATH=C:\Users\USER\miniconda3

rem Set the name of your virtual environment
set ENV_NAME=myenv

rem Set the path to your Jupyter Notebook file
set NOTEBOOK_PATH=F:\Ripon\Oracle Automation\BatchDetails\OracleBatchAutomation.ipynb

rem Activate the virtual environment
call "%CONDA_PATH%\Scripts\activate.bat" %ENV_NAME%

rem Run the Jupyter Notebook
jupyter nbconvert --execute --to notebook --inplace "%NOTEBOOK_PATH%"

rem Deactivate the virtual environment
call "%CONDA_PATH%\Scripts\deactivate.bat"

rem Show a message box indicating completion
msg * "Jupyter Notebook execution completed!"

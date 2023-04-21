import webbrowser
import subprocess
import time
import os

# Get current path
c_path =os.getcwd()

#go to src folder
os.chdir(f'{c_path}/src')

#time.sleep(5)

# Start the Flask application
subprocess.Popen(['python', 'ReadWebformData.py'])
time.sleep(5)

# Open the web browser
webbrowser.open('http://127.0.0.1:5523')

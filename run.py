import webbrowser
import subprocess
import time
# import GetPath
# from GetPath import current_path
# import os

#Get current path
# c_path = current_path()
# print("aaaa",c_path)
#go to src folder
# time.sleep(5)
# os.chdir(f'{c_path}/src')
# print("Current working directory ",os.getcwd())
# Start the Flask application
subprocess.Popen(['python', 'ReadWebformData.py'])

time.sleep(10)
# Open the web browser
webbrowser.open('http://127.0.0.1:5522')

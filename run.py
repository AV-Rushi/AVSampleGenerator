import webbrowser
import subprocess

# Start the Flask application
subprocess.Popen(['python', 'soapSolution.py'])

# Open the web browser
webbrowser.open('http://127.0.0.1:2024')

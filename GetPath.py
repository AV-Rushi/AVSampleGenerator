import os
# Function to Get the current
# working directory
def current_path():
    print("Current working directory before")
    c_path=os.getcwd()
    print()
    return c_path
# Driver's code
# Printing CWD before
# current_path()

# Changing the CWD
# os.chdir('../')

# Printing CWD after
# current_path()
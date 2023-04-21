import os
# Function to Get the current
# working directory
def current_path():
    print("Current working directory before")
    c_path1=os.getcwd()
    # os.chdir('../')
    # c1_path = os.getcwd()
    # print(c_path)
    # print(c1_path)
    return c_path1
# Driver's code
# Printing CWD before
# current_path()

# Changing the CWD
# os.chdir('../')

# Printing CWD after
# current_path()
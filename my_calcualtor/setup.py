import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\dharm\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\dharm\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("calculator.py", base=base, icon="download.ico")]


cx_Freeze.setup(
    name = "DP Calculator",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["download.ico",'tcl86t.dll','tk86t.dll']}}, #appicon,dll,dll,alliconfoldername
    version = "0.01",
    description = "Dharm Patel",
    executables = executables
    )

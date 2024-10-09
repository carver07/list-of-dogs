"""
Module Docstring: main.py
======================

This is the main module of the read/write to file project
"""

__author__ ="Carver Higginbotham"
__version__= "0.1"
__liscense__="None"
__date__="October 7, 2024"

def read_file(file_name) -> None:
    """
    reads a file and prints it to the console.
    """
with open(file_name) as f:
    print(f.readiness())

def main():
    """
    Main entry point of the application 
    """
    pass

if __name__ == "__main__":
    """
    Starts the program.
    """
    main()
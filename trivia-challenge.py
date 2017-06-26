#Title: Trivia challenge 
#MB 12-05-2017
#Demonstrates -  reading a plain text file bit

import sys

def open_file(file_name, mode):
    """Open a file"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print ("Unable to open the file" )
    
    else:
        return the_file
    
    
    
def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


input ("\n\nPress the enter key to exit")



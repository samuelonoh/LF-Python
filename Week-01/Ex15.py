# imports argv from system
from sys import argv

# Two arguments
script, filename = argv

# open the file which is stored in txt
txt = open(filename)

# Read this file
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

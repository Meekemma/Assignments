
import os

#using the library os, print your local file path on the screen
print("Local file path: ", os.getcwd())

# Create a text file that has your full name and write code to read it and extract first name, middle name and last name.
'''
with open('name.txt', 'r') as f:
    for line in f:
        print(line)
'''

mylines=[]
with open ('name.txt', 'r') as f:
    for line in f:
        mylines.append(line)
    print(mylines[0])    
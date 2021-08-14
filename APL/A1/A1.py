"""
        EE2703 Applied Programming Lab - 2020
            Assignment 1
            Submitted by Devaganthan S S, EE19B018
"""
from sys import argv
import os

if len(argv) < 2:  # This is to Ensure that, an input is always is fed in to the program, in the Command Line
    print('Input File Required')
    exit()
# This is to ensure that the input file exists in the computer
if os.path.exists(argv[1]) == False:
    print('The File does not exist in the computer, or check the file path')
    exit()


Circuit = '.circuit'
End = '.end'
f = open(argv[1])  # Opening the file
lines = f.readlines()  # Reading the lines from the Input File


start = 0
end = 0
k = False
m = False
"   1) The Below code is to ensure that, .circuit and .end are included in the input file. For file type of .netlist,"
"   .Circuit and .end are mandatory thereby, the file won't be opened unless the file has them. For a txt file, the"
"   below code ensures it has a .circuit and .end"
for line in lines:
    temp = line.split()
    if Circuit in temp:
        k = True
    if End in temp:
        m = True
    if k and m:
        break
if (k and m) == False:
    if k == False:
        print('Invalid Circuit Definition: Include .Circuit')
        exit()
    if m == False:
        print('Invalid Circuit Definition: Include .End')
        exit()
"End of 1"

"2) The below code stores the line number of .circuit and .end. It also checks if .circuit comes first and .end comes later"
for line in lines:
    if Circuit in line:
        start = lines.index(line)
    if End in line:
        end = lines.index(line)
if start >= end:  # Checks if .Circuit comes first and .end comes after.
    print('Invalid Circuit Definition')
    exit()

"End of 2"
"3) The next set of codes, removes comments, removes .circuit and .end, strips of \n , removes any extra comments from every line, and stores these"
"   new set of lines in the new list variable realLine"

realLine = []
tempLines = []
for i in range(start, end+1):
    tempLines = [lines[i]] + tempLines

for i in tempLines:
    i = i.strip('\n')  # Strips of newline character
    if Circuit in i or End in i:
        continue
    else:
        temp = i.split('#')  # Rips of comments
        realLine = realLine + [temp[0]]
for i in realLine:
    if i == '\n':
        realLine.remove('\n')


"End of 3"
"4) Now the strings in the realLine lists are reversed, and they are printed in reverse order"
for i in realLine:
    if i == "":
        continue
    temp = i.split()
    print(' '.join(reversed(temp)))

"End"

#!/usr/bin/env python3
# Sample script that reads from a file
# By Terrance Blandford

print ("Here is someone to hack information")
with open("hackme.txt", "r") as file:
    contents = file.read()
    
print("The information found in hackme.txt is: \n")
print(contents)
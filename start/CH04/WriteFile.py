#!/usr/bin/env python3
# Sample script that writes to a file
# By Terrance Blandford

name = input ("What is your name? ")
color = input ("What is your favorite color? ")
pet = input ("What was your first pets name? ")
maiden_name = input ("What is your mothers maiden name? ")
school = input ("What elementary school did you attend? ")

with open('hackme.txt', "w") as file:
    file.write ("User Information\n")
    file.write("------------------\n")
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Color; {color}\n")
    file.write(f"First Pet's Name: {pet}")
    file.write(f"Mother's Maiden Name: {maiden_name}\n")
    file.write(f"Elementary School: {school}\n")

print("Your answers have been saved to hackme.txt")
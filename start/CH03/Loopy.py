#!/usr/bin/env python3
# example workign with Loops
#By Terrance Blandford

question = input("Is today a good day? Please answer with y or n: ")

if question == "y" :
    #Create a loop of 10 times saying yea it is"
    number = 1
    while number < 11:
        print("Yes it is")
        number += 1
elif question == 'n' :
    print("Thats ok tomorrow will be!")
else:
    print("please answer with only 'y' or 'n'.")
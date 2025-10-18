#!/usr/bin/env python3
# example workign with conditionals
#By Terrance Blandford

question = input("Is today a good day? Please answer with y or n: ")

if question == "y" :
    print("Yes it is")
elif question == 'n' :
    print("Thats ok tomorrow will be!")
else:
    print("please answer with only 'y' or 'n'.")
#!/usr/bin/env python3
# example workign with Loops and Functions
#By Terrance Blandford

def send_message():
    number = 1
    while number <= 10:
        print ("Yeah it is")
        number += 1

question = input("Is today a good day? Please answer with y or n: ").strip().lower()

if question == "y" :
   send_message()
elif question == 'n' :
    print("Thats ok tomorrow will be!")
else:
    print("please answer with only 'y' or 'n'.")
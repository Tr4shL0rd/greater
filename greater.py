import os
from termcolor import colored
import datetime

name = input("what is your name? ")
os.system('clear')
now = datetime.datetime.now()
print("Hello, %s!" % name.title())
print()
print("the current date and time is:")
print(colored(now.strftime("%Y-%m-%d %H:%M:%S"), "yellow"))
print("")
if name == "ketil":
    print("******************")
    print("what day is it?")
    print("time")
    input("")    
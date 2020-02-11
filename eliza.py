# My name is ESWAR SAI VEERAPANENI
# 30/01/2020
# CMSC 416
# Email - veerapanenies@vcu.edu
# This program would act like an online therapist and chats with the user in a way that he can talk to it about
# anything and THE program (Eliza) would respond in a way that at least tries to make the user feel better,
# Lets say if the user says " Im sad", Eliza would reply saying, "why are you say?"
# if he says that " I want to talk" it replies "you want to talk?"
# The algorithm that I try to use is simple
# first the main method has a while loop that makes Eliza respond until user say quit
# if he doesnt say quit, it calls the respond method
# The respond method compares the given string with the user text and see for matches
# there are bunch of if else statements that would decide which block would the program go to.
# if none matches it goes to the final else block and it gives some default answers like " can you elaborate?" and answers like that
# The program will keep running until the user calls quits.


import random
import string
import re

# the below lines of code gives us the words that the computer should use to convert the words stated by the user
# into the answers it can give back
reflect = {"are": "am", "am": "are", "was": "were", "i": "you", "i'll": "you will", "you": "me", "your": "my",
           "you'll": "I will", "you've": "I have", "i've": "you have", "yours": "mine", "i'd": "you would",
           "my": "your", "me": "you", "it": "that"}
name = ""


# The below statements are the regex statements and are used to find the matching in the users statements and would
# reply the user based on that

# The below method would take the user string and does the reflection table and returns the user the required response.
def convert(string, result):
    # changes every upper case word into a lower case words
    words = string.lower().split()
    currentKeys = result.keys();  # get all the keys from the keys in the reflect thing
    length = len(words);
    for i in range(0, length):  # for loop that passes every word
        if words[i] in currentKeys:
            words[i] = result[words[i]]
    words = ' '.join(words)  # joins the word and sends it back as the result
    return words


# The given method would take the string and compares it to the Regular Expressions and checks what matches
# and returns the user the most suitable response
def respond(str):
    str = str.lower()
    # the below line of code would check if they are you and your in the user input
    if re.compile(r'\b(you|your)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(you|your)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] I am irrelevant in this topic, tell me more about you")
    # else the below line of code would check if they are can\'t|don\'t|won\'t|cant|dont|wont in the user input
    elif re.compile(r'\b(can\'t|don\'t|won\'t|cant|dont|wont)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(can\'t|don\'t|won\'t|cant|dont|wont)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        if beg == "can't|cant":
            print("[Eliza] Why do you think you")
        if beg == "won't|wont":
            print("[Eliza] why wouldn't you?")
        if beg == "don't|dont":
            print("[Eliza] Why don't you")
    # else the below line of code would check if they are think in the user input
    elif re.compile(r'\b(think)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(think)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza]Why do you think that?")
    # else the below line of code would check if they are good|bad|worse|better|worst in the user input
    elif re.compile(r'\b(good|bad|worse|better|worst)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(good|bad|worse|better|worst)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] Talk to me more about what is making you feel", beg)
    # else the below line of code would check if they are need|desire in the user input
    elif re.compile(r'\b(need|desire)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(need|desire)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] Are you sure you need this?")
    # else the below line of code would check if they are i\'m|am in the user input
    elif re.compile('^(.*?)\s(i\'m|am)\s(.*?)$').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('^(.*?)\s(i\'m|am)\s(.*?)$', str)
        beg = tokens.group(1)
        mid = tokens.group(2)
        last = tokens.group(3)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        # calls the reflect method and converts into a response
        mid = convert(mid, reflect)
        # calls the reflect method and converts into a response
        last = convert(last, reflect)
        print("[Eliza] Why do you think you are", last, "?")
    # else the below line of code would check if they are want in the user input
    elif re.compile('^(.*?)\s(want)\s(.*?)$').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('^(.*?)\s(want)\s(.*?)$', str)
        beg = tokens.group(1)
        mid = tokens.group(2)
        last = tokens.group(3)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        # calls the reflect method and converts into a response
        mid = convert(mid, reflect)
        # calls the reflect method and converts into a response
        last = convert(last, reflect)
        print("[Eliza] you want", last, "?")
    # else the below line of code would check if they are yes|no|maybe|guess in the user input
    elif re.compile('(.*)(yes|no|maybe|guess)(.*)').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('(.*)(yes|no|maybe|guess)(.*)', str)
        beg = tokens.group(1)
        mid = tokens.group(2)
        last = tokens.group(3)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        # calls the reflect method and converts into a response
        mid = convert(mid, reflect)
        # calls the reflect method and converts into a response
        last = convert(last, reflect)
        print("[Eliza] that's fine, do you want to elaborate on this? or you can choose talk about something else")
    # else the below line of code would check if they are fear|anger|sad|joy|disgust|surprise|trust in the user input
    elif re.compile(r'\b(fear|anger|sad|joy|disgust|surprise|trust)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(fear|anger|sad|joy|disgust|surprise|trust)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] what do you think is making you feel", beg)
    # else the below line of code would check if they are family|mother|mom|dad|father|friends in the user input
    elif re.compile('^(.*?)\s(family|mother|mom|dad|father|friends)\s(.*?)$').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('^(.*?)\s(family|mother|mom|dad|father|friends)\s(.*?)$', str)
        beg = tokens.group(1)
        mid = tokens.group(2)
        last = tokens.group(3)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        # calls the reflect method and converts into a response
        mid = convert(mid, reflect)
        # calls the reflect method and converts into a response
        last = convert(last, reflect)
        print("[Eliza] how is your", mid, "?")
    # else the below line of code would check if they are feel in the user input
    elif re.compile(r'\b(feel)\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b(feel)\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] Let us explore more about this feeling")
    # else the below line of code would check if they are i'm or i am in the user input
    elif re.compile('^(.*?)\s(i\'m|am)\s(.*?)$').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('^(.*?)\s(i\'m|am)\s(.*?)$', str)
        beg = tokens.group(1)
        mid = tokens.group(2)
        last = tokens.group(3)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        # calls the reflect method and converts into a response
        mid = convert(mid, reflect)
        # calls the reflect method and converts into a response
        last = convert(last, reflect)
        print("[Eliza] Why do you think you are", last, "?")
    # else the below line of code would check if they are am|was|it|i|i\'ll|you will|me|my|you\'ll|you\'ve|i\'ve|yours|i\'d|me|you in the user input
    elif re.compile(
            '(.*)(am|was|it|i|i\'ll|you will|me|my|you\'ll|you\'ve|i\'ve|yours|i\'d|me|you)(.*)').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('^(.*?)(am|was|i|i\'ll|you will|me|my|you\'ll|you\'ve|i\'ve|yours|i\'d|me|you)(.*)',
                           str)
        beg = tokens.group(1)
        mid = tokens.group(2)
        last = tokens.group(3)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        # calls the reflect method and converts into a response
        mid = convert(mid, reflect)
        # calls the reflect method and converts into a response
        last = convert(last, reflect)
        print("[Eliza]", beg, last, "?")
    # else the below line of code would check if they are why|what|when in the user input
    elif re.compile('(.*?)(why|what|when)(.*)').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search('(.*)(why|what|when)(.*)', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] Let us talk about something else, how are your friends?")
    # else the below line of code would print out a default statement
    elif re.compile(r'\b()\b').search(str):
        # it gets the message as the token if it contains the above words
        tokens = re.search(r'\b()\b', str)
        beg = tokens.group(1)
        # calls the reflect method and converts into a response
        beg = convert(beg, reflect)
        print("[Eliza] I don't think I understand, Can you please elaborate")


# The main method has all the opening credentials of Eliza
def main():
    print("enter 'quit' when you are done")
    print("[Eliza] Hello, I am Eliza! I specialize in therapy, What is your name")
    s = ""
    i = 0
    print("[user]", end='')
    # if the user types quit the program would end
    while s != 'quit':
        # it takes the input from user and executes other methods
        if (i < 1):
            s = input()
            name = s;
            print("[Eliza] Hello", s, ",how do you feel today?")
            i = 1
        else:
            # else it asks the user for input
            print("[", name, "] ", end='')
            s = input()
            respond(s)


main()

"""
Author: Michael Tekin, michael.tekin@uky.edu, CS115-009
Assignment: Program 3 (Chuck-A-Luck) Design
Purpose: A game of chance
Preconditions: User inputs a number from 1-6 to bet on, an amount to wager, and,
if they haven't lost all the money in the pot, whether or not to keep playing.
Postconditions: The user is shown an image for each of the die that were rolled,
feedback on whether or not their number matched, the amount of money they won or
lost, and, if they haven't lost all the money in the pot, a choice of whether or
not to keep playing.
Date completed: 28th Oct, 2015
"""


#initiailize playagain flag to True
#set initial pot amount

#while playagain and pot isn't empty

#-------------------------------------------------------------------------------
#draw_dice 
#Parameters: (int) x and y of location, (int) number of the die, the name of the
#graphics window that the die will be drawn on
#Purpose: draw a die image on the screen at the location given, using the
#corresponding gif file
#Postconditions: returns the image object created
#Design
    #Use the number of the die to determine which image to draw
    #Create and image object using the given x and y coordinates and the image
    #that corresponds with the number of the die
    #Draw the image object in the graphics window
    #Return the image object

#-------------------------------------------------------------------------------
#get_bet
#Parameters: the amount of the pot, the name of the graphics window that the
#input will be taken from
#Purpose: get a bet from the user between 1 and the amount of the pot
#(inclusive)
#Postconditions: returns the validated user's input
#Design
    #Get the users bet from the graphics window
    #As long as the users input isn't just one or more digits
        #Ask the user for another bet
    #As long as the users bet isn't between 1 and the amount of the pot 
    #(inclusive)
        #Ask the user for another bet
    #Return the users bet

#-------------------------------------------------------------------------------
#get_number
#Parameters: the name of the graphics window that the input will be taken from
#Purpose: get an integer from the user (1-6 inclusive)
#Postconditions: returns the users chosen integer (1-6 inclusive)
#Design
    #Get the users die number from the graphics window
    #As long as the users input isn't a digit
        #Ask the user for another die number
    #As long as the users input isn't between 1 and 6 inclusive
        #Ask the user for another die number
    #Return the users die number

#-------------------------------------------------------------------------------
#check_matches
#Parameters: three rolls and one user roll
#Purpose: compare one random integer between 1 and 6 (inclusive) to 3 other
#random integers between 1 and 6 (inclusive)
#Postconditions: returns the number of matches between the one random integer
#and the other three
#Design
    #Set a random integer between 1 and 6 as the users roll
    #Set three random integers to the three die that are rolled
    #For each of the three
        #If the users roll matches the other die roll
            #Count it as 1 match
    #Return the number of matches

#-------------------------------------------------------------------------------
#in_box
#Parameters: two points that define the box, a third point
#Purpose: compare three points to determine whether or not the third is
#inbetween the first two
#Postconditions: returns True if the third point is inbetween the first two,
#False if not
#Design
    #If the x and y coordinates of the third point are inbetween the x and y
    #coordinates of the first two points
        #Return True
    #Otherswise
        #Return False

#-------------------------------------------------------------------------------
#play_again
#Parameters: the name of the graphics window that will be checked for clicks
#Purpose: check whether the user clicks in a Yes box or a No box
#Postconditions: returns True if the user clicked in the Yes box, False
#otherwise
#Design
    #Get a mouseclick from the user
    #If the x and y coordinates of the users click are inbetween the corners of
    #the Yes box
        #Return True
    #Otherwise
        #Return False


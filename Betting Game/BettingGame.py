"""
Author: Michael Tekin, michael.tekin@uky.edu, CS115-009
Assignment: Program 3 (Chuck-A-Luck)
Purpose: A game of chance
Preconditions: User inputs a number from 1-6 to bet on, an amount to wager, and,
if they haven't lost all the money in the pot, whether or not to keep playing.
Postconditions: The user is shown an image for each of the die that were rolled,
feedback on whether or not their number matched, the amount of money they won or
lost, and, if they haven't lost all the money in the pot, a choice of whether or
not to keep playing.
Date completed: 9th Nov, 2015
"""

from graphics import *
from random import randrange

def main():

    win_x = 600
    win_y = 600
    win = GraphWin('Chuck-A-Luck', win_x, win_y)
    
    #initiailize playagain flag to True
    playagain = True
    
    #set initial pot amount
    pot = 100
    
    title = Text(Point(win_x/2, win_y/8), 'Chuck-A-Luck')
    title.setSize(30)
    title.draw(win)
    
    #---------------------------------------------------------------------------
    def draw_dice(d_coordinates, d_num, window): 
        """
        Purpose: draw a die image on the screen at the location given, using the
        corresponding gif file
        Parameters: (int) x and y of location, (int) number of the die, name
        of the graphics window
        Postconditions: draws an image and returns the image object created
        """
        
        #Get the file name of the appropriate die by concatenating the die
        #number with .gif
        die_image = Image(d_coordinates, str(d_num) + '.gif')
        
        die_image.draw(window)
    
        return die_image
    
    #---------------------------------------------------------------------------
    def get_bet(pot, window):
        """
        Purpose: get a bet from the user between 1 and the value of the pot
        (inclusive)
        Parameters: amount of the pot, name of the graphics window
        Postconditions: returns the validated user's bet
        """
        
        valid_bet = False
        get_bet_message = Text(Point(win_x/2, win_y/6+20),
                               'How much do you want to bet? ' +
                               '(1-{})'.format(pot))
        get_bet_message.draw(win)
        get_bet_entry = Entry(Point(win_x/2, win_y/6+50), 5)
        get_bet_entry.draw(win)
        
        win.getMouse()
        users_bet = get_bet_entry.getText()
        
        while not valid_bet:
            #While the users input isn't just one or more digits
            #Ask the user for another bet
            #BONUS#
            if users_bet.isdigit():
                users_bet = int(users_bet)
                #While the users bet isn't between 1 and the amount of the
                #pot (inclusive)                
                if (1 <= users_bet <= pot):
                    valid_bet = True
                else:
                    if users_bet < 1:
                        invalid_bet_message = Text(Point(win_x/2, win_y/6+80),
                                                   'You have to bet at ' +
                                                   'least $1')
                    else:
                        invalid_bet_message = Text(Point(win_x/2, win_y/6+80),
                                                   "You don't have that " +
                                                   "much money")
                        
                    invalid_bet_message.draw(win)   
                    win.getMouse()
                    invalid_bet_message.undraw()
                    users_bet = get_bet_entry.getText()       
                    
            else:
                invalid_bet_message = Text(Point(win_x/2, win_y/6+80),
                                           "That's not a valid bet")
                invalid_bet_message.draw(win)   
                win.getMouse()
                invalid_bet_message.undraw()
                users_bet = get_bet_entry.getText()                 
        
        get_bet_message.undraw()
        get_bet_entry.undraw()

        return users_bet
    
    #---------------------------------------------------------------------------
    def get_number(window):
        """
        Purpose: get a die number from the user (1-6)
        Parameters: name of the graphics window
        Postconditions: returns the validated user's die number
        """
        
        valid_number = False
        get_number_message = Text(Point(win_x/2, win_y/6+20),
                                  'Which number do you want to bet on? (1-6)')
        get_number_message.draw(win)
        get_number_entry = Entry(Point(win_x/2, win_y/6+50), 5)
        get_number_entry.draw(win)
        
        win.getMouse()

        users_number = get_number_entry.getText()        
        
        while not valid_number:
            #As long as the users input isn't a digit
            if users_number.isdigit():
                #As long as the users input isn't between 1 and 6 inclusive
                if (1 <= int(users_number) <= 6):
                    valid_number = True
                else:
                    invalid_number_message = Text(Point(win_x/2, win_y/6+80),
                                                  "That's not a valid " +
                                                  "die number")
                    invalid_number_message.draw(win)
                    
                    win.getMouse()
                    invalid_number_message.undraw()
                    users_number = get_number_entry.getText()
            else:
                invalid_number_message = Text(Point(win_x/2, win_y/6+80),
                                              "That's not a valid die number")
                invalid_number_message.draw(win)
                
                win.getMouse()
                invalid_number_message.undraw()
                users_number = get_number_entry.getText()                

        get_number_message.undraw()
        get_number_entry.undraw()
        
        users_number = int(users_number)
        return users_number
    
    #---------------------------------------------------------------------------
    def check_matches(rand_die_1, rand_die_2, rand_die_3, users_die_num):
        """
        Purpose: compare the users number to the three rolls and determine the
        number of matches
        Parameters: (int) three rolls and (int) one user number
        Postconditions: (int) 0-3 number of matches
        """    
        
        num_matches = 0
        
        #For each of the three
        #If the users roll matches the other die roll
            #Count it as 1 match 
        if users_die_num == rand_die_1:
            num_matches += 1
        if users_die_num == rand_die_2:
            num_matches += 1        
        if users_die_num == rand_die_3:
            num_matches += 1

        return num_matches
    
    #---------------------------------------------------------------------------
    def in_box(corner_1, corner_2, user_point):
        """
        Purpose: compare three points to determine whether or not the third is
        inbetween the first two
        Parameters: two points that define a box, a third point
        Postconditions: returns True if the third point is inbetween the first
        two, False if not
        """      
        
        in_box = False
        
        #If the x and y coordinates of the third point are inbetween the x and y
        #coordinates of the first two points
        if ((corner_1.getX() <= user_point.getX() <= corner_2.getX()) and 
            (corner_1.getY() <= user_point.getY() <= corner_2.getY())):
            in_box = True

        return in_box
    
    #---------------------------------------------------------------------------
    def play_again(window_name):
        """
        Purpose: check whether or not the user clicks in a Yes-box
        Parameters: name of graphics window
        Postconditions: returns True if the user clicked in the Yes-box, False
        otherwise
        """
        
        play_again_message = Text(Point(win_x/2, win_y/6+20),
                                  'Do you want to play another game?')
        play_again_message.draw(win)
        
        YES_box = Rectangle(Point(win_x/3-40, win_y/2-40), 
                            Point(win_x/3+40, win_y/2+40))
        YES_box.draw(win)
        
        YES_text = Text(Point(win_x/3, win_y/2), 'YES')
        YES_text.draw(win)
        
        NO_box = Rectangle(Point(win_x*2/3-40, win_y/2-40),
                           Point(win_x*2/3+40, win_y/2+40))
        NO_box.draw(win)
        
        NO_text = Text(Point(win_x*2/3, win_y/2), 'NO')
        NO_text.draw(win)
        
        #Get the coordinates of the users mouseclick to check where they've
        #clicked
        user_click = win.getMouse()
        
        while ((not in_box(Point(win_x/3-40, win_y/2-40),
                           Point(win_x/3+40, win_y/2+40),
                           user_click)) and
               (not in_box(Point(win_x*2/3-40, win_y/2-40),
                           Point(win_x*2/3+40, win_y/2+40),
                           user_click))):
            invalid_click_message = Text(Point(win_x/2, win_y*2/3),
                                         'You must click inside one of ' +
                                         'the two boxes')
            invalid_click_message.draw(win)
            
            user_click = win.getMouse()
            invalid_click_message.undraw()
        
        play_again_message.undraw()
        YES_box.undraw()
        YES_text.undraw()
        NO_box.undraw()
        NO_text.undraw()
        
        #Return True if the users click was inside the yes-box, false otherwise
        return in_box(Point(win_x/3-40, win_y/2-40),
                      Point(win_x/3+40, win_y/2+40), user_click)
    
    #While the user still has money and hasn't chosen to stop playing, keep
    #playing the game
    while playagain and pot != 0:
        
        users_bet = get_bet(pot, win)
        users_number = get_number(win)
        
        dice = []
        for die in range(0, 3):
            dice.append(randrange(1, 7))
        die_1_image = draw_dice(Point((((win_x-456)/4)+76), win_y/3), dice[0],
                                win)
        die_2_image = draw_dice(Point(win_x/2, win_y/3), dice[1], win)
        die_3_image = draw_dice(Point((win_x/2+152)+((win_x-456)/4), win_y/3),
                                dice[2], win)
        
        num_matches = check_matches(dice[0], dice[1], dice[2], users_number)
        
        if 0 < num_matches:
            if num_matches == 1:
                earnings = users_bet
            elif num_matches == 2:
                earnings = (users_bet * 5)
            elif num_matches == 3:
                earnings = (users_bet * 10)
            earnings_message = Text(Point(win_x/2, win_y*2/3), 
                                     'you matched {} die, you win ${}'.format(
                                         num_matches, earnings))
        else:
            #Make 'earnings' negative for 0 matches so that the pot accumulator 
            #down below will subtract the users losses
            earnings = (users_bet * -1)
            earnings_message = Text(Point(win_x/2, win_y*2/3), 
                                     'you matched {} die, you lose ${}'.format(
                                         num_matches, earnings * -1))
        earnings_message.draw(win)
        
        pot += earnings
        pot_amount_message = Text(Point(win_x/2, win_y*2/3+20), 'you have $' + 
                                  str(pot))
        pot_amount_message.draw(win)
        
        win.getMouse()
        die_1_image.undraw()
        die_2_image.undraw()
        die_3_image.undraw()
        earnings_message.undraw()
        pot_amount_message.undraw()
        
        if pot > 0:
            playagain = play_again(win)
            
    if pot > 0:
        final_results_message = Text(Point(win_x/2, win_y*2/3),
                                     "You're leaving with ${}".format(pot))
    else:
        final_results_message = Text(Point(win_x/2, win_y*2/3), 
                                     'Sorry, you lost!')
    final_results_message.draw(win)

    win.getMouse()
    win.close()

main()
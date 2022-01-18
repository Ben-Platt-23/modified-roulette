# This python file contains a program that imitates my (Ben Platts) modified version of the classic casino game roulette

# Importing math and random 
import math
import random

# Creates a list called 'cards' that stores every card 
global cards 
cards = ['2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'Jack', 'Jack', 'Jack', 'Jack', 'Queen', 'Queen', 'Queen', 'King', 'King', 'Ace']
# Creates a list called 'card_ids' that stores one of every card to be used in the draw_a_card function to check the entry
card_ids = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
global roulette_spin 
roulette_spin = ''
global player_result
player_result = ''
global play_again
play_again = False
global player_bet
player_bet = 0
global bet_is_ready
bet_is_ready = False



# Creates the system for payout
def betting_system():
    global betting_weight
    betting_weight = 1
    global player_payout
    player_payout = 0
    global card_weight
    card_weight = 0



    if roulette_spin == 'Ace':
        card_weight = 13
    elif roulette_spin == 'King':
        card_weight = 12
    elif roulette_spin == 'Queen':
        card_weight = 11
    elif roulette_spin == 'Jack':
        card_weight = 10
    elif roulette_spin == '10':
        card_weight = 9
    elif roulette_spin == '9':
        card_weight = 8
    elif roulette_spin == '8':
        card_weight = 7
    elif roulette_spin == '7':
        card_weight = 6
    elif roulette_spin == '6':
        card_weight = 5
    elif roulette_spin == '5':
        card_weight = 4
    elif roulette_spin == '4':
        card_weight = 3
    elif roulette_spin == '3':
        card_weight = 2
    elif roulette_spin == '2':
        card_weight = 1


    if player_bet >= 10000 and player_bet < 20000:
        betting_weight += 2
        player_payout = (card_weight + betting_weight) * player_bet
    elif player_bet >= 20000 and player_bet < 30000:
        betting_weight += 3
        player_payout = (card_weight + betting_weight) * player_bet
    elif player_bet >= 30000 and player_bet < 40000:
        betting_weight += 4
        player_payout = (card_weight + betting_weight) * player_bet
    elif player_bet >= 40000 and player_bet < 50000:
        betting_weight += 5
        player_payout = (card_weight + betting_weight) * player_bet
    elif betting_weight == 1:
        player_payout = (card_weight + betting_weight) * player_bet




# Creates the function for the betting system
def bet_intake_system():
    betting_system()
    # Creates a global variable for the amount of cards 
    global amount_of_cards 
    # Sets amount of cards equal to 0 
    amount_of_cards = 0
    # Creates a global variable for whether the player is betting or not (are they playing or not)
    global is_player_betting 
    # Sets the is player betting variable to False 
    is_player_betting = False    
    # Creates a global variable for the players bet 
    global player_bet
    global is_bet_ready
   

    
    
            


    # Creates a while loop to keep going until the is player betting variable does not equal False
    while is_player_betting == False:
        start_game = input('Welcome to modified roulette. If you are ready to play enter "ready". (CASE SENSITIVE)')
        while start_game != 'ready':
            start_game = input('Welcome to modified roulette. If you are ready to play enter "ready". (CASE SENSITIVE)')
        if start_game == 'ready':
            start_bet = input('If you are ready to bet, enter "ready". (CASE SENSITIVE)')
        while start_bet != 'ready':
            start_bet = input('If you are ready to bet, enter "ready". (CASE SENSITIVE)')
        if start_bet == 'ready':
            print('Minimum bet is 10,000.')
            player_bet = int(input('Please enter your bet.'))

        #
        if player_bet >= 10000:
            # Takes the amount of cards variable and sets it equal to 1 to represent the player getting one card
            amount_of_cards += 1
            # Sets the is bet ready variable to True
            is_bet_ready = True
            # Sets the is player betting variable to True
            is_player_betting = True
        else:
            # Sets the is player betting variable to False
            is_player_betting = False
            # Sets the is bet ready variable to False
            is_bet_ready = False   
            # Lets the player now that they entered an incorrect answer and need to enter a correct answer
            player_bet = input('Invalid bet. Please enter your bet.')




# Creates the function for drawing the players cards
def draw_a_card(cards):
    global random_cards
    random_cards = random.choices(card_ids, k = cards)
    print('Your card is ' + str(random_cards))







# Creates a function that will call the betting system function then the draw a card function and encapsulate the calculations for the games result and will print them out
def modified_roulette():

    bet_intake_system()
    

    # Checks if the bet is ready
    if bet_is_ready == True:
        # If the bet is ready then the game asks the player if they are ready to move to the card drawing phase
        is_player_ready_to_draw = input('Please type "ready" if you are ready to draw your cards. (CASE SENSITIVE)')

    # creates the ready to draw variable and sets it to False
    ready_to_draw = False
    # Creates the is player ready to draw variable and sets it to an empty string
    is_player_ready_to_draw = ''

    # Creates a loop that checks if ready ready to draw is NOT equal to True
    while ready_to_draw != True:
        # Checks if the is player ready to draw variable is set to 'ready;
        if is_player_ready_to_draw == 'ready':
            # If the player is ready to draw then the ready to draw variable is set to True
            ready_to_draw = True
        # If the answer isnt 'ready' then the game asks the player again if they are ready
        else:
            is_player_ready_to_draw = input('Please type "ready" if you are ready to draw your cards. (CASE SENSITIVE)')
    
    # Checks if the ready to draw variable is equal to True
    if ready_to_draw == True:
        # If the player is ready to draw then the game calls the draw a card function with the players amount of cards given as a parameter
        draw_a_card(cards = amount_of_cards)
      
    
    # Checks if the ready to draw variable is set to True
    if ready_to_draw == True:
        # If ready to draw equals True then the game asks the player if they are now ready to spin 
        ready_to_spin = input('If you are ready to spin enter "ready". (CASE SENSITIVE)')

    # Checks if the player is ready to spin
    if ready_to_spin == 'ready':
        # If the player is ready to spin then a new variable called roulette spin is created that holds the winning card
        roulette_spin = random.choices(cards, k = 1)
        # Prints out the winning card with a statement 
        print('The winning card is ' + str(roulette_spin) + '.')
    # Else 
    else:
        # Creates a while loop that checks if ready to spin does NOT equal 'ready'
        while ready_to_spin != 'ready':
            # While ready to spin does NOT equal 'ready' then continue to ask the player if they are ready to spin 
            ready_to_spin = input('If you are ready to spin enter "ready". (CASE SENSITIVE)')


    

    for card in roulette_spin:
        if card in random_cards:
            betting_system()
            player_result = 'won'
            print('Congratulations, you won!!!')
            print('Payout: $' + str(player_payout))
            play_again_input = input('If you would like to play again please enter "play". (CASE SENSITIVE)')
            
            while play_again_input != 'play':
                play_again_input = input('If you would like to play again please enter "play". (CASE SENSITIVE)')
            if play_again_input == 'play':
                modified_roulette()
            
            
     
        else:
            player_result = 'lost'
            print('Sorry, you lose.')
            print('You lost everything you bet.')
            play_again_input = input('If you would like to play again please enter "play". (CASE SENSITIVE)')
            
            while play_again_input != 'play':
                play_again_input = input('If you would like to play again please enter "play". (CASE SENSITIVE)')
            if play_again_input == 'play':
                modified_roulette()
           
            



modified_roulette()





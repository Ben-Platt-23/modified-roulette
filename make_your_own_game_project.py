import random

# Creates a list called 'cards' that stores every card 
cards = ['2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'Jack', 'Jack', 'Jack', 'Jack', 'Queen', 'Queen', 'Queen', 'King', 'King', 'Ace']
# Creates a list called 'card_ids' that stores one of every card to be used in the draw_a_card function to check the entry
card_ids = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#
card_weights = []
#
chosen_card = ''
#
ready = ''
#
player_bet = ''
#
is_player_betting = False
#
amount_of_cards = 0
#
is_bet_ready = False
#
ready_to_draw = False
#
ready_to_draw_user_input = ''

def draw_a_card():
    # Creates a variable that stores four random choices from the card_ids list to offer to the player
    four_random_cards = random.choices(card_ids, k = 4)
    # Prints out those four random cards
    print(four_random_cards)
    # Creates a variable that is defined by a player input where the player is asked to chose from the four random cards given to them
    chosen_card = input('Please enter ONE of the integers or strings displayed. (Case Sensitive)')

    # Checks if the card entered by the player is one of the four random cards
    if chosen_card in four_random_cards:
        # If it is one of the four random cards then it will tell the player they chose a valid entry 
        print('Correct entry, continue.')
    # If the card is not one of the four random choices a loop starts that lets the player know the card entry is invalid and then continues to ask them to enter a new choice until it is one of the four random cards
    else:
        # Starts the loop
        while chosen_card not in four_random_cards:
            # Lets the player know they have an invalid entry
            print('Invalid entry, please try again')
            # Updates the chosen card variable
            chosen_card = input('Please enter ONE of the integers or strings displayed. (Case Sensitive)')

def betting_system():
    
    amount_of_cards = 0
    is_player_betting = False
    while is_player_betting == False:
        print('Welcome to modified roulette.')
        #print('') Write a print statement explaining the game 
        print('If you bet 10,000 you get to pick one card. Every extra 10,000 you bet, you get an extra card to draw. (Limit of 5 cards)')
        player_bet = int(input('Please enter your bet.'))
        
        if player_bet >= 10000 and player_bet <= 20000:
            amount_of_cards += 1
            is_bet_ready = True
            is_player_betting = True
            print(amount_of_cards)
        elif player_bet >= 20001 and player_bet <= 30000:
            amount_of_cards += 2
            is_player_betting = True
            is_bet_ready = True
            print(amount_of_cards)
        elif player_bet >= 30001 and player_bet <= 40000:
            amount_of_cards += 3
            is_player_betting = True
            is_bet_ready = True
            print(amount_of_cards)
        elif player_bet >= 40001 and player_bet <= 50000:
            amount_of_cards += 4
            is_player_betting = True
            is_bet_ready = True
            print(amount_of_cards)
        elif player_bet >= 50001 and player_bet <= 60000:
            amount_of_cards += 5
            is_player_betting = True
            is_bet_ready = True
            print(amount_of_cards)
        elif player_bet >= 60001:
            is_player_betting = False
            is_bet_ready = False
            print(amount_of_cards)
            player_bet = input('Invalid bet. Please enter your bet.')


def draw_a_card(k):
        random_cards = random.choices(cards, k = amount_of_cards)
        print(random_cards)
        chosen_card = input('Please enter ONE of the integers or strings displayed. (Case Sensitive)')

        if chosen_card in random_cards:
            print('Valid entry, continue.')
        else:
            while chosen_card not in random_cards:
                print('Invalid entry, please try again')
                chosen_card = input('Please enter ONE of the integers or strings displayed. (Case Sensitive)')
        



def modified_roulette():
    betting_system()

    if is_bet_ready == True:
        ready_to_draw_user_input = input('Please type "ready" if you are ready to draw your cards.')
    
    ready_to_draw = False
    ready_to_draw_user_input = ''
    while ready_to_draw != True:
        if ready_to_draw_user_input == 'ready':
            ready_to_draw = True
        else:
            ready_to_draw_user_input = input('Invalid entry. Enter "ready" when ready')
    if ready_to_draw == True:
        draw_a_card(k = amount_of_cards)
        
    if ready_to_draw == True:
        ready = input('If you are ready to spin enter "ready". (Case Sensitive)')
   
    if ready == 'ready':
        weighted_roulette_spin = random.choices(card_ids, k = 1)
        print('The winning card is ' + str(weighted_roulette_spin) + '.')
    else:
        while ready != 'ready':
            ready = input('If you are ready to spin enter "ready". (Case Sensitive)')  

    if weighted_roulette_spin == chosen_card:
        print('Congratulations, you won!!!')
    else:
        print('Sorry, you lose.')


draw_a_card()





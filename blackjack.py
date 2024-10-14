import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
possible_actions = ['H','S','h','s']
keep_playing_choices = ['Y','y','N','n']

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        # deck_cards attribute is a list containing all 52 cards
        self.deck_cards = []
        for suit in suits:
            for rank in ranks:
                self.deck_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.deck_cards)
    
    def deal_one(self):
        return self.deck_cards.pop()
        
    def __str__(self):
        for index in range(len(self.deck_cards)):
            print(self.deck_cards[index])
        
        return f"\nDeck has {len(self.deck_cards)} cards."

class Player:
    
    def __init__(self,name,bank=100):
        # player_cards attribute is a list containing all the player's cards on the table (face up)
        self.name = name
        self.bank = bank
        self.action = ''
        self.bet = 0
        self.player_cards = []
        self.total_value = 0
    
    def place_bet(self):
        #Player places bet
        bet = 0
        choice_made = False
        while (choice_made == False):
            bet = input("Place your bet: ")
            if bet.isnumeric():
                #Check if bet is a number
                bet = int(bet)
                if (0<bet<=player.bank):
                    #Check if bet is less than player bank
                    self.bet = bet
                    self.bank -= bet
                    choice_made = True
                    print("\n")
                else:
                    #Bet too high
                    print("Not enough money!")
            else:
                #Invalid input
                print("Please choose a valid number!")
    
    def hit(self,new_card):
        self.player_cards.append(new_card)
        if (new_card.rank != 'Ace'):
            #If card is not an Ace, add to total value normally
            self.total_value += new_card.value
        elif (self.total_value >= 11):
            #If total value + 11 >= 21, count Ace as value 1
            new_card.value = 1
            self.total_value += new_card.value
        else:
            #If card is Ace and total value + 11 < 21, add as default Ace value, 11
            self.total_value += new_card.value
        
    def display_cards(self):
        print(self.name,"has:")
        for index in range(len(self.player_cards)):
            time.sleep(1.5)
            print(self.player_cards[index])
        print("Total value: ",self.total_value,"\n")
        print("Bet: ",self.bet,"$\n")
    
    def bust_condition(self):
        if self.total_value>21:
            return True
        else:
            return False
    
    def blackjack_condition(self):
        if self.total_value == 21:
            return True
        else:
            return False
    
    def choose_action(self):
        print(f"{player.name}, hit(H) or stand(S)?")
        choice_made = False
        while (choice_made == False):
            choice = input()
            if (choice in possible_actions):
                self.action = choice.upper()
                choice_made = True
                break
            else:
                print("Invalid choice!")
                
    def discard(self):
        self.player_cards = []
        self.total_value = 0
        self.bet = 0
        
    def __str__(self):
        return f"{self.name} has {len(self.player_cards)} cards.\nTotal Value: {self.total_value}\nBank: {self.bank}$\nBet: {self.bet}$\n"
    
class Dealer:
    
    def __init__(self):
        # player_cards attribute is a list containing all the player's cards on the table (face up)
        self.dealer_cards = []
        self.total_value = 0
        
    def hit(self,new_card):
        self.dealer_cards.append(new_card)
        if (new_card.rank != 'Ace'):
            #If card is not an Ace, add to total value normally
            self.total_value += new_card.value
        elif (self.total_value >= 11):
            #If total value + 11 >= 21, count Ace as value 1
            new_card.value = 1
            self.total_value += new_card.value
        else:
            self.total_value += new_card.value
    
    def reveal_one_card(self):
        print("Dealer has:")
        time.sleep(1.5)
        print(self.dealer_cards[0])
        print("Total Value: ",self.dealer_cards[0].value,"\n")
        
    def display_cards(self):
        print("Dealer has:")
        for index in range(len(self.dealer_cards)):
            time.sleep(1.5)
            print(self.dealer_cards[index])
        print("Total value: ",self.total_value,"\n")
    
    def bust_condition(self):
        if self.total_value>21:
            return True
        else:
            return False
    
    def blackjack_condition(self):
        if self.total_value == 21:
            return True
        else:
            return False
    
    def discard(self):
        self.dealer_cards = []
        self.total_value = 0
        
    def __str__(self):
        for index in range(len(self.dealer_cards)):
            print(self.dealer_cards[index])
        return f"Dealer has {len(self.dealer_cards)} cards.\nTotal Value: {self.total_value}\n"

    
    
# GAME SETUP
win_condition = False
keep_playing = True
#Initialise deck and shuffle it
deck = Deck()
deck.shuffle()

#Initialise player and dealer
name = input("Choose your name: ")
player = Player(name,100)
dealer = Dealer()

while (keep_playing == True):
    #Start round
    while (win_condition == False):
        
        #Check if deck has at least 4 cards
        if len(deck.deck_cards)<=4:
            deck = Deck()
            deck.shuffle()
            
        #Discard previous cards
        player.discard()
        dealer.discard()
        
        print(player)
        player.place_bet()
        #Deal two cards to player and dealer
        player.hit(deck.deal_one())
        player.hit(deck.deal_one())

        dealer.hit(deck.deal_one())
        dealer.hit(deck.deal_one())

        #Reveal player's two cards and dealer's one card
        player.display_cards()
        dealer.reveal_one_card()

        #Player plays, choosing between hit (H) or stand (S)
        player.choose_action()

        #If player hits
        while (player.action == 'H'):

            #Check if deck has at least 1 card
            if len(deck.deck_cards)<=1:
                deck = Deck()
                deck.shuffle()
            
            player.hit(deck.deal_one())
            player.display_cards()

            #Check for bust
            if (player.bust_condition() == True):
                win_condition = True
                print(f"{player.name} you bust! Bank: {player.bank}$")
                break

            #Keep hitting?
            player.choose_action()

        if win_condition == True:
            break

        dealer.display_cards()
        #Check if beat player
        if (dealer.total_value > player.total_value):
            win_condition = True
            print(f"Dealer wins! {player.name} you lost! Bank: {player.bank}$")

        #Dealer's turn
        while (dealer.total_value < player.total_value):
            
            #Check if deck has at least 1 card
            if len(deck.deck_cards)<=1:
                deck = Deck()
                deck.shuffle()
            
            #Hit until beats player or until busts
            dealer.hit(deck.deal_one())
            dealer.display_cards()
            
            #Check for bust
            if (dealer.bust_condition() == True):
                win_condition = True
                player.bank = player.bank + player.bet*2
                print(f"Dealer busts! {player.name} you won! Bank: {player.bank}$")
            
            #Check if beat player
            elif (dealer.total_value > player.total_value):
                win_condition = True
                print(f"Dealer wins! {player.name} you lost! Bank: {player.bank}$")


        if win_condition == True:
            break

        if (player.total_value == dealer.total_value):
            player.bank += player.bet
            print(f"Both players won! Split pot! Bank: {player.bank}$")
            win_condition = True
    
    if player.bank == 0:
        print("Your bank is 0$!")
        break
    
    #Ask if player wants to keep playing
    choice_made = False
    while (choice_made == False):
        print(f"{player.name}, keep playing? (Y or N)")
        choice = input()
        if choice in keep_playing_choices:
            choice_made = True
        else:
            print("\nInvalid choice!")
    if choice.upper() == 'N':
        keep_playing = False
    elif choice.upper() == 'Y':
        win_condition = False
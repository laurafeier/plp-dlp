'''
Created on Sep 12, 2012

@author: lfeier
'''
#*******************************
#P1
#*******************************
from mx.DateTime.DateTime import TimeDelta
input_dict = {'a': 123, 'b': 456}
input_dict2 = {'a': (1,2,(2))}


def check_in_tuple(tup):
    for el in tup:
        print str(el) + " " + str(type(el))
        if type(el) in [list, set, dict]:
            return False
        elif type(el) is tuple:
            return check_in_tuple(el)
    return True

def test_swap_dict(input_dict):
    can_be_done =True
    for key in input_dict:
        if type(input_dict[key]) in [list, set, dict]:
            can_be_done = False
            break
        elif type(input_dict[key]) is tuple and not check_in_tuple(input_dict[key]):
            can_be_done = False
            break
    return can_be_done

print(test_swap_dict(input_dict))

#*******************************
#P2
#*******************************
from random import shuffle
from operator import attrgetter
class Card:
    """ abstract class 4 cards """
    TYPE = {0: "spade", 1: "heart", 2: "diamond", 3: "club"}
    
    def __init__(self, type_card, number):
        self.__type_card = type_card
        self.__number = number 
    
    def str_pretty_print(self):
        return self.__type_card + str(self.__number)
    
    def getnumber(self):
        return self.__number
    
    def gettype_card(self):
        return self.__type_card
    
class CardDealer:
    """ card dealer """
    def __init__(self):
        print "building deck..."
        self.__cards = []
        for i in range(1,14):
            for key in Card.TYPE:
                self.__cards.append(Card(Card.TYPE[key],i))        
        print self.str_pretty_print_cards()
        print "deck built"
        
    def shuffle_cards(self):
        print "shuffle cards"
        shuffle(self.__cards)

    def sort_cards(self):
        print "sort cards"
        self.__cards = sorted(self.__cards, key=attrgetter("gettype_card","getnumber"))
    
    def send_cards(self, no_of_cards):
        print "sending "+ str(no_of_cards) + " cards from deck"
        cards_to_send = []
        for i in range(no_of_cards):
            cards_to_send.append(self.__cards.pop())
        print "sending " + str(self.str_pretty_print_cards(cards_to_send))
        return cards_to_send
        
    def str_pretty_print_cards(self, arr_of_cards = None):
        if arr_of_cards is None:
            return [card.str_pretty_print() for card in self.__cards]
        return [card.str_pretty_print() for card in arr_of_cards]
        
class Player:
    """ cards player """ 
    def __init__(self, some_id):
        self.id = some_id   
    
    def receive_cards(self, cards):
        print "player " + str(self.id) + " receives cards"
        self.__cards = cards
    
    def getid(self):
        return self.id

class Game:
    """ abstract object used only to register players and dealer""" 
    def __init__(self, no_of_players):
        self.__dealer = CardDealer()
        self.__players = []
        for el in range(no_of_players):
            self.__players.append(Player(el))
    
    def start_game(self):
        print "players" +  str([pl.id for pl in self.__players])            

        self.__dealer.sort_cards()
        print self.__dealer.str_pretty_print_cards()
        self.__dealer.shuffle_cards()
        print self.__dealer.str_pretty_print_cards()
        
        print "send cards to player"
        for player in self.__players:
            player.receive_cards(self.__dealer.send_cards(2))
        
        print "draw the table hand of 5 cards"
        self.__dealer.send_cards(5)
        
        print "cards left in deck: " + str(self.__dealer.str_pretty_print_cards())
            
game = Game(3)
game.start_game()


#*******************************
#P3
#*******************************
from datetime import datetime
from datetime import timedelta
from time import sleep

def time_slow(threshold = 0.05):
    def _time_slow(function):
        def inner(*args, **kwargs):
            start = datetime.now()
            function(*args, **kwargs)
            duration = datetime.now() - start
            
            inner.__name__ = function.__name__
            inner.__doc__ = function.__doc__
            inner.__dict__.update(function.__dict__)
            
            if duration > timedelta(seconds = threshold) :
                print function.__name__ + " took long enough " + str(duration)
        return inner
    return _time_slow

@time_slow(threshold = 0.05)
def fast_method(sleep_sec):
    print "in fast method"
    sleep(sleep_sec) 
    print "out fast method"
    
fast_method(0.05)
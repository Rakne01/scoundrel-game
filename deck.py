from constants import RANKS, SUITS
import random

########################CARD FUNCTIONS##################################
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)
    
    def __str__(self):
        face_values = {
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14
        }
        
        if self.rank in face_values:
            return f"{self.rank} of {self.suit} ({face_values[self.rank]})"
        else:
            return f"{self.rank} of {self.suit}"
    
########################DECK FUNCTIONS##################################
class Deck:
    def __init__(self):
        self.cards = []
        red_suits = ["Diamonds", "Hearts"]
        face_and_ace = ["Jack", "Queen", "King", "Ace"]
        # Generate all 52 cards
        for suit in SUITS:
            for rank in RANKS:
                if suit in red_suits and rank in face_and_ace:
                    continue

                card = Card(rank, suit)
                self.cards.append(card)
        # Shuffle the deck
        random.shuffle(self.cards)
    
    def draw(self):
        # Remove and return the top card
        if len(self.cards) > 0:
            return self.cards.pop()
        return None  # or raise an exception if deck is empty
    
    def cards_remaining(self):
        return len(self.cards)
    
    def return_to_bottom(self, cards):
        # Add cards to the bottom of the deck
        for card in cards:
            self.cards.insert(0, card)
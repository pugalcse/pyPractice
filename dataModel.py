import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

    def upper(self, cards):
        return [card for card in cards if card.rank in 'JQKA']  
    
    def reversed(self, cards):
        return reversed(cards)  
    
    def sorted(self, cards):
        return sorted(cards, key=self.spades_high)

    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        print(f"Rank: {card.rank}, Suit: {card.suit}, Rank Value: {rank_value}, Suit Value: {FrenchDeck.suit_values[card.suit]}")
        return rank_value * len(FrenchDeck.suits) + FrenchDeck.suit_values[card.suit]
    
deck = FrenchDeck()
print(len(deck))
deck_sorted = deck.sorted(deck._cards)
for card in deck_sorted:
    print(card)
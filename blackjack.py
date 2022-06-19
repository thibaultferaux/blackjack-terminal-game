from random import randint


# create a blackjack terminal game

class Player:
    def __init__(self, _name):
        self.name = _name
        self.count = 0
    
    def draw_card(self):
        card = randint(1, 14)
        self.count += card
        return print(f'{self.name}, you drew a {card}. Your total is {self.count}.')
    
    def get_count(self):
        return print(f'{self.name}, your total is {self.count}.');

class Dealer:
    def __init__(self,):
        self.count = 0
    
    def draw_card(self):
        self.count += randint(1, 14)

    def get_count(self):
        return print(f'The dealers total is {self.count}.');

class Card:
    def __init__(self, _suit, _value):
        self.suit = _suit
        self.value = _value
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))


class Blackjack:
    def __init__(self, _player):
        self.deck = Deck()
        self.player = Player(_player)
        self.dealer = Dealer()
        self.dealer.draw_card()
        self.player.draw_card()
        self.play()

    def play(self):
        while True:
            choice = input('Hit or stand?\n>> ').lower()
            if choice == 'hit':
                self.player.draw_card()
                if self.player.count > 21:
                    print('You busted!')
                    break
            elif choice == 'stand':
                self.dealer.draw_card()
                self.dealer.get_count()
                if self.dealer.count > 21:
                    print('Dealer busted!')
                    break
                while self.dealer.count < 17:
                    self.dealer.draw_card()
                    self.dealer.get_count()
                    if self.dealer.count > 21:
                        print('Dealer busted!')
                        break
                if self.dealer.count > self.player.count:
                    print('Dealer wins!')
                elif self.dealer.count < self.player.count:
                    print('You win!')
                else:
                    print('Tie!')
                break
            else:
                print('Invalid choice!')

if __name__ == '__main__':
    print("""\
     ____  _        _    ____ _  __   _   _    ____ _  __
    | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /
    |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' / 
    | |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \ 
    |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\ 
                                                      
        """);
    player_name = input('What\'s your name\n>> ')
    Blackjack(player_name)
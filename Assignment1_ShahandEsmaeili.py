from enum import Enum


class Card:
    class CardValue(Enum):
        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13

    class CardSuit(Enum):
        SPADES = 1
        HEARTS = 2
        DIAMONDS = 3
        CLUBS = 4

    DEFAULT_VAL = CardValue(3)
    DEFAULT_SUIT = CardSuit(4)

    def __init__(self, value=DEFAULT_VAL, suit=DEFAULT_SUIT):
        self.value = value
        self.suit = suit
        self.set(value, suit)

    def __str__(self):
        if self.error_flag:
            return "Invalid suit and value combination"

        else:
            string = self.value.name + " of " + self.suit.name
            return string

    def set(self, value, suit):
        self.error_flag = Card.valid_card(value, suit)

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getErrorFlag(self):
        return self.error_flag

    def equals(self, other_card):
        if (self.value == other_card.value
                and self.suit == other_card.suit
                and self.error_flag == other_card.error_flag):
            return True

        else:
            return False

    @classmethod
    def valid_card(cls, value, suit):
        try:
            v = value.name
            s = suit.name

        except AttributeError:
            v = value
            s = suit

        if (v not in cls.CardValue.__members__ or
                s not in cls.CardSuit.__members__):
            return True


        else:
            return False


class Hand:
    MAX_CARDS_PER_HAND = 50

    def __init__(self):
        self.my_cards = []
        self.num_cards = 0

    def reset_hand(self):
        self.my_cards.clear()
        self.num_cards = 0

    def take_card(self, card):
        if not card.error_flag and self.num_cards < Hand.MAX_CARDS_PER_HAND:
            self.my_cards.append(card)
            self.num_cards += 1
            return True

        if card.error_flag:
            return True

        else:
            return False

    def play_card(self):
        if (self.num_cards > 0):
            self.num_cards -= 1
            return self.my_cards.pop()

        else:
            return None

    def __str__(self):
        if (self.num_cards > 0):
            return ''.join(str(c) + ', ' for c in self.my_cards)

        else:
            return str(None)

    def getNumCards(self):
        return self.num_cards

    def inspect_card(self, k):
        if (k < self.num_cards):
            card = self.my_cards[k]
            return card

        else:
            card = Card("JOKER", "APPLE")
            return card


def test_Card():
    Card1 = Card()
    Card2 = Card(Card.CardValue.ACE, Card.CardSuit.SPADES)
    Card3 = Card("JOKER", "APPLE")
    print(Card1)
    print(Card2)
    print(Card3)


def test_hand():
    hand = Hand()
    Card1 = Card()
    Card2 = Card(Card.CardValue.ACE, Card.CardSuit.SPADES)
    Card3 = Card("JOKER", "APPLE")

    print()
    print()

    while hand.getNumCards() < 50:
        hand.take_card(Card1)
        hand.take_card(Card2)
        hand.take_card(Card3)

    print("Hand = (", end=" ")
    print(hand, end=" ")
    print(")")
    print()
    print()

    while hand.getNumCards() > 0:
        print(hand.play_card())

    print()
    print()
    print("Hand = (", end=" ")
    print(hand, end=" ")
    print(")")


if __name__ == "__main__":
    test_Card()
    test_hand()

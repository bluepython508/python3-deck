import pydeck.deck as deck


class TCGCard:
    def __init__(self, data, **kwdata):
        data.update(kwdata)
        self.card = data


class TCGDeck(deck.PartialDeck):
    def __init__(self, *carddata):
        cards = []
        for card in carddata:
            cards.append(card)
        super().__init__(cards)

    def shuffle(self):

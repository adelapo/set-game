import tkinter as tk
from Card import Card
import random


class GameFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.deck = []
        self.shown_cards = []
        self.load_set()

        self.selection = []

        self.score = 0

    def load_set(self):
        self.deck = []

        COLORS = ["red", "green", "blue"]
        FONTS = ["Times", "Arial", "Comic Sans MS"]
        SHAPES = ["A", "B", "C"]

        for color in COLORS:
            for font in FONTS:
                for shape in SHAPES:
                    for number in range(1, 4):
                        card = Card(self, number, color, font, shape)
                        self.deck.append(card)

        random.shuffle(self.deck)

    def card_selected(self, card):
        if card in self.selection:
            self.selection.remove(card)
        else:
            self.selection.append(card)

        if len(self.selection) == 3:
            if self.is_set(self.selection):
                self.set_found()
            else:
                self.set_not_found()

    def add_card(self, card, row, column):
        print(self.grid_slaves(row, column))
        card.grid(row=row, column=column, padx=10, pady=10)

    @staticmethod
    def is_set(cards):
        if len(cards) != 3:
            return False

        colors = set([card.color for card in cards])
        fonts = set([card.font for card in cards])
        shapes = set([card.shape for card in cards])
        numbers = set([card.number for card in cards])

        return len(colors) != 2 and len(fonts) != 2 and len(shapes) != 2 and len(numbers) != 2

    def set_found(self):
        print("HOORAY!")

    def set_not_found(self):
        print("BOO.")

    def get_next_card(self):
        return self.deck.pop(0)

    def replace_card(self, old_card):
        new_card = self.get_next_card()
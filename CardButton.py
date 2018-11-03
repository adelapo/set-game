import tkinter as tk


class CardButton(tk.Button):
    def __init__(self, card, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.is_clicked = False

        self.config(text=str(card))

    def clicked(self):
        self.is_clicked = not self.is_clicked


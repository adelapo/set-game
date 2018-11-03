import tkinter as tk

CARD_WIDTH = 160
CARD_HEIGHT = 80
SPACING = 30


class Card(tk.Button):

    width = 160
    height = 80

    def __init__(self, parent, number, color, font, shape):
        self.parent = parent

        self.number = number
        self.color = color
        self.font = font
        self.shape = shape

        self.is_clicked = False

        invisible_image = tk.PhotoImage(width=1, height=1)

        tk.Button.__init__(self, parent, width=self.width, height=self.height, bg="white", relief="solid",
                           text=shape*number, font=(font, 32, "bold"), fg=color, command=self.clicked,
                           image=invisible_image, compound="c")

        self.image = invisible_image

    def clicked(self):
        self.is_clicked = not self.is_clicked

        if self.is_clicked:
            self.config(bg="gray")
        else:
            self.config(bg="white")

        self.parent.card_selected(self)

    def __str__(self):
        return self.color + " " + self.shape * self.number + " (" + self.font + ")"

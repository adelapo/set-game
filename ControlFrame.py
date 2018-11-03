import tkinter as tk


class ControlFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.title_label = tk.Label(self, text="Set", font=("Arial", 32, "bold"))
        self.title_label.pack()

        self.score_label = tk.Label(self, text="Score: 0", font=("Arial", 20))
        self.score_label.pack()

        self.num_cards_label = tk.Label(self, text="Cards Remaining: 0", font=("Arial", 20))
        self.num_cards_label.pack(side="bottom")

    def update_score(self, score):
        self.score_label.config(text="Score: " + str(score))

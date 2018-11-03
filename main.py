import tkinter as tk
from ControlFrame import ControlFrame
from GameFrame import GameFrame

root = tk.Tk()

game_frame = GameFrame(root)
game_frame.pack(side="left")

for i in range(12):
    row = i // 3
    col = i % 3
    card = game_frame.deck[i]
    game_frame.add_card(card, row=row, column=col)

next_card = game_frame.get_next_card()


control_frame = ControlFrame(root)
control_frame.pack(side="right", fill="y")

root.mainloop()

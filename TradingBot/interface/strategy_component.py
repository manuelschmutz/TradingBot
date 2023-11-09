import tkinter as tk
import typing
from interface.styling import *


class StrategyEditor(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.commands_frame = tk.Frame(self, bg=BG_COLOR)
        self.commands_frame.pack(side=tk.TOP)

        self.table_frame = tk.Frame(self, bg=BG_COLOR)
        self.table_frame.pack(side=tk.TOP)

        self.add_button = tk.Button(self.commands_frame, text="Add strategy", font=GLOBAL_FONT,
                                    command=self.add_strategy_row, bg=BG_COLOR_2, fg=FG_COLOR)
        
        self.add_button.pack(side=tk.TOP)

        self.body_widgets = dict()

        self.headers = ["Strategy", "Contract", "Timeframe", "Balance %", "TP %", "SL %"]

        for idx, h in enumerate(self.headers):
            header = tk.Label(self.table_frame, text=h.capitalize(), 
                              bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
            header.grid(row=0, column=idx)

        for h in self.headers:
            self.body_widgets[h] = dict() 

        self.body_index = 1


    def add_strategy_row(self):
        return
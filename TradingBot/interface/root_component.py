import tkinter as tk
from interface.styling import *
from interface.logging_component import Logging
from connectors.binance_futures import BinanceFuturesClient

class Root(tk.Tk):
    def __init__(self, binance: BinanceFuturesClient):
        super().__init__()

        self.binance = binance

        self.title("Trading Bot")
        self.configure(bg=BG_COLOR)

        self.left_frame = tk.Frame(self, bg=BG_COLOR)
        self.left_frame.pack(side=tk.LEFT)

        self.right_frame = tk.Frame(self, bg=BG_COLOR)
        self.right_frame.pack(side=tk.LEFT)

        self.logging_frame = Logging(self.left_frame, bg=BG_COLOR)
        self.logging_frame.pack(side=tk.TOP)

        self._update_ui()

    def _update_ui(self):
        for log in self.binance.logs:
            if not log['displayed']:
                self.logging_frame.add_log(log['log'])
                log['displayed'] = True

        self.after(1500, self._update_ui)

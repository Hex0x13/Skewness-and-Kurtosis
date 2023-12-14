from typing import Optional, Tuple, Union
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import matplotlib.pyplot as plt
from data import DataScreen
from result import *


class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry('1000x620')
        self.title('Skewness and Kurtosis Calculator')

        pack_screen = {
            'expand': True,
            'fill': 'both',
            'side': ctk.LEFT
        }

        self.data_frame = DataScreen(self)
        self.result_frame = ResultScreen(self)

        self.data_frame.pack(**pack_screen)
        self.result_frame.pack(**pack_screen)

        self.data_frame.result_btn.configure(command=lambda: generate_result(self))
    
    def resize(self, event):
        width = event.width // 2
        self.data_frame.configure(width=width)
        self.result_frame.configure(width=width)

    def close(self):
        if self.result_frame.histfigure:
            plt.close(self.result_frame.histfigure)
        self.destroy()
        self.quit()
        

if __name__ == '__main__':
    app = App()
    app.protocol("WM_DELETE_WINDOW",app.close)
    app.mainloop()

from typing import Optional, Tuple, Union
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from screenmanager import ScreenManager
import matplotlib.pyplot as plt
from header import HeaderSection
from data import DataScreen
from result import *


class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry('860x600')

        pack_screen = {
            'expand': True,
            'fill': 'both'
        }

        self.screenmanager = ScreenManager()
        self.header = HeaderSection(self, self.screenmanager)
        self.header.pack(pady=10)

        self.data_frame = DataScreen(self)
        self.result_frame = ResultScreen(self)

        self.screenmanager.add_screen('data_screen', self.data_frame, **pack_screen)
        self.screenmanager.add_screen('result_screen', self.result_frame, **pack_screen)

        self.screenmanager.set_current('data_screen')
        self.data_frame.result_btn.configure(command=lambda: generate_result(self))
    
    def close(self):
        if self.result_frame.histfigure:
            plt.close(self.result_frame.histfigure)
        self.destroy()
        self.quit()
        

if __name__ == '__main__':
    app = App()
    app.protocol("WM_DELETE_WINDOW",app.close)
    app.mainloop()

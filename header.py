from typing import Optional, Tuple, Union
from screenmanager import ScreenManager
import customtkinter as ctk


def change_screen(value, screenmanager):
    if value == 'data':
        screenmanager.set_current('data_screen')
    elif value == 'result':
        screenmanager.set_current('result_screen')
    elif value == 'formula':
        screenmanager.set_current('formula_screen')



class HeaderSection(ctk.CTkFrame):
    def __init__(self, master: any, screenmanager: ScreenManager, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.screen_opt = ['data', 'result', 'formula']

        self.segemented_button = ctk.CTkSegmentedButton(
            self,
            values=self.screen_opt,
            command=lambda value: change_screen(value, screenmanager=screenmanager)
        )
        self.segemented_button.set(self.screen_opt[0])
        self.segemented_button.pack()

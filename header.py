from typing import Optional, Tuple, Union
from screenmanager import ScreenManager
import customtkinter as ctk


class HeaderSection(ctk.CTkFrame):
    def __init__(self, master: any, screenmanager: ScreenManager, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.screen_opt = ['Data', 'Result']
        self.__screenmanager = screenmanager

        self.segemented_button = ctk.CTkSegmentedButton(
            self,
            values=self.screen_opt,
            command=lambda value: self.change_screen(value),
            width=400,
            font=ctk.CTkFont(size=14)
        )
        self.segemented_button.set(self.screen_opt[0])
        self.segemented_button.pack()
        self.segemented_button.pack_propagate(False)

    def change_screen(self, value):
        if value == self.screen_opt[0]:
            self.__screenmanager.set_current('data_screen')
        elif value == self.screen_opt[1]:
            self.__screenmanager.set_current('result_screen')

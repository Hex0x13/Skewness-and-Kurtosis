from typing import Optional, Tuple, Union
import customtkinter as ctk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from solution import *
from text_to_array import text_to_float_array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResultScreen(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.inner_frame = ctk.CTkLabel(self, text='No Result')
        self.inner_frame.pack(expand=True)
        self.histfigure = None


class FormulaScreen(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.inner_frame = ctk.CTkLabel(self, text='Formula')
        self.inner_frame.pack(expand=True)


def generate_result(result_frame: ResultScreen, textbox: ctk.CTkTextbox):
    if isinstance(result_frame.inner_frame, ctk.CTkLabel):
        result_frame.inner_frame.destroy()
        result_frame.inner_frame = ctk.CTkFrame(result_frame)
        result_frame.inner_frame.pack(expand=True, fill='both')

    data = np.array(sorted(text_to_float_array(textbox.get('1.0', 'end'))))
    
    result_frame.histfigure, ax = plt.subplots()
    sns.histplot(data, kde=True, ax=ax)
    ax.set_title("Skewness & Kurtosis")
    ax.set_ylabel("Frequency")
    ax.set_xlabel("Values")

    canvas = FigureCanvasTkAgg(result_frame.histfigure, master=result_frame.inner_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True)

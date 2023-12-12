from typing import Tuple
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
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


def generate_result(root):
    text = root.data_frame.textbox.get('1.0', 'end').strip(' \n\t')
    data = text_to_float_array(text)

    if text and data:
        if isinstance(root.result_frame.inner_frame, ctk.CTkLabel):
            root.result_frame.inner_frame.destroy()
            root.result_frame.inner_frame = ctk.CTkFrame(root.result_frame)
            root.result_frame.inner_frame.pack(expand=True, fill='both')

        data = np.array(data)
        root.result_frame.histfigure, ax = plt.subplots()
        sns.histplot(data, kde=True, ax=ax)
        ax.set_title("Skewness & Kurtosis")
        ax.set_ylabel("Frequency")
        ax.set_xlabel("Values")

        canvas = FigureCanvasTkAgg(root.result_frame.histfigure, master=root.result_frame.inner_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)
    elif not text:
        CTkMessagebox(root, title='Warning', message='Textbox is Empty!')
    else:
        CTkMessagebox(root, title='Warning', message='Invalid Input!')

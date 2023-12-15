from typing import Tuple
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from solution import *
from text_to_array import text_to_float_array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResultScreen(ctk.CTkScrollableFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.__default_innerframe()
        self.histfigure = None
    
    def set_innerframe_to_default(self):
        if self.histfigure:
            plt.close(self.histfigure)
        self.inner_frame.destroy()
        self.__default_innerframe()
    
    def __default_innerframe(self):
        self.inner_frame = ctk.CTkLabel(self, text='No Result', fg_color='transparent', font=ctk.CTkFont(size=18, weight='bold'))
        self.inner_frame.grid(row=0, column=0, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


def generate_result(root):
    text = root.data_frame.textbox.get('1.0', 'end').strip(' \n\t')
    data = text_to_float_array(text)

    if text and data:
        if root.result_frame.inner_frame:
            if root.result_frame.histfigure:
                plt.close(root.result_frame.histfigure)
            root.result_frame.inner_frame.destroy()
            root.result_frame.inner_frame = ctk.CTkFrame(root.result_frame)
            root.result_frame.inner_frame.pack(expand=True, fill='both', anchor=ctk.N)

        data = np.array(data)
        root.result_frame.histfigure, ax = plt.subplots()
        sns.histplot(data, kde=True, ax=ax)
        ax.set_title("Skewness & Kurtosis")
        ax.set_ylabel("Frequency")
        ax.set_xlabel("Values")

        canvas = FigureCanvasTkAgg(root.result_frame.histfigure, master=root.result_frame.inner_frame)
        canvas.draw()
        canvas.get_tk_widget().configure(width=500, height=400)
        canvas.get_tk_widget().pack(pady=(80, 20))

        skewness = skew(data)
        kurtosis = kurt(data)

        skew_frame = ctk.CTkFrame(root.result_frame.inner_frame)
        skew_frame.pack(ipadx=10, ipady=10)
        skew_label = ctk.CTkLabel(skew_frame, text='Skewness:', font=ctk.CTkFont(size=24, weight='bold'))
        skew_label.pack(anchor='w', pady=(5, 10), padx=10)
        label_font = ctk.CTkFont(size=14)
        
        for k, v in skewness.items():
            if isinstance(v, dict) and v:
                first_key = list(v.keys())[0]
                label = ctk.CTkLabel(skew_frame, text=f'{k.title()}:   {v[first_key]}', font=label_font)

                mode_frame = ctk.CTkFrame(skew_frame, fg_color='transparent')
                mode_frame.pack(anchor='w')

                mode_label = ctk.CTkLabel(mode_frame, text='Select Mode:', font=label_font)
                mode_label.pack(side=ctk.LEFT, padx=(20, 10))

                modes_menu = ctk.CTkComboBox(mode_frame, width=100, values=[str(x) for x in v.keys()], state='readonly')
                modes_menu.pack(side=ctk.LEFT)
                modes_menu.set(str(first_key))
                modes_menu.configure(command=lambda e, label=label, k=k, v=v: label.configure(text=f'{k}: {v[float(e)]}'))
                label.pack(anchor='w', padx=20)
            else:
                val = 'No Modal' if isinstance(v, dict) and not v else v
                label = ctk.CTkLabel(skew_frame, text=f'{k.title()}:   {val}', font=label_font)
                label.pack(anchor='w', padx=20, pady=2)
        

        kurt_frame = ctk.CTkFrame(root.result_frame.inner_frame)
        kurt_frame.pack(ipadx=10, ipady=10, pady=20)
        kurt_label = ctk.CTkLabel(kurt_frame, text='Kurtosis:', font=ctk.CTkFont(size=24, weight='bold'))
        kurt_label.pack(anchor='w', pady=(5, 10), padx=10)

        for k, v in kurtosis.items():
            label = ctk.CTkLabel(kurt_frame, text=f'{k}:   {v}', font=label_font)
            label.pack(anchor='w', padx=20, pady=2)

    elif not text:
        CTkMessagebox(root, title='Warning', message='Textbox is Empty!')
        root.result_frame.set_innerframe_to_default()
    else:
        CTkMessagebox(root, title='Warning', message='Invalid Input!')
        root.result_frame.set_innerframe_to_default()


def clear_input(root):
    root.data_frame.textbox.delete('1.0', 'end')
    root.result_frame.set_innerframe_to_default()

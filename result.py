import customtkinter as ctk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from solution import *
from text_to_array import text_to_float_array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def result_section(root, **kwargs):
    result_frame = ctk.CTkFrame(root, **kwargs)
    # ctk.CTkLabel(result_frame, text='No Result').pack(expand=True)
    return result_frame


def formula_section(root, **kwargs):
    formula_frame = ctk.CTkFrame(root, **kwargs)
    ctk.CTkLabel(formula_frame, text='Formula').pack(expand=True)
    return formula_frame


def generate_result(result_frame: ctk.CTkFrame, textbox: ctk.CTkTextbox):
    data = np.array(sorted(text_to_float_array(textbox.get('1.0', 'end'))))

    histplot = sns.histplot(data, kde=True)

    fig, ax = plt.subplots()
    sns.histplot(data, kde=True, ax=ax)
    ax.set_title("Skewness & Kurtosis")
    ax.set_ylabel("Frequency")
    ax.set_xlabel("Values")
    
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True)

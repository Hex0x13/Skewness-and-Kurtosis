from screenmanager import ScreenManager
import customtkinter as ctk


def change_screen(value, screenmanager):
    if value == 'data':
        screenmanager.set_current('data_screen')
    elif value == 'result':
        screenmanager.set_current('result_screen')
    elif value == 'formula':
        screenmanager.set_current('formula_screen')


def header_section(root, screenmanager: ScreenManager, **kwargs):
    header_frame = ctk.CTkFrame(root, **kwargs)
    screen_opt = ['data', 'result', 'formula']

    segemented_button = ctk.CTkSegmentedButton(
        header_frame,
        values=screen_opt,
        command=lambda value: change_screen(value, screenmanager=screenmanager)
    )
    segemented_button.set(screen_opt[0])
    segemented_button.pack()

    return header_frame

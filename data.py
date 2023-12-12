from typing import Optional, Tuple, Union
import customtkinter as ctk
from text_to_array import sanitize_input


class DataScreen(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        textbox_style = {
            'width': 600,
            'height': 300,
            'fg_color': 'white',
            'corner_radius': 10,
            'text_color': 'black',
            'border_color': 'black',
            'border_width': 1,
            'border_spacing': 15,
            'font': ctk.CTkFont(size=16)
        }
        button_frame_style = {
            'fg_color': 'transparent',
            'height': 50,
        }

        # Container for textbox and textbox label
        self.input_frame = ctk.CTkFrame(self, width=600, fg_color='transparent')
        self.input_frame.pack(expand=True)

        self.textbox = ctk.CTkTextbox(self.input_frame, **textbox_style)
        self.textbox.pack(expand=True)
        self.textbox.pack_propagate(False)

        self.input_label = ctk.CTkLabel(self.input_frame, text='comma separated input values')
        self.input_label.pack(anchor=ctk.E, padx=(0, 10))

        # Container for buttons
        self.button_frame = ctk.CTkFrame(self.input_frame, **button_frame_style)
        self.button_frame.pack(fill='x')

        self.clear_btn = ctk.CTkButton(self.button_frame, text='Clear')
        self.clear_btn.pack(side=ctk.LEFT)

        self.result_btn = ctk.CTkButton(self.button_frame, text='Generate Result')
        self.result_btn.pack(side=ctk.RIGHT, padx=10, pady=10)

        self.sanitize_btn = ctk.CTkButton(self.button_frame, text='Sanitize Input', command=lambda: replace_text(self.textbox))
        self.sanitize_btn.pack(side=ctk.RIGHT)


def replace_text(textbox: ctk.CTkTextbox):
    replacement_text = sanitize_input(textbox.get('1.0', 'end'))
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', replacement_text)

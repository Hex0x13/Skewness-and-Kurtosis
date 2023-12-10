import customtkinter as ctk
from text_to_array import sanitize_input


def data_section(root, **kwargs):
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

    data_frame = ctk.CTkFrame(root, **kwargs)

    input_frame = ctk.CTkFrame(data_frame, width=600, fg_color='transparent')
    input_frame.pack(expand=True)

    textbox = ctk.CTkTextbox(input_frame, **textbox_style)
    textbox.pack(expand=True)
    textbox.pack_propagate(False)

    input_label = ctk.CTkLabel(
        input_frame, text='comma separated input values')
    input_label.pack(anchor=ctk.E, padx=(0, 10))

    button_frame = ctk.CTkFrame(input_frame, **button_frame_style)
    button_frame.pack(fill='x')

    result_btn = ctk.CTkButton(button_frame, text='Generate Result')
    result_btn.pack(side=ctk.RIGHT, padx=10, pady=10)

    sanitize_btn = ctk.CTkButton(button_frame, text='Sanitize Input',
        command=lambda: replace_text(textbox))
    sanitize_btn.pack(side=ctk.RIGHT)

    return data_frame, result_btn, textbox

def replace_text(textbox: ctk.CTkTextbox):
    replacement_text = sanitize_input(textbox.get('1.0', 'end'))
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', replacement_text)

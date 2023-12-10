import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from screenmanager import ScreenManager
from header import header_section
from data import data_section
from result import *


def main():
    root = ctk.CTk()
    root.geometry('860x600')

    pack_screen = {
        'expand': True,
        'fill': 'both'
    }
    screenmanager = ScreenManager()
    header = header_section(root, screenmanager)
    header.pack()

    data_frame, result_btn, textbox = data_section(root)
    result_frame = result_section(root)
    formula_frame = formula_section(root)

    screenmanager.add_screen('data_screen', data_frame, **pack_screen)
    screenmanager.add_screen('result_screen', result_frame, **pack_screen)
    screenmanager.add_screen('formula_screen', formula_frame, **pack_screen)

    screenmanager.set_current('data_screen')
    result_btn.configure(command=lambda: generate_result(result_frame, textbox))

    root.mainloop()


if __name__ == '__main__':
    main()



# from solution import *
# from text_to_array import textfile_to_farray, sanitize_input

# if __name__ == '__main__':
#     data1 = np.array(textfile_to_farray('./dataset1'))
#     print(*[f'{k}: {v}' for k, v in central_tendency(data1).items()], sep='\n')
#     print(*[f'{k}: {v}' for k, v in measure_of_location(data1).items()], sep='\n')
#     print(*[f'{k}: {v}' for k, v in measure_of_dispersion(data1).items()], sep='\n')
#     print(*[f'{k}: {v}' for k, v in skew(data1).items()], sep='\n')
#     print(*[f'{k}: {v}' for k, v in kurt(data1).items()], sep='\n')
#     smaple_m = sample_moment(data1)
#     print("Skew:", smaple_m['skew'])
#     print("Kurt:", smaple_m['kurt'])

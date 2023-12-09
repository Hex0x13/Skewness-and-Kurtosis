import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class ScreenManager:
    def __init__(self, screens={}) -> None:
        if not isinstance(screens, dict):
            raise Exception
        self.__screens = screens
        self.__current = None
    
    def set_current(self, key):
        screen = self.__screens.get(key)
        if screen and screen is not self.__current:
            if self.__current:
                self.__current.pack_forget()
            self.__current = screen[0]
            self.__current.pack(**screen[1])
    
    def get_current(self):
        return self.__current
    
    def add_screen(self, key, value, **kwargs):
        self.__screens[key] = [value, kwargs]

    def remove_screen(self, key):
        to_remove = self.__screens.pop(key)
        if to_remove:
            to_remove[0].destroy()


def change_screen(value, screenmanager):
    if value == 'data':
        screenmanager.set_current('data_screen')
    elif value == 'skewness':
        screenmanager.set_current('skew_screen')
    elif value == 'kurtosis':
        screenmanager.set_current('kurt_screen')


def header_section(root, screenmanager: ScreenManager, **kwargs):
    header_frame = ctk.CTkFrame(root, **kwargs)
    screen_opt = ['data', 'skewness', 'kurtosis']

    segemented_button = ctk.CTkSegmentedButton(
        header_frame,
        values=screen_opt,
        command=lambda value: change_screen(value, screenmanager=screenmanager)
    )
    segemented_button.set(screen_opt[0])
    segemented_button.pack()

    return header_frame


def data_section(root, **kwargs):
    data_frame = ctk.CTkFrame(root, **kwargs)
    ctk.CTkLabel(data_frame, text='Data Section').pack(expand=True)
    return data_frame


def skew_section(root, **kwargs):
    skew_frame = ctk.CTkFrame(root, **kwargs)
    ctk.CTkLabel(skew_frame, text='Skewness Section').pack(expand=True)
    return skew_frame


def kurt_section(root, **kwargs):
    kurt_frame = ctk.CTkFrame(root, **kwargs)
    ctk.CTkLabel(kurt_frame, text='Kurtosis Section').pack(expand=True)
    return kurt_frame


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
    
    data_frame = data_section(root)
    skew_frame = skew_section(root)
    kurt_frame = kurt_section(root)

    screenmanager.add_screen('data_screen', data_frame, **pack_screen)
    screenmanager.add_screen('skew_screen', skew_frame, **pack_screen)
    screenmanager.add_screen('kurt_screen', kurt_frame, **pack_screen)

    screenmanager.set_current('data_screen')

    root.mainloop()


if __name__ == '__main__':
    main()

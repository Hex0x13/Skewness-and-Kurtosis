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

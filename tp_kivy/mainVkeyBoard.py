from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

Builder.load_file('VkeyBoard.kv')

class MyVKeyboard(VKeyboard):
    pass

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'

        layout = GridLayout(cols=1)

        keyboard = MyVKeyboard(on_key_up=self.key_up)

        self.label = Label(text="Type Something", font_size="20sp")
        self.shift_pressed = False
        self.caps_lock = False

        layout.add_widget(self.label)
        layout.add_widget(keyboard)

        return layout

    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]

        thing = self.label.text

        if thing == "Type Something":
            thing = ''

        if keycode == 'backspace':
            thing = thing[:-1]
            keycode = ''
        elif keycode == 'spacebar':
            keycode = ' '
        elif keycode == 'enter':
            keycode = '\n'
        elif keycode == 'escape':
            self.label.text = ''
            return
        elif keycode == 'shift':
            self.shift_pressed = not self.shift_pressed
            return
        elif keycode == 'capslock':
            self.caps_lock = not self.caps_lock
            return

        if self.caps_lock or self.shift_pressed:
            keycode = keycode.upper()
            self.shift_pressed = False
        else:
            keycode = keycode.lower()

        self.label.text = f'{thing}{keycode}'


if __name__ == '__main__':
    MainApp().run()


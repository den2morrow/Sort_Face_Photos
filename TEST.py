

from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.button import Button

kv=Builder.load_string('''
BoxLayout:
    GridLayout:
        id:grid_button
        cols:1
        Button:
            text:'2'
''')

class Accounting(App):
    def build(self):
        return kv
    def on_start(self):
        for a in range(2):
#I want to put these buttons above the button (2) in grid layout
            self.root.ids.grid_button.add_widget(Button(text=str(a)), index=1)

Accounting().run()
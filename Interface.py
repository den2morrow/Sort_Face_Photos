from kivy.app import App

from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config
Config.set('graphics', 'resizable', False)

class MyApp(App):

    def build(self):
        box = FloatLayout()
        buttonImage = Button(text='Фотография',size_hint = [0.6,0.6],pos = [0,300])
        buttonСhoiceImage = Button(text='Выбрать фото',size_hint = [0.2,0.1],pos =[600, 500])
        buttonTakeImage = Button(text='Сделать фото',size_hint = [0.2,0.1], pos = [600,400])
        buttonStart = Button(text='Страрт',size_hint = [0.3,0.1], pos = [300,150])
        box.add_widget(buttonImage)
        box.add_widget(buttonСhoiceImage)
        box.add_widget(buttonTakeImage)
        box.add_widget(buttonStart)

        return box


if __name__ == "__main__":
    app = MyApp()
    app.run()
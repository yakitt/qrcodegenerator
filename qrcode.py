from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import pyqrcode
class MyApp(App):
    def build(self):
        self.layout=FloatLayout()
        self.label=Label(text='Напишите URL:',pos_hint={'center_x': 0.5,'center_y': 0.95},font_size=50)
        self.text_input=TextInput(text='',
            hint_text="",
            font_size=60,
            size_hint=(0.95, 0.2),
            height=100,
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            background_normal="",  # Отключаем стандартный фон
            background_color=(1, 1, 1, 1),  # Белый фон
            foreground_color=(0, 0, 0, 1),  # Чёрный текст,
            multiline=False)
        self.button=Button(text='Сгенерировать',size_hint=(0.7,0.2),pos_hint={'center_x': 0.5,'center_y': 0.1})
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        return self.layout
    def on_button_press(self,insta):
        qr_str=self.text_input.text
        url_to_qr=pyqrcode.create(qr_str)
        url_to_qr.png('qr.png',scale=8)
        self.layout.clear_widgets()
        self.image=Image(source='qr.png',size_hint=(0.5,0.5),pos_hint={'center_x': 0.5,'center_y':0.5})
        self.layout.add_widget(self.image)

if __name__=="__main__":
    MyApp().run()
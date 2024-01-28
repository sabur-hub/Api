from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.slider import MDSlider
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import requests

class BedtimeStoryApp(BoxLayout):
    def __init__(self, **kwargs):
        super(BedtimeStoryApp, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        self.age_label = MDLabel(text='Возраст ребёнка:')
        self.age_input = MDTextField()

        self.type_label = MDLabel(text='Тип сказки:')
        self.type_input = MDTextField()
        self.type_input.text = 'Фэнтези'

        self.slider_label = MDLabel(text='Длина сказки:')
        self.slider = MDSlider(min=1, max=10, step=1)

        self.language_label = MDLabel(text='Язык сказки:')
        self.language_input = MDTextField()
        self.language_input.text = 'Русский'

        self.author_checkbox = MDCheckbox(active=False)
        self.author_label = MDLabel(text='Сказку написал ребёнок')

        self.create_button = MDRaisedButton(text='Создать сказку', on_release=self.create_story)

        self.add_widget(self.age_label)
        self.add_widget(self.age_input)

        self.add_widget(self.type_label)
        self.add_widget(self.type_input)

        self.add_widget(self.slider_label)
        self.add_widget(self.slider)

        self.add_widget(self.language_label)
        self.add_widget(self.language_input)

        self.add_widget(self.author_label)
        self.add_widget(self.author_checkbox)

        self.add_widget(self.create_button)

    def create_story(self, instance):
        # Обработка нажатия кнопки и отправка запроса к API GPT-3
        # Используйте self.age_input.text, self.type_input.text и другие значения

        # Пример кода для отправки запроса (используется библиотека requests)
        # response = requests.post(api_url, data={'length': self.slider.value, 'age': self.age_input.text, 'type': self.type_input.text})
        # story_text = response.text
        # print(story_text)

        # Просто для демонстрации, пока не подключен API
        popup = Popup(title='Готово',
                      content=MDLabel(text='Сказка успешно создана!'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class BedtimeStoryAppApp(MDApp):
    def build(self):
        return BedtimeStoryApp()

if __name__ == '__main__':
    BedtimeStoryAppApp().run()

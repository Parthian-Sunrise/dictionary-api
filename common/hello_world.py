from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock

class MyPopup(Popup):
    def __init__(self, title, message, callback, **kwargs):
        super(MyPopup, self).__init__(**kwargs)
        self.title = title
        self.size_hint = (0.75, 0.5)
        self.auto_dismiss = False

        layout = BoxLayout(orientation='vertical')
        self.input_text = TextInput(multiline=False)
        layout.add_widget(Label(text=message))
        layout.add_widget(self.input_text)

        button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.3)
        ok_button = Button(text='OK')
        ok_button.bind(on_press=self.on_ok)
        button_layout.add_widget(ok_button)
        
        close_button = Button(text='Close')
        close_button.bind(on_press=self.on_close)
        button_layout.add_widget(close_button)
        
        layout.add_widget(button_layout)
        self.add_widget(layout)
        
        self.callback = callback

    def on_ok(self, instance):
        self.callback(self.input_text.text)
        self.dismiss()

    def shutdown(self, dt=0.5):
        App.get_running_app().close_app(dt)

    def on_close(self, instance):
        Clock.schedule_once(self.shutdown, 0.5)

class MyApp(App):
    def build(self):
        self.show_input_popup("Input", "What's your name?:")

    def show_input_popup(self, title, message):
        popup = MyPopup(title, message, self.process_input)
        popup.open()

    def process_input(self, text):
        if text == "Matthew":
            self.show_input_popup("Input", "Smelly boy:")
        else:
            self.show_input_popup("Input", "Good, Matthew's not here!")

    def close_app(self, dt):
        from kivy.base import EventLoop
        EventLoop.window.close()
        self.stop()

if __name__ == '__main__':
    MyApp().run()

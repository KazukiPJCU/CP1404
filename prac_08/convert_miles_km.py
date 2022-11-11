from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_CONVERSION = 1.60934


class MilesConversionApp(App):
    km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATE = 1.60934


class MilesConversionApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        number = self.get_valid_miles()
        result = number * CONVERSION_RATE
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        number = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(number)
        self.handle_calculate()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConversionApp().run()

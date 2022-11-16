from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Lindsay", "Bob", "Norm", "Greg", "Spiderman", ]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        [self.root.ids.name_box.add_widget(Label(text=name)) for name in self.names]


DynamicLabelsApp().run()

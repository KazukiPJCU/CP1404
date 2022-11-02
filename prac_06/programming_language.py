"""CP1404/CP5632 Practical - programming language.
    35 min:"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Programming language class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """string formatting."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """If dynamic"""
        return self.typing == "Dynamic"

"""CP1404/CP5632 Practical - programming language."""


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


def run_test():
    """Run test"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamic languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_test()

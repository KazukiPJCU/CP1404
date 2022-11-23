"""Band class for CP1404"""


class Band:

    def __init__(self, name=''):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({','.join([musician.__str__() for musician in self.musicians])})"

    def add(self, musician):
        """Add musician to band"""
        self.musicians.append(musician)


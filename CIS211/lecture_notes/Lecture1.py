'''
class Event():
    def __int__(self, year: int, desc: str):
        self.year = year
        self.desc = desc

    @property
    def describe(self) -> str:
        return f"{self.year}: {self.description}"


e = Event(1941, 'First relay-based computer')

print(e.describe())

'''


class Pet:
    def __init__(self, kind: str, name: str):
        self.species = kind
        self.called = name

    def rename(self, new_name):
        self.called = new_name


my_pet = Pet("canis familiaris", "fido")


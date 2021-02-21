class Event:
    def __int__(self, year: int, desc: str):
        self.year = year
        self.desc = desc

    def describe(self) -> str:
        return f"{self.year}: {self.description}"


e = Event(1941, 'First relay-based computer')

print(e.describe())


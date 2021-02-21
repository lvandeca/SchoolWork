class Event:
    def __init__(self, year: int, desc: str):
        self.year = year
        self.desc = desc

    def __str__(self) -> str:
        return f"{self.year}:{self.desc}"

    def __repr__(self) -> str:
        return f"Event({self.year},{self.desc})"

    def change_year(self, new_year: int):
        self.year = new_year
        return self.__str__()

    def change_desc(self, new_desc: str):
        self.desc = new_desc
        return self.__str__()

def main():
    event1 = Event(2020, "Pandemic")
    print(event1)
    print(event1.change_year(1920))
    print(event1.change_desc("Roaring 20's"))

if __name__ == '__main__':
    main()

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

class Era:
    def __init__(self, beg_year: int, end_year: int, Event_list: Event):
        self.beg_year = beg_year
        self.end_year = end_year
        self.Event_list = Event_list

    def __str__(self):
        return f"Start:{self.beg_year} End:{self.end_year} Events:{self.Event_list}"

    def __repr__(self):
        return f"Era({self.beg_year},{self.end_year},{self.Event_list}"


def main():
    event1 = Event(2020, "Pandemic")
    #print(event1)
    event2 = Event(2000, "Y2K Bug")
    event3 = Event(2015, "Gay Marriage Legalized")
    e1 = Era(2000, 2030, [event1, event2, event3])
    print(e1)

if __name__ == "__main__":
    main()

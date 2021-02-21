class Phone:

    def __init__(self, name: str):
        self.name = name

    def pickUp(self):
        print(f"Picking up {self.name}")

    def dial(self, num: str):
        print(f"dialing {num}")

    def speak(self, msg: str):
        print(f"speaking {msg}")

    def call(self, num: str, msg: str):
        self.pickUp()
        self.dial(num)
        self.speak(msg)


# an object of SmartPhone is also of type Phone

class SmartPhone(Phone):
    def __init__(self, name: str):
        super().__init__(name)

    def openPhoneApp(self):
        print(f"opening Phone App on {self.name}")

    # overriding
    def call(self, num: str, msg: str):
        self.openPhoneApp()
        self.dial(num)
        self.speak(msg)


def callUO(phone: "Phone"):
    phone.call("5413461000", "This is CIS 211 Lab")

def main():
    ph1 = Phone("Panasonic")
    ph2 = Phone("AT&T")

    sph1 = SmartPhone("Iphone")
    sph2 = SmartPhone("Google Phone")

    phoneList = [ph1,ph2,sph1,sph2]
    for phone in phoneList:
        callUO(phone)
        print("------------------------------------------")

if __name__ == "__main__":
    main()
class Listener:
    """Abstract base for listeners"""
    def notify(self, desc: str, val: int):
        raise NotImplementedError("Oops!")


class Listenable:
    def __init__(self):
        self.listeners = []

    def attach_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, desc: str, val: int):
        for listener in self.listeners:
            listener.notify(desc,val)


class Button(Listenable):
    def __init__(self):
        super().__init__()

    def poke(self):
        self.listener.notify("poked", 42)


class Anvil(Listener):
    def notify(self, desc: str, val: int):
        print(f"Clang! {desc}")


class Horn(Listener):
    def notify(self, desc: str, val: int):
        print(f"Honk! {desc} {val}")


b = Button()
h = Horn()
b.attach_listener(h)

b.poke()


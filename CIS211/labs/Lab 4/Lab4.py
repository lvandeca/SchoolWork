class Node():
    def __init__(self, value: int):
        self.value = value

    def sum(self):
        raise NotImplementedError("should be a subclass with this method")

    def __str__(self):
        raise NotImplementedError("implemented in subclasses")


class Leaf(Node):
    def __init__(self, value: int):
        self.value = value

    def sum(self):
        return self.value

    def __str__(self):
        return f"{self.value}"


class Internal(Node):
    def __init__(self, value: int, left: Node, right: Node):
        self.value = value
        self.left = left
        self.right = right
        self.type_left = type(left)
        self.type_right = type(right)

    def sum(self):
        return self.value + self.left.sum() + self.right.sum()

    def __str__(self):
        return f"<{self.value}, {self.left}, {self.right}>"


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7,l2,l3)
    root = Internal(5,l1,i)
    print(root.sum())
    print(root)

if __name__ == "__main__":
    main()
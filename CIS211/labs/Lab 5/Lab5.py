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

    def deepcopy(self):
        return Leaf(self.value)

    def copy(self):
        return self


class Internal(Node):
    def __init__(self, value: int, left: Node, right: Node):
        self.value = value
        self.left = left
        self.right = right

    def sum(self):
        return self.value + self.left.sum() + self.right.sum()

    def __str__(self):
        return f"<{self.value}, {self.left}, {self.right}>"

    def deepcopy(self):
        return Internal(self.value, self.left.deepcopy(), self.right.deepcopy())

    def copy(self):
        return self


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7,l2,l3)
    root = Internal(5,l1,i)
    deep = root.deepcopy()
    deep.right.value = 8
    print("Deep = {}".format(deep))
    print("Root has not been altered due to a deepcopy. Root = {}".format(root))
    shallow = root.copy()
    shallow.right.value = 8
    print("Shallow = {}".format(shallow))
    print("Root has now been altered due to a shallow copy. Root = {}".format(root))

if __name__ == "__main__":
    main()
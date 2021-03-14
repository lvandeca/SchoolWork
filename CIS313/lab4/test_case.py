from mealticket import *
from lvandeca_lab4 import *
from random import *


def defaultTestTickets(vals):
    """
        Generates a list of meal tickets with the provided list of values
    """
    result = []
    for i in range(len(vals)):
        ticket = MealTicket("My Meal " + str(i))
        ticket.ticketID = vals[i]
        ticket.addItem(("Test Item", round(uniform(0, 30), 2)))
        result.append(ticket)
    return result


def randomTestTickets(size):
    """
        Generates a list of random mealtickets with no duplicates
        Returns <size> mealtickets
    """
    result = []
    vals = sample(range(1, size+20), size)
    for i in range(size):
        ticket = MealTicket("My Meal " + str(i))
        ticket.ticketID = vals[i]
        ticket.addItem(("Test Item", round(uniform(0, 30), 2)))
        result.append(ticket)
    return result


def displayNodes(node):
    """
        Input: the root of your RBTree
        For every node in the tree, it will print it's relationships
        (children, parent, etc.) as well as the color.
        Useful for debugging your tree and making sure things are working
    """
    if not node.isSentinel():
        print(node)
        print(f"Color: {node.getColor()}\n")
        displayNodes(node.getLChild())
        displayNodes(node.getRChild())


def myChoice(ticketID, testTickets):
    for ticket in testTickets:
        if ticket.ticketID == ticketID:
            return ticket


def main():
    SIZE = 12                          # Number of nodes you want in tree
    # Premade tickets to test specific cases
    testValues = [12, 13, 17, 10, 4, 6, 9, 15, 30, 25, 20, 40]

    # Only uncomment the one you want to use
    # testTickets = randomTestTickets(SIZE)             # For random tickets
    testTickets = defaultTestTickets(testValues)     # For premade tickets

    testTree = RedBlackTree()

    print("List of Test Tickets:", end=" ")
    print([t.ticketID for t in testTickets])

    print("============ Testing Insert Method ============")
    res = True
    for ticket in testTickets:
        print("Inserting " + str(ticket.ticketID), end=": ")
        res = testTree.insert(ticket)
        print(res)
        if not res:
            print("SOMETHING WENT WRONG")
            break

    if res:
        print("============ Testing Traversal Methods ============")
        print("Pre-order:", end=" ")
        print(testTree.traverse("pre-order"))
        print("In-order:", end=" ")
        print(testTree.traverse("in-order"))
        print("Post-order:", end=" ")
        print(testTree.traverse("post-order"))

        print("============ Testing Find Method ============")
        findTestVals = []
        for _ in range(2):
            # Grab a ticket that should be in the tree
            findTestVals.append(choice(testTickets).ticketID)
            # Grab a random value (may or may not be in tree)
            findTestVals.append(randint(1, SIZE+20))
        for value in findTestVals:
            result = testTree.find(value)
            if result is not False:
                result = True
            print(f"Is {value} in the tree: {result}")

        print("============ Testing Delete Method ============")
        i = 0
        while len(testTickets) > 0:
            # deleteOrder = [13, 12]          #
            # deleteTicket = myChoice(deleteOrder[i], testTickets)
            deleteTicket = choice(testTickets)
            testTickets.remove(deleteTicket)
            deleteID = deleteTicket.ticketID
            print(f"Deleting node {deleteID}...")
            deleteNode = testTree.findNode(deleteID)
            deleteResult = testTree.delete(deleteID)
            if deleteResult:
                print("DELETION SUCCESSFUL!\n")
            else:
                print("DELETION FAILED!\n")
                break
            i += 1


if __name__ == '__main__':
    main()

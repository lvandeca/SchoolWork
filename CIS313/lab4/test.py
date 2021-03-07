from lvandeca_lab4 import *
from mealticket import *
from random import *


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


def testTreeInsert(testTickets, testTree):
    insert = True
    for ticket in testTickets:
        if(testTree.insert(ticket)):
            pass
        else:
            print("Insert Failed: {} into tree {}".format(
                ticket._key, testTree))
            insert = False
            break

    return insert


def formatPrint(testNum):
    printTest = testNum + 1
    testPrint = "Checking tree {}".format(printTest)
    if(printTest < 10):
        testPrint += "........."
    elif(printTest < 100):
        testPrint += "........"
    elif(printTest < 1000):
        testPrint += "......."
    else:
        testPrint += "......"

    return testPrint


def checkTree(testTree, testPrint):
    RedBlackProperty = True
    check = testTree.check(testTree._root, 0)
    if((type(check[0]) == bool)):
        testPrint += "Passed"
        print(testPrint)
        pass
    else:
        testPrint += "Failed"
        print(testPrint)
        print("     Test Failed: {}".format(testTree))
        print(
            "     Red-Black Tree Property Violated: {}".format(check[0]))
        RedBlackProperty = False

    return RedBlackProperty


def testInsert(testCases, treeSize):
    print("Testing insert")
    print()
    for test in range(testCases):

        testTickets = randomTestTickets(treeSize)
        testTree = RedBlackTree()

        # insert all the tickets into the tree, tests to make sure they are
        # inserted properly
        insertSuccess = testTreeInsert(testTickets, testTree)
        if(insertSuccess):

            # formating print output for user readability
            testPrint = formatPrint(test)
            # check that the tree conforms to Red-Black properties
            check = checkTree(testTree, testPrint)

            if(not check):
                break

    if(check):
        print()
        print("All insert tests passed")
        print()


def main():

    # number of test cases
    testCases = 2000
    treeSize = 100

    # tests
    testInsert(testCases, treeSize)


if __name__ == "__main__":
    main()

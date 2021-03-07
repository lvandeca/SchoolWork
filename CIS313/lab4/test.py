from lvandeca_lab4 import *
from test_main import *


def main():

    RedBlackProperty = True
    for test in range(200):

        testTickets = randomTestTickets(4)
        testTree = RedBlackTree()
        insert = True
        for ticket in testTickets:
            if(testTree.insert(ticket)):
                pass
            else:
                print("Insert Failed: {} into tree {}".format(
                    ticket._key, testTree))
                insert = False
                break

        print("Checking tree 1")
        print("--------------------------------------------------------------")
        check = testTree.check(testTree._root, 0)
        if((type(check[0]) == bool) and insert):
            pass
        else:
            print("Test Failed: {}".format(testTree))
            print("Red-Black Tree Property Violated: {}".format(check[0]))
            RedBlackProperty = False
            break
        print("--------------------------------------------------------------")

    if(not RedBlackProperty):
        print("All insert tests passed")

if __name__ == "__main__":
    main()

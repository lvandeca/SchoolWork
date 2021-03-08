from __future__ import print_function
from math import *
from lvandeca_lab4 import *
from mealticket import *
from random import *
import sys
import time


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


def myPercent(percent):
    p = floor(percent * 100)
    ret = f"{p}%"
    ret2 = 80
    if(p < 10):
        ret2 -= 2
    elif(p < 100):
        ret2 -= 3
    else:
        ret2 -= 4

    return ret, ret2


def output(test, testCases):
    percent = test / testCases
    ofEighty = myPercent(percent)

    doneNum = floor(percent * ofEighty[1])
    done = "#"*(doneNum)
    todo = '-'*(ofEighty[1] - doneNum)
    s = "{}".format(done + todo + ofEighty[0])
    if(not todo):
        s += '\n'
    if(test > 1):
        s = '\r' + s
    sys.stdout.write(s)
    sys.stdout.flush()


def checkTree(testTree, test, testCases):
    RedBlackProperty = True
    printTest = test + 1
    check = testTree.check(testTree._root, 0)
    if((type(check[0]) == bool)):
        output(printTest, testCases)
    else:
        print("Failed Test #{}".format(printTest))
        print("     Tree Failed: {}".format(testTree))
        print(
            "     Red-Black Tree Property Violated: {}".format(check[0]))
        RedBlackProperty = False

    return RedBlackProperty


def testInsert(testCases, treeSize):
    print("Testing insert")
    for test in range(testCases):

        testTickets = randomTestTickets(treeSize)
        testTree = RedBlackTree()

        # insert all the tickets into the tree, tests to make sure they are
        # inserted properly
        insertSuccess = testTreeInsert(testTickets, testTree)
        if(insertSuccess):

            # check that the tree conforms to Red-Black properties
            check = checkTree(testTree, test, testCases)

            if(not check):
                break

    if(not check):
        return False
    else:
        return True


def main():

    # number of test cases
    testCases = 2000
    treeSize = 100

    # tests
    if(not testInsert(testCases, treeSize)):
        return
    # if(not testDelete(testCases, treeSize)):
    #    return


if __name__ == "__main__":
    main()

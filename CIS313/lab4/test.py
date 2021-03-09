from __future__ import print_function
from math import *
from lvandeca_lab4 import *
from mealticket import *
from random import *
import sys
import time


# Global Variables
testCases = 2000    # number of trees to test
treeSize = 100      # size of tree to test


# ================================Helper Functions==============================
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
            checkPartialTree = testTree.check(testTree._root, 0)
            if(type(checkPartialTree[0]) != bool):
                print("Tree check failed after insert: {}".format(
                    ticket.ticketID))
                print("     Improper Tree: {}".format(testTree))
                print("     Red-Black Tree Property Violated: {}".format
                      (checkPartialTree[0]))
        else:
            print("Insert Failed: {} into tree {}".format(
                ticket.ticketID, testTree))
            insert = False
            break

    return insert


def testTreeDelete(testTickets, testTree):
    delete = True
    while(len(testTickets) > 0):
        deleteTicket = choice(testTickets)
        testTickets.remove(deleteTicket)
        deleteID = deleteTicket.ticketID

        if(testTree.delete(deleteID)):
            checkPartialTree = testTree.check(testTree._root, 0)
            if(type(checkPartialTree[0]) != bool):
                print("Tree check failed after insert: {}".format(deleteID))
                print("     Improper Tree: {}".format(testTree))
                print("     Red-Black Tree Property Violated: {}".format
                      (checkPartialTree[0]))
        else:
            print("Deletion Failed: {} into tree {}".format(
                deleteID, testTree
            ))
            delete = False
            break

    return delete


def myPercent(percent, testType):
    p = floor(percent * 100)
    ret = f" {p}%"
    ret2 = 79 - len(testType) + 1
    if(p < 10):
        ret2 -= 2
    elif(p < 100):
        ret2 -= 3
    else:
        ret2 -= 4

    return ret, ret2


def output(test, testCases, testType):
    percent = test / testCases
    ofEighty = myPercent(percent, testType)

    doneNum = floor(percent * ofEighty[1])
    done = "#"*(doneNum)
    todo = '-'*(ofEighty[1] - doneNum)
    s = "\r{}{}".format(testType, done + todo + ofEighty[0])
    if(not todo):
        s += '\n'
    sys.stdout.write(s)
    sys.stdout.flush()


def checkTree(testTree, test, testCases, testType):
    RedBlackProperty = True
    printTest = test + 1
    check = testTree.check(testTree._root, 0)
    if((type(check[0]) == bool)):
        output(printTest, testCases, testType)
    else:
        print("Failed Test #{}".format(printTest))
        print("     Improper Tree: {}".format(testTree))
        print("     Red-Black Tree Property Violated: {}".format(check[0]))
        RedBlackProperty = False

    return RedBlackProperty


def testInsert(testCases, treeSize):
    testType = "Testing insert ----------------------------------------------------------------0%"
    print_slow(testType)
    insertSuccess = False
    fullTreeCheck = False
    for test in range(testCases):

        testTickets = randomTestTickets(treeSize)
        testTree = RedBlackTree()

        # insert all the tickets into the tree, tests to make sure they are
        # inserted properly
        insertSuccess = testTreeInsert(testTickets, testTree)
        if(insertSuccess):

            # check that the tree conforms to Red-Black properties
            fullTreeCheck = checkTree(
                testTree, test, testCases, "Testing insert ")

            if(not fullTreeCheck):
                break

    if(fullTreeCheck and insertSuccess):
        return True
    else:
        return False


def testDelete(testCases, treeSize):
    testType = "Testing delete ----------------------------------------------------------------0%"
    print_slow(testType)
    deleteSuccess = False
    fullTreeCheck = False
    for test in range(testCases):

        testTickets = randomTestTickets(treeSize)
        testTree = RedBlackTree()

        # insert all the tickets into the tree, tests to make sure they are
        # inserted properly
        insertSuccess = testTreeInsert(testTickets, testTree)
        if(insertSuccess):

            # delete tickets one at a time, if a deletion fails, don't continue
            # to check full tree
            deleteSuccess = testTreeDelete(testTickets, testTree)

            if(deleteSuccess):
                # check that the tree conforms to Red-Black properties
                fullTreeCheck = checkTree(
                    testTree, test, testCases, "Testing delete ")

                if(not fullTreeCheck):
                    break

    if(fullTreeCheck and deleteSuccess):
        return True
    else:
        return False


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if(letter == '=' or letter == '-'):
            time.sleep(0.012)
        else:
            time.sleep(0.125)


def massTest():
    if(not testInsert(testCases, treeSize)):
        return
    if(not testDelete(testCases, treeSize)):
        return


def caseTest():
    pass


def main():

    print()
    printstdout = "================================================================================"
    print_slow(printstdout)
    print()
    printstdout = "========================Test Suite for Red-Black Tree==========================="
    print_slow(printstdout)
    print()
    printstdout = "================================================================================"
    print_slow(printstdout)
    print()
    print()

    # specific case testing for code
    printstdout = "---------------------------------Case Testing-----------------------------------"
    print_slow(printstdout)
    print()
    print()

    caseTest()

    # mass testing to catch a possible random scenario
    printstdout = "---------------------------------Mass Testing-----------------------------------"
    print_slow(printstdout)
    print()
    print()

    massTest()
    print()


if __name__ == "__main__":
    main()

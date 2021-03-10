"""
Author: Luke Vandecasteele
Date: 3/6/2021 Last Modified: 3/9/2021
Credits: Jimmoothy (on discord), Sebastian and Remi on StackOverflow
Description: classes for managing testing for Red-Black Trees for CIS 313:
             Interm Data Structures at University of Oregon
Notes:
    1. Credits are listed in the specific functions below
"""

from __future__ import print_function
from math import *
from lvandeca_lab4 import *
from mealticket import *
from random import *
import sys
import time


class Test():
    """Description: Easier testing suite and process for Red-Black Trees and lab
       assignment 4 in CIS 313.
    """

    def __init__(self, totalTests, treeSize):
        self.totalTests = totalTests
        self.treeSize = treeSize

    def testInsert(self, RedBlackTree):
        testType = "Testing insert " + ("-"*63) + "0%"
        print_slow(testType)
        for testNum in range(self.totalTests):
            testTicketList = randomTestTickets(self.treeSize)


def print_slow(str):
    """
    Description: function to print slowly to terminal. Simulates real life
                    typing

    Credits: Sebastian on StackOverflow
    https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing

    Args:
        str (str): string to print slowly to standard output
    """

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if(letter == '=' or letter == '-'):
            time.sleep(0.012)
        else:
            time.sleep(0.125)


def randomTestTickets(size):
    """
    Author: Jimmoothy (on discord)

    Credits: function copied from test_case.py

    Description: Generates a list of random mealtickets with no duplicates,
                    helper function for testing purposes

    Returns: <size> mealtickets
    """

    result = []
    vals = sample(range(1, size+20), size)
    for i in range(size):
        ticket = MealTicket("My Meal " + str(i))
        ticket.ticketID = vals[i]
        ticket.addItem(("Test Item", round(uniform(0, 30), 2)))
        result.append(ticket)
    return result

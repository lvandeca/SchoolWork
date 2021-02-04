"""
Author: Luke Vandecasteele
Date: 2/1/2021 Last Modified: 2/2/2021
Credits: Class notes
Description: Implementation of a PriorityQueue class using a heap data
             structure.
Notes:
      1. Enqueue and dequeueMax methods use different function calls to
         restructure heap
      2. TODO: add better documentation
"""

from mealticket import *

# Define Global Variable
DEFAULT_CAPACITY = 50


#=============================PriorityQueue Class=============================#

class PriorityQueue():
    """PriorityQueue implemented using a heap"""

    def __init__(self, capacity):
        self._currentSize = 0
        self._heap = []

        try:
            invalidInput = (capacity < 1)           #invalid input if capacity
            if(invalidInput):                       #is not an integer > 1, use
                self._maxSize = DEFAULT_CAPACITY    #DEFAULT_CAPACITY
            else:
                self._maxSize = capacity

        except TypeError:
            self._maxSize = DEFAULT_CAPACITY

    def __str__(self):
        """
        Author: Jared Hall
        Date: 01/03/2020
        Description: Output the current queue as a string.
        Inputs: None
        Outputs: str
        """
        returnValue = "Current queue: ["
        if(self._currentSize != 0):
            for ticket in self._heap:
                if(ticket is None):
                    break
                else:
                    returnValue += "(" + str(ticket.ticketID) + ", "
                    returnValue += str(ticket.totalCost) + "), "
            returnValue = returnValue[:-2] + "]"
        else:
            returnValue += "]"
        return returnValue

    def enqueue(self, ticket):
        """Adds ticket to the queue. Appends to end of list self._heap(), then
        restructures the heap. Called by user. Calls self._heapInsert().
        Returns Boolean."""

        success = (type(ticket) == MealTicket and not self.isFull())

        if(success):
            self._heap.append(ticket)
            self._currentSize += 1
            self.isEmpty() or self._heapInsert(self._currentSize - 1)

        return success

    def dequeueMax(self):
        """Destructive read of the queue. Called by user. Calls self._heapDelete
        to maintain heap structure. Returns Boolean/MealTicket"""

        success = (not self.isEmpty())

        if(success):
            success = self._heap[0]
            self._currentSize -= 1

            self._heap[0] = self._heap[self._currentSize]
            del self._heap[self._currentSize]

            self._heapDelete()

        return success

    def peekMax(self):
        """Non-Destructive read of the queue. Called by user. Returns
        Boolean/MealTicket"""

        success = (not self.isEmpty())

        if(success):
            success = self._heap[0]

        return success

    def _heapInsert(self, child):
        """Bottom up fix of self._heap to fix heap structure after insertion
        into the queue. Called by self.enqueue(). Returns None."""

        swapped = True
        while(swapped):
            parent = self._getParent(child)
            if(parent < 0):
                break
            swapped = self._swap(child, parent)
            child = parent

        return None

    def _heapDelete(self):
        """Top down fix of self._heap to fix heap structure after removal of
        max element from the queue. Called by self.dequeueMax(). Return None"""

        maxParent = self._getParent(self._currentSize)
        parent = 0
        swapped = True

        while(swapped and parent <= maxParent):
            child = self._greaterChild(parent)
            swapped = self._swap(child, parent)
            parent = child

        return None

    def _swap(self, child, parent):
        """Helper function for heap restructuring fucntions. Switches child
        and parent to conform to heap structure. Returns Boolean."""

        childID = self._heap[child].ticketID
        parentID = self._heap[parent].ticketID

        swapped = childID > parentID
        if(swapped):
            tmpTicket = self._heap[parent]
            self._heap[parent] = self._heap[child]
            self._heap[child] = tmpTicket

        return swapped

    def _getParent(self, child):
        """Helper function for self._heapInsert(). Returns parent
        index for a given child. Returns integer."""

        odd = child % 2
        if(odd):
            parent = (child) // 2
        else:
            parent = (child //2) - 1
        return parent

    def _greaterChild(self, parent):
        """Helper function for self._heapDelete(). Returns index of child with
        greater priority. Returns integer."""

        child1 = (parent * 2) + 1
        child2 = (parent * 2) + 2

        child1ID = self._heap[child1].ticketID
        child2ID = self._heap[child2].ticketID

        if(child1ID >= child2ID):
            greaterChild = child1

        else:
            greaterChild = child2

        return greaterChild

    def isEmpty(self):
        """Returns True if queue is empty. Called by self.dequeueMax() and
        self.peekMax(). Returns Boolean."""

        return self._currentSize == 0

    def isFull(self):
        """Returns True if queue is full. Called by self.enqueue(). Returns
        Boolean."""

        return self._currentSize == self._maxSize

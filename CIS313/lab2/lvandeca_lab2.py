"""
Author: Luke Vandecasteele
Date: 2/1/2021 Last Modified: 2/8/2021
Credits: Class notes
Description: Implementation of a PriorityQueue class using a max heap data
             structure for MealTickets.
Notes:
      1. Enqueue and dequeueMax methods use different function calls to
         restructure heap (self._siftUp() and self._siftDown() respectively)

      2. Both methods self._siftUp() and self._siftDown() are O(log(n)) since
         the counter for the loop is either incremented by 2*i to the child
         node (as we go up the heap) or decremented by i//2 to the parent node
         (as we go down the heap) which means in both cases we only cover each
         "level" of the tree and not ever single element in the heap, making 
         the running time O(long(n)) and not O(n).

      3. Extra Credit is O(nlog(n)) behavior since we iterate through each 
         element in the input array one time (which gives us O(n)) and for each
         element we make exactly one call to self.enqueue() which is an
         O(log(n)) procedure which means that we get O(nlog(n)) running time.
"""

from mealticket import *

# Define Global Variable
DEFAULT_CAPACITY = 50


#=============================PriorityQueue Class=============================#

class PriorityQueue():
    """PriorityQueue implemented using a max heap"""

    def __init__(self, capacity):
        self._currentSize = 0
        self._heap = []

        if type(capacity) == int and capacity > 0:      #valid input is an
            self._maxSize = capacity                    #integer in (0,∞]
        else:
            self._maxSize = DEFAULT_CAPACITY    #non-valid input use default

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
        restructures the heap. Called by user. Calls self._siftUp() and
        self.isFull(). Returns Boolean."""

        #valid input is a MealTicket and the queue is not already full
        success = (type(ticket) == MealTicket and not self.isFull())

        if(success):                        #continue if valid input
            self._heap.append(ticket)       #append ticket to end of list
            self._currentSize += 1          

            #if Queue is empty, we don't need to siftUp to maintain heap
            #structure. Otherwise, self._siftUp()
            self.isEmpty() or self._siftUp(self._currentSize - 1)

        return success

    def dequeueMax(self):
        """Destructive read of the queue. Called by user. Calls self._siftDown
        to maintain heap structure and self.isEmpty(). Returns 
        Boolean/MealTicket"""

        success = (not self.isEmpty())      #continue if Queue is not empty


        if(success):
            success = self._heap[0]         #get max element
            self._currentSize -= 1          

            #move last element in the heap to the front effectively removing max
            self._heap[0] = self._heap[self._currentSize]

            #delete last element since it is now at the from of the heap
            del self._heap[self._currentSize]

            self._siftDown()    #fix heap structure

        return success

    def peekMax(self):
        """Non-Destructive read of the queue. Called by user. Calls
        self.isEmpty(). Returns Boolean/MealTicket."""

        success = (not self.isEmpty())      #continue if Queue is not empty


        if(success):
            success = self._heap[0]         #get max element

        return success

    def _siftUp(self, child):
        """Bottom up fix of self._heap to fix heap structure after insertion
        into the queue. Called by self.enqueue(). Calls self._getParent().
        and self._swap(). Returns None."""

        swapped = True
        while(swapped):                         #only continue if a swap is made
            parent = self._getParent(child)
            if(parent < 0):                     #parent is not in heap, break loop
                break
            swapped = self._swap(child, parent)
            child = parent                      #new child is old parent
                                                #creating O(log(n)) behavior
        return None

    def _siftDown(self):
        """Top down fix of self._heap to fix heap structure after removal of
        max element from the queue. Called by self.dequeueMax(). Calls
        self._greaterChild() and self._swap(). Returns None."""

        maxParent = self._getParent(self._currentSize)
        parent = 0
        swapped = True

        #continue if swap was made and bottom row of tree hasnt been passed
        while(swapped and parent < maxParent):
            child = self._greaterChild(parent)  #swap with larger child node
            swapped = self._swap(child, parent)
            parent = child

        return None

    def _swap(self, child, parent):
        """Helper function for heap restructuring functions. Switches child
        and parent to conform to heap structure. Called by self._siftDown()
        and self._siftUp(). Returns Boolean."""

        childID = self._heap[child].ticketID        #childID for comparison
        parentID = self._heap[parent].ticketID      #parentID for comparison


        swapped = childID > parentID            #only swap if condition is met
        if swapped:                     
            tmpTicket = self._heap[parent]
            self._heap[parent] = self._heap[child]
            self._heap[child] = tmpTicket

        return swapped

    def _getParent(self, child):
        """Helper function for self._heapInsert(). Returns parent
        index for a given child. Called by self._siftUp() and self._siftDown().
        Returns integer."""

        odd = child % 2
        if odd:                             #child is odd, use different
            parent = (child) // 2           #equation for parent node
        else:                               #calculation
            parent = (child //2) - 1
        return parent

    def _greaterChild(self, parent):
        """Helper function for self._heapDelete(). Returns index of child with
        greater priority. Called by self._siftDown(). Returns integer."""

        child1 = (parent * 2) + 1
        child2 = (parent * 2) + 2

        child1ID = self._heap[child1].ticketID      #get priority of each child
        child2ID = self._heap[child2].ticketID

        if(child1ID >= child2ID):           #return child with larger priority
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

#====================================Extra Credit==============================#

    def heap_sort(self, array):
        """Method to sort given list of MealTickets. Called by user. Returns
        Boolean/List"""

        success = False                     #assume failure

        for ticket in array:                #iterate through input list
            success = self.enqueue(ticket)
            if not success:                 #enqueue failed, break loop
                break

        if success:                         #made it through whole array and
            success = self._heap            #success = True, then return
                                            #self._heap (aka sorted list)
        return success


def printArray(array):
    """
    Author: Jared Hall
    Date: 01/03/2020
    Description: Output the current queue as a string.
    Inputs: list
    Outputs: str
    """
    returnValue = "Current queue: ["
    if(len(array)!= 0):
        for ticket in array:
            if(ticket is None):
                break
            else:
                returnValue += "(" + str(ticket.ticketID) + ", "
                returnValue += str(ticket.totalCost) + "), "
        returnValue = returnValue[:-2] + "]"
    else:
        returnValue += "]"
    return returnValue


def main():

    queue1 = PriorityQueue(8)
    tickets = generateMealTickets(8)

    printArray(tickets)
    
    sortedTickets = queue1.heap_sort(tickets)
    print(queue1)

    printArray(sortedTickets)


main()

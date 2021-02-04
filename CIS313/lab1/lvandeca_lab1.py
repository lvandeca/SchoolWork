"""
Author: Luke Vandecasteele
Credits: Class notes and textbook
Date: 1/17/2021 Last Edited: 1/26/2021
Description: Implementation of a Stack and Queue data
structure using a singely linked list.
"""

from mealticket import *

#Define Global Variable
DEFAULT_CAPACITY = 50


#===============================Node Class====================================#

class Node():
    """Container for the creation of a singely linked list"""

    def __init__(self, ticket, next):
        self.ticket = ticket            #type checked 
        self.next = next                #type Node


#===============================Queue Class===================================#

class Queue():
    """Implementation of a FIFO linked list for a Queue"""

    def __init__(self, capacity):
        self.tail = None
        self.head = None
        try:
            invalidInput = (capacity < 1)
            if(invalidInput):
                self.maxSize = DEFAULT_CAPACITY
            else:
                self.maxSize = capacity

        except TypeError:
            self.maxSize = DEFAULT_CAPACITY

        self.currentSize = 0

    def enqueue(self, ticket):
        """Creation of a new Node and placement in the linked list.
        Called by user. Calls self.isFull(). Checks that input ticket
        is of type MealTicket. Creates instance of Node() class.
        Returns True if enqueue is successfull, else False."""

        #continue if input is type MealTicket and Queue not full
        success = ( (type(ticket) == MealTicket) and (not self.isFull()) )

        if(success):
                new = Node(ticket, None)        #new Node instance
                if(self.tail == None):          #Queue is empty
                    self.head = new
                else:
                    self.tail.next = new        #old tail points to new
                self.tail = new                 #input becomes new tail
                self.currentSize += 1

        return success

    def dequeue(self):
        """Destructive read of the head node in the queue. Called by
        user. Calls self.isEmpty to ensure a Node is in the Queue
        before read. Returns MealTicket if Node in the Queue, else
        returns False."""

        success = (not self.isEmpty())          #continue if Queue not empty

        if(success):
            success = self.head.ticket          #return ticket at head
            self.head = self.head.next          #head is next field of old head
            self.currentSize -= 1               #decrement size of Queue

        return success

    def front(self):
        """Non-destructive read of the queue. Called by user. Calls
        self.isEmpty to ensure Node is available in the queue.
        Returns a MealTicket if Node in Queue, else returns False."""

        success = (not self.isEmpty())          #continue if Queue not empty

        if(success):
            success = self.head.ticket          #return type MealTicket
                                                #return ticket at head
        return success

    def isEmpty(self):
        """Returns True if size of the Queue equals 0, else returns
        False. Called by self.dequeue, self.front, and user."""

        return (self.currentSize == 0)

    def isFull(self):
        """Returns True if size of the Queue equals the max capacity
        of the Queue. Called by self.enqueue and user."""

        return (self.currentSize == self.maxSize)


#===============================Stack Class===================================#

class Stack():
    """Implementation of a LIFO linked list for a Stack."""

    def __init__(self, capacity):
        self.head = None
        try:
            invalidInput = (capacity < 1)
            if(invalidInput):
                self.maxSize = DEFAULT_CAPACITY
            else:
                self.maxSize = capacity

        except TypeError:
            self.maxSize = DEFAULT_CAPACITY

        self.currentSize = 0

    def push(self, ticket):
        """Creation of a new Node at the head of the linked
        list. Called by user. Calls self.isFull(). Creates
        instance of a Node() class. Returns True if new Node
        is placed on the stack, else False."""


        #continue if ticket is type MealTicket and Stack is not full
        success = (type(ticket) == MealTicket and not self.isFull())

        if(success):
            new = Node(ticket, None)        #new Node instance
            if(self.head != None):          #Stack not empty
                new.next = self.head        #new.next points to old head
            self.head = new                 #head Node becomes new Node
            self.currentSize += 1           #increase size

        return success

    def pop(self):
        """Destructive read of the Stack. Called by user, calls
        self.isEmpty(). Returns MealTicket at head Node, else
        returns False."""

        success = (not self.isEmpty())      #continue if Stack not empty

        if(success):
            success = self.head.ticket      #return ticket at head
            self.head = self.head.next      #head become next of old head
            self.currentSize -= 1           #decrease size

        return success

    def peek(self):
        """Non-destructive read of the Stack. Called by user,
        calls, self.isEmpty(). Returns a MealTicket at the head
        Node, else returns False."""

        success = (not self.isEmpty())      #continue if Stack not empty

        if(success):
            success = self.head.ticket      #return ticket at head

        return success

    def isEmpty(self):
        """Returns True if the size of the Stack is 0, else
        returns False. Called by self.peek(), self.pop() and
        user."""

        return (self.currentSize == 0)

    def isFull(self):
        """Returns True if the size of the Stack equals its
        max capacity, else returns False. Called by self.push()
        and user."""

        return (self.currentSize == self.maxSize)

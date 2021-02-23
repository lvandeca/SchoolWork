""" 
Author: Luke Vandecasteele
Date: 2/22/2021 Last Modified: 2/22/2021
Credits: Class notes and textbook
Description: Implementation of a binary search tree for CIS 313 at University
             of Oregon.
Notes:
        1. Provide better documentation for three functions implemented:
           delete, insert, and find.
"""


from skeleton_lab3 import *
from mealticket import *


# ================================ BST Class ====================================
class BinarySearchTree:
    """
    Description: A Binary Search Tree (BST).
    Note: Algorithms for the BST can be found in ch. 12 of the book.
    """

    def __init__(self):
        """ The constructor for our BST """
        self._root = Sentinel()
        # Add any other instance variables you need.

    def _isValid(self, ticket):
        """
        Description: A method for checking if the given ticket is a valid
                     mealticket.
        Inputs: Some object in the variable ticket.
        Outputs: Boolean (True|False) depending on if it is a valid mealticket.
        """
        return type(ticket) == MealTicket

    def _findMinimum(self, node):
        """
        Description: Finds the minimum child of a tree when given a node.
        Inputs: A node from the BST.
        Outputs: The minumum node from the sub-tree (e.g the left-most child).
        """
        returnValue = False
        if not node.isSentinel():
            returnValue = node
            while not returnValue._leftChild.isSentinel():
                returnValue = returnValue._leftChild
        return returnValue

    def _findSuccessor(self, node):
        """
        Description: Given a node, returns the successor of that node,
                     or False if there is no successor.
        """
        successor = False
        # if node has a right child
        if(node.hasRightChild()):
            # then successor is the min of the right subtree
            successor = self._findMinimum(node._rightChild)
        elif(node._parent):  # node has no right child, but has a parent
            if(node.isLeftChild()):  # node is a left child
                successor = self._parent  # then succ is the parent
            else:  # node is right child, and has not right child
                successor = node._parent
                while not successor._parent.isSentinel() and node.isRightChild():
                    node = successor
                    successor = successor._parent
        return successor

    def _mytransplant(self, uNode, vNode):

        if(uNode._parent.isSentinel()):
            self._root = vNode
            uNode._leftChild = None
            uNode._rightChild = None

        elif(uNode == uNode._parent._leftChild):
            uNode._parent._leftChild = vNode

        else:
            uNode._parent._rightChild = vNode

        if(not vNode.isSentinel()):
            vNode._parent = uNode._parent

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "  "
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(not node.isSentinel()):
            self.inorder(node.getLChild())
            self.output += str(node._key) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(not node.isSentinel()):
            self.output += str(node._key) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(not node.isSentinel()):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + ", "

    def insert(self, ticket):
        """
        Description: Inserts given MealTicket into the tree while
                     preserving binary tree property.
                     Returns True if successful, False otherwise
        """
        status = self._isValid(ticket)

        if(status):
            cNode = self._root
            newNode = Node(ticket)
            pNode = Sentinel()

            while(not cNode.isSentinel()):
                pNode = cNode

                if(newNode < cNode):
                    cNode = cNode.getLChild()
                else:
                    cNode = cNode.getRChild()

            newNode._parent = pNode

            if(pNode.isSentinel()):
                self._root = newNode
            elif(newNode < pNode):
                pNode._leftChild = newNode
            else:
                pNode._rightChild = newNode

        return status

    def delete(self, ticketID):
        """
        Description: Deletes node from tree with given ticketID;
                     restructures binary tree. Returns True if successful,
                     False otherwise
        """
        node = self.find(ticketID)
        status = True
        if(type(node) is bool):
            status = False

        if(status):

            # handles case when node to be deleted has no children
            if(node.isLeaf()):

                if(node.isLeftChild()):
                    node._parent._leftChild = node._leftChild

                    # for garbage collection
                    node = None

                # node is right child
                else:
                    node._parent._rightChild = node._rightChild

                    # for garbage collection
                    node = None

            # handles case when node to be deleted has one children
            if(node.hasOnlyOneChild()):

                # node is a left child
                if(node.isLeftChild()):

                    if(node.hasL)

                # node is right child
                else:

        return status

    def find(self, ticketID):
        """
        Description: Finds node in tree with given ticketID,
                     returns corresponding ticket. Returns False if unsuccessful.
        """
        status = ticketID > 0

        if(status):
            cNode = self._root

            while(not cNode.isSentinel() and ticketID != cNode._key):
                if(ticketID < cNode._key):
                    cNode = cNode._leftChild
                else:
                    cNode = cNode._rightChild

            if(not cNode.isSentinel()):
                status = cNode
            else:
                status = False

        return status

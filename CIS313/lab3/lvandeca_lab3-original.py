"""
Author: Luke Vandecasteele
Date: 2/22/2021 Last Modified: 2/23/2021
Credits: Class notes and textbook
Description: Implementation of a binary search tree for CIS 313 at University
             of Oregon.
Notes:
    1. Own transplant method self._mytransplant(self, uNode, vNode) used
    rather than given methods. Could not get given transplant method to work.
    Lots of errors with various calls within original given transplant method 
    such as line: "if vNode != None:" of which results in many errors. Instead
    I decided to create my own transplant method to make things simpler.
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

    def _mytransplant(self, uNode, vNode):
        """
        Description: Replaces subtree at uNode with subtree at vNode.

        Note: See pg. 296 for description of the transplant routine.

        Args:
            uNode (Node): Node at head of subtree to be replaced
            vNode (Node): Node at head of subtree to be transplanted
        """
        # uNode is the root of the tree
        if(uNode._parent.isSentinel()):
            self._root = vNode

        # uNode is either a right or a left child of a node
        elif(uNode == uNode._parent._leftChild):  # uNode is a left child
            uNode._parent._leftChild = vNode

        else:  # uNode is a right child
            uNode._parent._rightChild = vNode

        # sets parent of vNode if vNode is not a Sentinel Node
        if(not vNode.isSentinel()):
            vNode._parent = uNode._parent

    def insert(self, ticket):
        """ 
        Description: Inserts given MealTicket into the tree while
                         preserving binary tree property.
                         Returns True if successful, False otherwise. Exhibits
                         O(log(n)) behavior since we iterate the depth of the
                         BST which is log(n)

        Args:
            ticket (MealTicket): MealTicket to be inserted in the BST

        Returns:
            Boolean: True is successful, False if not
        """

        # status condition set if input is valid for BST
        status = self._isValid(ticket)

        if(status):
            cNode = self._root  # start at the root
            newNode = Node(ticket)  # new Node instance
            pNode = Sentinel()  # temp storage for parent of cNode

            # iterate down through the depth of the tree
            # produce O(log(n)) behavior since log(n) is the depth of the tree
            while(not cNode.isSentinel()):  # iterate until leaf is hit
                pNode = cNode

                if(newNode < cNode):  # move to left subtree
                    cNode = cNode.getLChild()
                else:
                    cNode = cNode.getRChild()  # move to right subtree

            # bottom node found (cNode is Sentinel())
            # set parent of newNode to pNode
            newNode._parent = pNode

            # BST is empty, set newNode to root
            if(pNode.isSentinel()):
                self._root = newNode

            # not empty, set to either left or right child of pNode
            elif(newNode < pNode):
                pNode._leftChild = newNode  # left child of pNode
            else:
                pNode._rightChild = newNode  # right child of pNode

        return status

    def delete(self, ticketID):
        """
        Description: 
            Deletes node from tree with given ticketID;
            restructures binary tree. Returns True if successful,
            False otherwise

        Notes: 
            Case 1 includes cases when a node has only a right child as
            well as cases when a node has no children since in both
            scenarios node is being transplanted with its right child. 

            Case 2 is when a node has only a left node which is then when
            we transplant the node with its left child.

            Case 3 is when a node has both children, so we find its 
            successor. A conditional then arises. 

                3a: If the successor's parent is the original node 
                (aka the right subtree of the node being deleted only has
                one element), then we only need to transplant the successor 
                with node and set new left child (lines 253-255). This is
                always executed to ensure that the left node is set properly,
                and that successor is the transplanting the deleted node.

                3b: If the successor's parent isn't the original node then 
                we also need to transplant the successor with its right child
                and set the right child of the successor to the right child 
                of the node (lines 247 - 249).

        Args:
            ticketID (int): ticketID of a MealTicket in BST to be deleted

        Returns:
            Boolean: returns True if ticketID is associated to a MealTicket
                     in BST and delete is successfull, False otherwise
        """

        # check if Node with that key is in BST
        node = self.find(ticketID)
        status = True

        # if check returns a False then Node not found
        if(type(node) is bool):
            status = False

        if(status):

            # Case 1 in docstring notes
            if (node._leftChild.isSentinel()):
                self._mytransplant(node, node._rightChild)

            # Case 2 in docstring notes
            elif (node._rightChild.isSentinel()):
                self._mytransplant(node, node._leftChild)

            # Case 3 in docstring notes: node has both children
            else:

                # find successor of node, aka min Node of right subtree
                treeMin = self._findMinimum(node._rightChild)

                # Case 3b in docstring notes
                if(treeMin._parent != node):
                    self._mytransplant(treeMin, treeMin._rightChild)
                    treeMin._rightChild = node._rightChild
                    treeMin._rightChild._parent = treeMin

                # Case 3a in docstring notes, this scenario is always
                # executed for Case 3
                self._mytransplant(node, treeMin)
                treeMin._leftChild = node._leftChild
                treeMin._leftChild._parent = treeMin

            # set all pointers of node deleted to None to ensure
            # removal through garbage collection
            node._leftChild = None
            node._rightChild = None
            node._parent = None

        return status

    def find(self, ticketID):
        """ 
        Description: Finds node in tree with given ticketID,
                         returns corresponding ticket. Returns False
                         if unsuccessful.

        Args:
            ticketID (int): ticketID of a MealTicket in BST

        Returns:
            MealTicket/Boolean: returns MealTicket if ticketID in BST, 
                                False otherwise
        """

        # valid ticketIDs are integers > 0
        status = ticketID > 0

        if(status):

            # start at the root
            cNode = self._root

            # iterate down. Stop when either ticketID is found for a Node in
            # BST, or we have reached a leaf
            while(not cNode.isSentinel() and ticketID != cNode._key):

                # go to left or right subtree depending on comparison between
                # key and ticketID, produces O(log(n)) behavior since we only
                # iterate the depth of the tree
                if(ticketID < cNode._key):
                    cNode = cNode._leftChild  # go to left subtree
                else:
                    cNode = cNode._rightChild  # go to right subtree

            # node found with matching key
            if(not cNode.isSentinel()):
                status = cNode

            # node not found with that ticketID as a key
            else:
                status = False

        return status

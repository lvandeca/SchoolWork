"""
Lab 4 - Red Black Tree
Author: Luke Vandecasteele, Jared Hall
Date: 3/6/2021 Last Modified: 3/7/2021
Description: Implementation of a Red-Black Tree for MealTickets
Notes:
    1. <Anything you think I should know while grading>
"""
from mealticket import *

# ============================== Aux Classes ===================================


class Sentinel():
    """This class builds the Sentinel nodes"""

    def __init__(self):
        """The constructor for the Sentinel class"""
        self._key = None
        self._value = None
        self._leftChild = None
        self._rightChild = None
        self._parent = None
        self._color = "black"

    def __str__(self):
        return "Sentinel()"

    def __repr__(self):
        return "Sentinel()"

    def isSentinel(self):
        """ This method makes it easy to check if a given node is a Sentinel"""
        return True


class RBNode():
    """ This class implements a node for the RBT. """

    def __init__(self, ticket):
        """
        Description: The constructor for the Node class.

        Inputs: A valid MealTicket (input validation should be done by insert)
        """
        self._parent = Sentinel()
        self._leftChild = Sentinel()
        self._rightChild = Sentinel()
        self._value = ticket
        self._key = ticket.ticketID
        self._color = "red"

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        return "key: {}, color: {}".format(self._key, self._color)

    def __repr__(self):
        returnValue = "RBNode("
        returnValue += "key: {}, ".format(self._key)
        returnValue += "color: {})".format(self._color)
        return returnValue

    def isSentinel(self):
        """ A helper method for figureing out if a node is a Sentinel """
        return False

    # Accessor Methods
    def getColor(self):
        """
        Description: This method returns the color.
        """
        return self._color

    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        """
        return self._parent

    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        """
        return self._rightChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        """
        return self._leftChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the MealTicket.
        """
        return self._value

    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.

        Input: A Node() reference.
        """
        self._parent = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.

        Input: A Node() reference.
        """
        self._leftChild = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.

        Input: A Node() reference.
        """
        self._rightChild = node

    def setColor(self, color):
        """
        Description: This method sets the color
        """
        self._color = color

    # comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes. Now we can do node1 > node2.

        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key > other._key
        return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes. Now we can do node1 < node2.

        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key < other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes. Now we can do node1 == node2.

        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes. Now we can do node1 != node2.

        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key != other._key
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes. Now we can do node1 <= node2.

        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key <= other._key
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes. Now we can do node1 >= node2.

        Input: Another instance of the node class.
        """
        returnValue = False
        if(not self.isSentinel() and not other.isSentinel()):
            returnValue = self._key >= other._key
        return returnValue

    # Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node has a left
                     child
        """
        returnValue = False
        cond1 = not self._leftChild.isSentinel()
        cond2 = self._leftChild._parent is self
        if(cond1 and cond2):
            returnValue = True
        return returnValue

    def hasRightChild(self):
        """ This method returns true|false depending on if the current node has
            a right child or not."""
        returnValue = False
        cond1 = not self._rightChild.isSentinel()
        cond2 = self._rightChild._parent is self
        if(cond1 and cond2):
            returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """ Returns True if the current node has only one child."""
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """ Returns True if the current node has both children"""
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """ Returns true if the current node is a leaf node."""
        returnValue = False
        if(self._rightChild.isSentinel() and self._leftChild.isSentinel()):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """Returns true if the current node is a left child"""
        cond1 = not self._parent.isSentinel()
        cond2 = self._parent._leftChild is self
        cond3 = self._parent._rightChild is not self
        return cond1 and cond2 and cond3

    def isRightChild(self):
        """Returns true if the current node is a right child"""
        cond1 = not self._parent.isSentinel()
        cond2 = self._parent._rightChild is self
        cond3 = self._parent._leftChild is not self
        return cond1 and cond2 and cond3
# ==============================================================================


class RedBlackTree:
    """ Skeleton code for the red-black tree"""

    def __init__(self):
        """ The constructor for the red-black tree"""
        self._root = Sentinel()
        self._treeHeight = 0
        self.output = ""

    def __repr__(self):
        returnValue = "RedBlackTree("
        returnValue += "height: {}, ".format(self._treeHeight)
        returnValue += "root: {}, ".format(repr(self._root))
        returnValue += "preorder: {})".format(self.traverse("repr pre-order"))
        return returnValue

    def __str__(self):
        return self.traverse("in-order")

    def _isRoot(self, node):
        """
        Description: This function returns true if the given node is the root.
        """
        return node is self._root

    def _isEmpty(self):
        """
        Description: This method returns true if the tree is empty, else False.
        """
        return self._root.isSentinel()

    def _isValid(self, ticket):
        """
        Description: A method for checking if the given ticket is a valid
                     mealticket.

        Inputs: Some object in the variable ticket.

        Outputs: Boolean (True|False) depending on if it is a valid mealticket.
        """
        return type(ticket) == MealTicket

    def _transplantR(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child to
                     the current nodes parent.

        Notes: 1. Do not call this method when cNode is the root. 2. Don't
                forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getRChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def _transplantL(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child to
                     the current nodes parent.

        Notes: 1. Do not call this method when cNode is the root. 2. Don't
                forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getLChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep of the tree
                     according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "repr pre-order"):
                self.reprPreorder(self._root)
            elif(mode == "repr post-order"):
                self.reprPostorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "  "
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(not node.isSentinel()):
            self.inorder(node.getLChild())
            self.output += str(node._key) + " " + str(node._color) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(not node.isSentinel()):
            self.output += str(node._key) + " " + str(node._color) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def reprPreorder(self, node):
        """computes the pre-order traversal"""
        if(not node.isSentinel()):
            self.output += repr(node) + ", "
            self.reprPreorder(node.getLChild())
            self.reprPreorder(node.getRChild())

    def reprPostorder(self, node):
        """computes the pre-order traversal"""
        if(not node.isSentinel()):
            self.output += repr(node) + ", "
            self.reprPostorder(node.getLChild())
            self.reprPostorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(not node.isSentinel()):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + " " + str(node._color) + ", "

    def _findMinimum(self, node):
        """
        Description: Finds the minimum child of a tree when given a node.

        Inputs: A node from the BST.

        Outputs: The minumum node from the sub-tree (e.g the left-most child).
        """
        returnValue = False
        if not node.isSentinel():
            returnValue = node
            while not returnValue.getLChild().isSentinel():
                returnValue = returnValue.getLChild()
        return returnValue

    def _findSuccessor(self, node):
        """
        Description: Given a node, returns the successor of that node, or False
                     if there is no successor.

        """
        succ = False
        # if node has a right child
        if(node.hasRightChild()):
            # then successor is the min of the right subtree
            succ = self._findMinimum(node._rightChild)
        # node has no right child, but has a parent
        elif(node.getParent().isSentinel()):
            if(node.isLeftChild()):  # node is a left child
                succ = node.getParent()  # then succ is the parent
            else:  # node is right child, and has not right child
                succ = node.getParent()
                while not succ.getParent().isSentinel() and node.isRightChild():
                    node = succ
                    succ = succ.getParent()
        return succ

    # =========================== Manditory Methods ============================
    # You write these. I will update with BST solution on saturday.
    def find(self, ticketID):
        """ Hints: This method returns either a stored mealticket or False just
                   like in the BST lab. Start at the root then make your way to
                   the RBNode whose ticketID matches the input. Then return the
                   value of that node.
        """
        ret = False
        if(type(ticketID) == int and ticketID > 0):
            currentNode = self._root
            while(not currentNode.isSentinel()):
                if(currentNode._key == ticketID):
                    ret = currentNode.getValue()
                    break
                elif(ticketID < currentNode._key):
                    currentNode = currentNode.getLChild()
                else:
                    currentNode = currentNode.getRChild()
        return ret

    def delete(self, ticketID):
        """ The delete method starts out the same as BST but then you need to
            restructure your RBT.
        """
        ret = False
        if(type(ticketID) == int and ticketID > 0):
            currentNode = self.findNode(ticketID)
            if(type(currentNode) == RBNode):
                ret = True
                y = currentNode
                yColor = y._color
                if(currentNode._leftChild.isSentinel()):
                    x = currentNode._rightChild
                    self.RBTransplant(currentNode, currentNode._rightChild)
                elif(currentNode._rightChild.isSentinel()):
                    x = currentNode._leftChild
                    self.RBTransplant(currentNode, currentNode._leftChild)
                else:
                    y = self._findMinimum(currentNode._rightChild)
                    yColor = y._color
                    x = y._rightChild

                    if(y._parent == currentNode):
                        x._parent = y
                    else:
                        self.RBTransplant(y, y._rightChild)
                        y._rightChild = currentNode._rightChild
                        y._rightChild._parent = y
                    self.RBTransplant(currentNode, y)
                    y._leftChild = currentNode._leftChild
                    y._leftChild._parent = y
                    y._color = currentNode._color
                if(yColor == "black"):
                    self.deleteFixup(x)
                self._treeHeight -= 1
                currentNode.setLChild(None)
                currentNode.setRChild(None)
                currentNode.setParent(None)
        return ret

    def insert(self, ticket):
        """
        Hints: add a key to the tree. Don't forget to fix up the tree and
        balance the nodes.
        """
        ret = False
        if(self._isValid(ticket)):
            newNode = RBNode(ticket)
            ret = True
            nextNode = Sentinel()
            currentNode = self._root

            while(not currentNode.isSentinel()):
                nextNode = currentNode

                if(newNode < currentNode):
                    currentNode = currentNode._leftChild
                else:
                    currentNode = currentNode._rightChild

            newNode._parent = nextNode
            if(nextNode.isSentinel()):
                self._root = newNode
            elif(newNode < nextNode):
                nextNode._leftChild = newNode
            else:
                nextNode._rightChild = newNode

            self.insertFixup(newNode)
            self._treeHeight += 1

        return ret

    # ========================== Additional Methods ============================
    # I think these are useful. Implement them if you want.
    def findNode(self, ticketID):
        """  
        Description: This method finds a node and returns it or false if no node is
                     found. First do a BST search for the RBNode with the same key as
                     the input ticketID. Then return that node.

        Returns:
            bool/RBNode: returns a node if found, else returns False
        """

        # similar to find but returns a node (used internally for find sucessor
        # and delete). Same steps as above, just return currentNode

        ret = False
        if(type(ticketID) == int and ticketID > 0):
            currentNode = self._root
            while(not currentNode.isSentinel()):
                if(currentNode._key == ticketID):
                    ret = currentNode
                    break
                elif(ticketID < currentNode._key):
                    currentNode = currentNode.getLChild()
                else:
                    currentNode = currentNode.getRChild()
        return ret

    def RBTransplant(self, uNode, vNode):

        uParent = uNode.getParent()
        if(uParent.isSentinel()):
            self._root = vNode
        elif(uNode.isLeftChild()):
            uParent._leftChild = vNode
        else:
            uParent._rightChild = vNode
        vNode._parent = uParent

    def insertFixup(self, currentNode):
        """Hint: write a function to balance your tree after inserting"""

        while(currentNode.getParent()._color == "red"):
            nodeParent = currentNode.getParent()
            nodeGrandParent = nodeParent._parent

            if(nodeParent.isLeftChild()):

                nodeUncle = nodeGrandParent._rightChild
                if(nodeUncle._color == "red"):
                    nodeParent._color = "black"
                    nodeUncle._color = "black"
                    nodeGrandParent._color = "red"
                    currentNode = nodeGrandParent

                else:
                    if(currentNode.isRightChild()):
                        currentNode = nodeParent
                        self.leftRotate(currentNode)
                    currentNode._parent._color = "black"
                    currentNode._parent._parent._color = "red"
                    self.rightRotate(nodeGrandParent)

            else:

                nodeUncle = nodeGrandParent._leftChild
                if(nodeUncle._color == "red"):
                    nodeParent._color = "black"
                    nodeUncle._color = "black"
                    nodeGrandParent._color = "red"
                    currentNode = nodeGrandParent

                else:
                    if(currentNode.isLeftChild()):
                        currentNode = nodeParent
                        self.rightRotate(currentNode)
                    currentNode._parent._color = "black"
                    currentNode._parent._parent._color = "red"
                    self.leftRotate(nodeGrandParent)

        self._root._color = "black"

    def deleteFixup(self, currentNode):
        """
        Hint: receives a node and fixes up the tree, balancing from that node.
        """
        while(not currentNode == self._root and currentNode._color == "black"):
            if(currentNode == currentNode._parent._leftChild):
                uncleNode = currentNode._parent._rightChild

                if(uncleNode._color == "red"):
                    uncleNode._color = "black"
                    currentNode._parent._color = "red"
                    self.leftRotate(currentNode._parent)
                    uncleNode = currentNode._parent._rightChild

                if(uncleNode._leftChild._color == "black" and uncleNode._rightChild._color == "black"):
                    uncleNode._color = "red"
                    currentNode = currentNode._parent

                else:
                    if(uncleNode._rightChild._color == "black"):
                        uncleNode._leftChild._color = "black"
                        uncleNode._color = "red"
                        self.rightRotate(uncleNode)
                        uncleNode = currentNode._parent._rightChild
                    uncleNode._color = currentNode._parent._color
                    currentNode._parent._color = "black"
                    uncleNode._rightChild._color = "black"
                    self.leftRotate(currentNode._parent)
                    currentNode = self._root
            else:
                uncleNode = currentNode._parent._leftChild

                if(uncleNode._color == "red"):
                    uncleNode._color = "black"
                    currentNode._parent._color = "red"
                    self.rightRotate(currentNode._parent)
                    uncleNode = currentNode._parent._leftChild

                if(uncleNode._rightChild._color == "black" and uncleNode._leftChild._color == "black"):
                    uncleNode._color = "red"
                    currentNode = currentNode._parent

                else:
                    if(uncleNode._leftChild._color == "black"):
                        uncleNode._rightChild._color = "black"
                        uncleNode._color = "red"
                        self.leftRotate(uncleNode)
                        uncleNode = currentNode._parent._leftChild
                    uncleNode._color = currentNode._parent._color
                    currentNode._parent._color = "black"
                    uncleNode._leftChild._color = "black"
                    self.rightRotate(currentNode._parent)
                    currentNode = self._root
        currentNode._color = "black"

    def leftRotate(self, currentNode):
        """
        Description: perform a left rotation from a given node.

        Note: This function runs in O(1) time and only changes pointers between
              nodes. The color of nodes is altered in deleteFixup and 
              insertFixup.
        """

        # get currentNode's right child
        nodeRight = currentNode.getRChild()
        # set currentNode's right subtree to nodeRight's left subtree
        currentNode._rightChild = nodeRight._leftChild

        # nodeRight is not a sentinel, then push up its left child
        if(not nodeRight.isSentinel()):
            nodeRight._leftChild._parent = currentNode

        # set nodeRight's parent to currentNode's old parent
        # i.e. shift nodeRight up the tree
        nodeRight._parent = currentNode._parent

        # currentNode was the root, make nodeRight new root
        if(currentNode._parent.isSentinel()):
            self._root = nodeRight

        # check if current node is a right or left child
        # then replace its spot with nodeRight
        elif(currentNode.isLeftChild()):
            currentNode._parent._leftChild = nodeRight

        else:
            currentNode._parent._rightChild = nodeRight

        # put currentNode on nodeRight left (i.e. shift currentNode down)
        # and set corrent parent
        nodeRight._leftChild = currentNode
        currentNode._parent = nodeRight

    def rightRotate(self, currentNode):
        """
        Description: perform a right rotation from a given node

        Notes: See comments in self.leftRotate for clarification.
        """
        # see self.leftRotate, this method is exactly the same but with left and
        # right switched to perform a rotation to the right

        nodeLeft = currentNode.getLChild()
        currentNode._leftChild = nodeLeft._rightChild

        if(not nodeLeft._rightChild.isSentinel()):
            nodeLeft._rightChild._parent = currentNode

        nodeLeft._parent = currentNode._parent

        if(currentNode._parent.isSentinel()):
            self._root = nodeLeft

        elif(currentNode.isRightChild()):
            currentNode._parent._rightChild = nodeLeft

        else:
            currentNode._parent._leftChild = nodeLeft

        nodeLeft._rightChild = currentNode
        currentNode._parent = nodeLeft

    # ====================== Extra helper function ============================

    def check(self, node, blackHeight):
        """
        Description: Extra helper function to recursively check that the current
                     tree conforms to the definition of a Red-Black Tree for 
                     testing.

        Args:
            node (RBNode): top of tree to begin testing on
            blackHeight (int): counter for the number of black nodes hit 
                               during the recursion

        Returns:
            tuple: returns True/False depending on if tree conforms to 
                   standards, as well as a potential error message for debugging
        """

        # assume tree is empty, so tree is Red-Black
        status = True, blackHeight
        # get left and right child for recursive check
        left = node._leftChild
        right = node._rightChild
        # step 1: check that root is black
        if(self._root._color != "black"):
            return "Root node is not black", blackHeight
        # update black height for step 3
        if(node._color == "black"):
            blackHeight += 1

        # we have reached bottom of tree, all tests passed
        if(node.isSentinel()):
            return True, blackHeight

        # node is red, enter the recursion
        elif(node._color == "red"):
            # step 2: check that red node has only black children
            if(left._color == "black" and right._color == "black"):
                status = True, blackHeight
            # return error message for red children without two black children
            else:
                nK = node._key
                rK = right._key
                rC = right._color
                lK = left._key
                lC = left._color
                ret = f"Both children of node: {nK} are not black--"
                ret += f"Right child: ({rK}, {rC}) Left child: ({lK}, {lC})"
                return ret, blackHeight

        # perform recursion to check subtrees for same conditions
        leftCheck = self.check(left, 0)
        rightCheck = self.check(right, 0)

        # step 3: check to make sure the the blackHeight for each subtree is
        # equal (aka that all simple paths to the leaves have the same number of
        # black nodes), if not equal, generate and return error message
        if(leftCheck[1] != rightCheck[1]):
            ret = "Number of black nodes unequal: "
            ret += f"Left child: {left} height: {leftCheck[1]} -- "
            ret += f"Right child: {right} height: {rightCheck[1]}"
            return ret, blackHeight
        # subtrees have same number of black nodes, increment blackHeight
        # counter by the count for the subtrees
        blackHeight += leftCheck[1]

        # check the both of the subtrees didn't violate step 1 or 2
        subCheck = (type(leftCheck[0]) != str and type(rightCheck[0]) != str)
        # subtree's check was successfull
        if(subCheck):
            status = True, blackHeight
        # return the error message for which subtree failed
        elif(type(leftCheck[0]) != bool):
            return leftCheck[0], blackHeight
        else:
            return rightCheck[0], blackHeight

        return status

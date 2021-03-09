from __future__ import print_function
import sys
import time

# status generator


def range_with_status(total):
    n = 0
    while n < total:
        done = '#'*(n+1)
        todo = '-'*(total-n-1)
        s = '<{0}>'.format(done+todo)
        if not todo:
            s += '\n'
        if n > 0:
            s = '\r'+s
        sys.stdout.write(s)
        sys.stdout.flush()
        yield n
        n += 1


print('doing something ...')
for i in range_with_status(3):
    time.sleep(0.1)

print('ready')
time.sleep(0.4)


print('And now for something completely different ...')
time.sleep(0.5)
msg = 'I am going to erase this line from the console window.'
sys.stdout.write(msg)
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\r' + ' '*len(msg))
sys.stdout.flush()
time.sleep(0.5)
print('\rdid I succeed?')
time.sleep(4)

"""
def delete(self, ticketID):
     The delete method starts out the same as BST but then you need
            to restructure your RBT.
      ret = False
       if(type(ticketID) == int and ticketID > 0):
            currentNode = self.find(ticketID)
            if(type(currentNode) == RBNode):
                ret = True
                # Step-02: If the node is a leaf - just delete it
                if(currentNode.isLeaf()):
                    parent = currentNode.getParent()
                    if(currentNode is self._root):
                        self._root = Sentinel()
                    elif(currentNode.isLeftChild()):
                        parent.setLChild(Sentinel())
                    else:
                        parent.setRChild(Sentinel())
                    currentNode.setParent(None)
                    currentNode.setLChild(None)
                    currentNode.setRChild(None)

                # Step-02: If the node has only one child then transplant
                elif(currentNode.hasOnlyOneChild()):
                    if(currentNode.hasLeftChild()):
                        # transplant left
                        if(currentNode is self._root):
                            self._root = currentNode.getLChild()
                        else:
                            self._transplantL(currentNode)
                    else:
                        # transplant right
                        if(currentNode is self._root):
                            self.root = currentNode.getRChild()
                        else:
                            self._transplantR(currentNode)
                    currentNode.setParent(None)
                    currentNode.setLChild(None)
                    currentNode.setRChild(None)

                # Step-03: If the node has both children - Find successor
                else:
                    successor = self._findSuccessor(currentNode)
                    self.delete(successor._key)
                    currentNode._value = successor._value
                    currentNode._key = successor._key
        return ret
"""

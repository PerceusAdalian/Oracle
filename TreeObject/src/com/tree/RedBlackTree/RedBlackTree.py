'''
Created on 3/13/2026
Author: Perceus Willy
Github: https://github.com/PerceusAdalian
Lines: 343 (Including this line)

Project Definition:
This project implements a Red-Black Tree, a self-balancing binary search tree that maintains balance
through a set of properties and rules. The Red-Black Tree ensures that the tree remains approximately balanced, 
providing efficient search, insertion, and deletion operations.

Class Definitions:
- Node: Represents a node in the Red-Black Tree, containing data, color, and pointers to left and right children and parent.
- RedBlackTree: Contains methods for inserting, deleting, searching, and validating the Red-Black Tree properties, as well as performing rotations and traversals

Methods:
- rotateLeft(node): Performs a left rotation around the given node.
- rotateRight(node): Performs a right rotation around the given node.
- traversal_io(node): Inorder traversal of the tree, printing node data and color.
- search(node): Searches for a node with the given data and returns it if found.
- getMinimum(node): Returns the node with the minimum value in the subtree rooted at the given node.
- getMaximum(node): Returns the node with the maximum value in the subtree rooted at the given node.
- getSuccessor(node): Returns the successor of the given node in the tree.
- getPredecessor(node): Returns the predecessor of the given node in the tree.
- contains(node): Checks if a node with the given data exists in the tree.
- size(node): Returns the number of nodes in the subtree rooted at the given node.
- height(node): Returns the height of the subtree rooted at the given node.
- blackHeight(node): Returns the black height of the subtree rooted at the given node.
- validate(): Validates the Red-Black Tree properties.
- insert(data): Inserts a new node with the given data into the tree.
- delete(node): Deletes the given node from the tree.
- fixInsert(node): Fixes the tree after insertion to maintain Red-Black properties.
- fixDelete(node): Fixes the tree after deletion to maintain Red-Black properties.

Example Usage:
- Utilizes the main functions of this class to demonstrate the insertion of nodes, traversal, and validation of the Red-Black Tree properties in main.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'  # New nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)  # Sentinel node for leaves
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotateRight(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def traversal_io(self, node):
        if node != self.NIL:
            self.traversal_io(node.left)
            print(f"{node.data} ({node.color})", end=' ')
            self.traversal_io(node.right)

    def search(self, node):
        current = self.root
        while current != self.NIL:
            if node.data == current.data:
                return current
            elif node.data < current.data:
                current = current.left
            else:
                current = current.right
        return None  # Not found
    
    def getMinimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def getMaximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node
    
    def getSuccessor(self, node):
        if node.right != self.NIL:
            return self.minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent
    
    def getPredecessor(self, node):
        if node.left != self.NIL:
            return self.maximum(node.left)
        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent
        return parent
    
    def contains(self, node):
        return self.search(node.data) is not None
    
    def size(self, node):
        if node == self.NIL:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
    
    def height(self, node):
        if node == self.NIL:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def blackHeight(self, node):
        if node == self.NIL:
            return 0
        left_black_height = self.blackHeight(node.left)
        right_black_height = self.blackHeight(node.right)
        if left_black_height != right_black_height:
            raise Exception("Red-Black Tree property violated: black heights differ")
        return left_black_height + (1 if node.color == 'BLACK' else 0)
    
    def validate(self):
        if self.root.color != 'BLACK':
            raise Exception("Red-Black Tree property violated: root is not black")
        self.validateNode(self.root)
    
    def validateNode(self, node):
        if node == self.NIL:
            return 1  # Black height of NIL is 1
        if node.color == 'RED':
            if node.left.color == 'RED' or node.right.color == 'RED':
                raise Exception("Red-Black Tree property violated: red node has red child")
        left_black_height = self.validateNode(node.left)
        right_black_height = self.validateNode(node.right)
        if left_black_height != right_black_height:
            raise Exception("Red-Black Tree property violated: black heights differ")
        return left_black_height + (1 if node.color == 'BLACK' else 0)
    
    def transplant(self, node, value):
        if node.parent is None:
            self.root = value
        elif node == node.parent.left:
            node.parent.left = value
        else:
            node.parent.right = value
        value.parent = node.parent 

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self.insertNode(new_node)

    def insertNode(self, new_node):
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node  # Tree was empty
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.fixInsert(new_node)

    def fixInsert(self, new_node):
        while new_node != self.root and new_node.parent.color == 'RED':
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.color == 'RED':
                    # Case 1: Uncle is red (recoloring)
                    new_node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    new_node = new_node.parent.parent
                else:
                    # Case 2: Uncle is black (rotation needed)
                    if new_node == new_node.parent.right:
                        # Case 2a: New node is right child (left rotation needed)
                        new_node = new_node.parent
                        self.rotateLeft(new_node)
                    # Case 3: New node is left child (right rotation needed)
                    new_node.parent.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    self.rotateRight(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.color == 'RED':
                    # Case 1: Uncle is red (recoloring)
                    new_node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    new_node = new_node.parent.parent
                else:
                    # Case 2: Uncle is black (rotation needed)
                    if new_node == new_node.parent.left:
                        # Case 2a: New node is left child (right rotation needed)
                        new_node = new_node.parent
                        self.rotateRight(new_node)
                    # Case 3: New node is right child (left rotation needed)
                    new_node.parent.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    self.rotateLeft(new_node.parent.parent)

    def delete(self, node):
        if node is None:
            return  # Node not found, nothing to delete
        self.deleteNode(node)
    
    def deleteNode(self, node):
        original_color = node.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if original_color == 'BLACK':
            self.fixDelete(x)
    
    def fixDelete(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.rotateLeft(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self.rotateRight(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self.rotateLeft(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.rotateRight(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self.rotateLeft(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self.rotateRight(node.parent)
                    node = self.root
        node.color = 'BLACK'

# Example usage
def main():
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)

    print("Inorder Traversal of Red-Black Tree:")
    rbt.traversal_io(rbt.root)
    print()

    print("Tree contains 20:", rbt.contains(Node(20)))
    print("Tree size:", rbt.size(rbt.root))
    print("Tree height:", rbt.height(rbt.root))
    print("Tree black height:", rbt.blackHeight(rbt.root))
    rbt.validate()  # Validate the Red-Black Tree properties

if __name__ == "__main__":
    main()
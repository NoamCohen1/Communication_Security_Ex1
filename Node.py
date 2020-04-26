"""
The class creates Nodes for the merkle
tree.
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def find_largest(self):
        if self.root is None:
            raise ValueError("The tree is empty")
        return self._find_largest(self.root)

    def _find_largest(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.key

    def find_smallest(self):
        if self.root is None:
            raise ValueError("The tree is empty")
        return self._find_smallest(self.root)

    def _find_smallest(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def find_sum(self):
        return self._find_sum(self.root)

    def _find_sum(self, node):
        if node is None:
            return 0
        return node.key + self._find_sum(node.left) + self._find_sum(node.right)

    def plot_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        plt.figure(figsize=(10, 8))
        self._plot_tree(self.root, 0, 0, 20)
        plt.axis('off')
        plt.show()

    def _plot_tree(self, node, x, y, x_offset):
        if node is not None:
            plt.text(x, y, str(node.key), ha="center", va="center",
                     bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='circle'))
            if node.left is not None:
                plt.plot([x, x - x_offset], [y, y - 2], 'k-')
                self._plot_tree(node.left, x - x_offset, y - 2, x_offset / 2)
            if node.right is not None:
                plt.plot([x, x + x_offset], [y, y - 2], 'k-')
                self._plot_tree(node.right, x + x_offset, y - 2, x_offset / 2)

bst = BinarySearchTree()
values = [15, 10, 28, 8, 3, 11, 25]
for v in values:
    bst.insert(v)

largest_value = bst.find_largest()
print("Largest value in the tree:", largest_value)

smallest_value = bst.find_smallest()
print("Smallest value in the tree:", smallest_value)

total_sum = bst.find_sum()
print("Sum of all values in the tree:", total_sum)

bst.plot_tree()

import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize - 1

# a binary tree node
class Node:
  def __init__(self, item):
    self.item = item
    self.left = None
    self.right = None

# returns true if the given tree is a BST
def is_bst(node):
  return __is_bst__(node, MIN_INT, MAX_INT)

def __is_bst__(node, min, max):
  if node is None:
    return True

  if node.item < min or node.item > max:
    return False

  return __is_bst__(node.left, min, node.item - 1) and __is_bst__(node.right, node.item + 1, max)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(is_bst(root))
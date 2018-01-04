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
# first approach = first do an inroder traversal of the tree
def is_bst_inorder(node):
  tree = __inorder__(node)
  for n in range(len(tree) - 1):
    if tree[n].item > tree[n + 1].item:
      return False
  return True

def __inorder__(n, nodes = []):
  if n.left:
    __inorder__(n.left, nodes)
  nodes.append(n)
  if n.right:
    __inorder__(n.right, nodes)
  return nodes

# second approach = keeping track of min and max 
# and check left and right subtress recursively
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

# print(is_bst(root))
print(is_bst_inorder(root))
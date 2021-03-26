# A class to store a binary tree node
class Node:
    def __init__(self, info=None, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


# Recursive function to perform preorder traversal on the tree and fill the dictionary.
# Here, the node has `dist` horizontal distance from the tree's root,
# and the level represents the node's level.
def exploreTop(root, h_dist, level, hdl_dict):
    # base case: empty tree
    if root is None:
        return

    if h_dist not in hdl_dict or level < hdl_dict[h_dist][1]:
        # update value and level for current distance
        hdl_dict[h_dist] = (root.info, level)

    exploreTop(root.left, h_dist - 1, level + 1, hdl_dict)
    exploreTop(root.right, h_dist + 1, level + 1, hdl_dict)


# Function to print the top view of a given binary tree
def printTopView(root):
    hdl_dict = {}
    exploreTop(root, 0, 0, hdl_dict)
    for hd in sorted(hdl_dict.keys()):
        print(hdl_dict.get(hd)[0], end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printTopView(root)
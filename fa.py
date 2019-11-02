class TreeNode:
    def __init__(self, node, children=None):
        self.node = node
        self.children = children

    def __str__(self):
        return str(self.node)


def display_tree(root, count=0):
    print(root, end=" ")
    if root.children is None:
        return
    for i in root.children:
        display_tree(i)


n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)
n12 = TreeNode(12)
n13 = TreeNode(13)
n14 = TreeNode(14)
n15 = TreeNode(15)
n16 = TreeNode(16)
n17 = TreeNode(17)

n0.children = [n1, n2, n3]
n1.children = [n4]
n4.children = [n9]
n2.children = [n5, n6]
n5.children = [n10, n11]
n6.children = [n12, n13, n14]
n13.children = [n17]
n3.children = [n7, n8]
n8.children = [n15, n16]

display_tree(n0, 2)

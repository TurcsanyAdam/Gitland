import json

class TreeNode:
    def __init__(self, node):
        self.children = get_children(node)
        self.node = node

    def __str__(self):
        return str(self.node)


def display_tree(root, row, count=0):
    count += 1
    if count == row:
        print(root, end=" ")
    if root.children is None:
        return
    for i in root.children:
        display_tree(TreeNode(i), row, count)


def get_children(node):
    children = dict()

    with open('vechicles.json', 'r') as f:
        vechicles_dict = json.load(f)

    for vehicle in vechicles_dict:
        if vehicle["parent_category"] in children:
            children[vehicle["parent_category"]].append(vehicle["category"])
        else:
            children[vehicle["parent_category"]] = [vehicle["category"]]
    if node not in children.keys():
        return
    return children[node]


node = TreeNode("Vehicle")
print(display_tree(node, 2))

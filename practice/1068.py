n = int(input())
parents_list = list(map(int, input().split()))

class Node:
    def __init__(self, num):
        self.num = num
    def set(self, parent, children):
        self.parent = parent
        self.children = children
        
node_list = list(Node(i) for i in range(n))

for i in range(n):
    elt = parents_list[i]
    if elt == -1:
        root = elt
    else:
        node_list[i].parent = elt
        node_list[elt].children = i

cutting_node = int(input())
        
class Tree:
    def __init__(self, root, nodes):
        self.root = root
        self.nodes = nodes
    def cut(self, node):
        self.nodes[node].parent.children = None

tree = Tree(root, node_list)

tree.cut(cutting_node)

print(tree)
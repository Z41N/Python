# O(N+E) Time (where N = # of nodes; E = # of edges)
# O(N) Space

# Depth refers to going down each branch
# Breadth is the counterpart; goes to the right
# Semi-recursive?
# Call DfS function on each child node, 1 after 1
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
        return array

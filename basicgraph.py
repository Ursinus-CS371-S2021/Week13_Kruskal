class GraphNode:
    def __init__(self, data = {}):
        self.edges = set([])
        self.data = data

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class Graph:
    def __init__(self):
        self.nodes = []

def make_planar_graph_ex():
    g = Graph()
    for i in range(5):
        g.nodes.append(GraphNode())
    # Add all of 0s edges
    for neighbor in [1, 2, 3, 4]:
        g.nodes[0].edges.add(g.nodes[neighbor])
    # Add all of 2s edges
    for neighbor in [1, 3, 4]:
        g.nodes[2].edges.add(g.nodes[neighbor])
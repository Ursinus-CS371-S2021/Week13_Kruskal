import numpy as np
import matplotlib.pyplot as plt
from unionfind import *

class GraphNode:
    def __init__(self):
        self.edges = []
        self.data = {}

def draw_2d_graph(nodes, edges):
    ax = plt.gca()
    ax.set_facecolor((0.9, 0.9, 0.9))
    for (i, j, d) in edges:
        x1, y1 = nodes[i].data['x'], nodes[i].data['y']
        x2, y2 = nodes[j].data['x'], nodes[j].data['y']
        plt.plot([x1, x2], [y1, y2])
    for i, n in enumerate(nodes):
        plt.scatter(n.data['x'], n.data['y'], 100, c='k')
        plt.text(n.data['x']+0.002, n.data['y']+0.002, "{}".format(i), zorder=10, c='r', fontsize='xx-large')

def make_complete_2D_graph(n_points, seed=0):
    np.random.seed(seed)
    x = np.random.rand(n_points)
    y = np.random.rand(n_points)
    nodes = []
    for i in range(n_points):
        n = GraphNode()
        n.data = {'x':x[i], 'y':y[i]}
        nodes.append(n)
    edges = []
    for i in range(n_points):
        for j in range(i+1, n_points):
            d = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            nodes[i].edges.append((nodes[j], d))
            nodes[j].edges.append((nodes[i], d))
            edges.append((i, j, d))
    return nodes, edges

def dist_of_edge(e):
    return e[2]

def get_mst_kruskal(nodes, edges):
    edges = sorted(edges, key = dist_of_edge)
    djset = UFFast(len(nodes))
    new_edges = []
    roots_last = [i for i in range(len(nodes))]
    

    plt.figure(figsize=(8, 8))
    draw_2d_graph(nodes, new_edges)
    plt.savefig("0.png")
    plot_idx = 1
    total_dist = 0
    for e in edges:
        (i, j, d) = e
        rooti = djset.root(i)
        rootj = djset.root(j)
        c = 'b'
        title = "Adding Edge of Distance %.3g"%d
        if rooti == rootj:
            # Do not add this edge because it would create a cycle
            c = 'r'
            title = "Not " + title
        else:
            # Add edge and update union find
            new_edges.append(e)
            djset.union(i, j)
            total_dist += d
        title += ", total_dist = %.3g"%total_dist
        roots = [djset.root(k) for k in range(len(nodes))]
        title += "\nRoots: "
        for k, r in enumerate(roots):
            s = "{} \\rightarrow {}".format(k, r)
            if roots_last[k] != roots[k]:
                #s = "\\textcolor{red}{" + s + "}"
                s = "**{}**".format(s)
            s = "${}$".format(s)
            title += s + ', '
            if (k+1)%10 == 0:
                title += "\n"
        roots_last = roots
        title = title[0:-2]

        plt.clf()
        draw_2d_graph(nodes, new_edges)
        x1, y1 = nodes[i].data['x'], nodes[i].data['y']
        x2, y2 = nodes[j].data['x'], nodes[j].data['y']
        plt.plot([x1, x2], [y1, y2], linestyle='--', linewidth='5', c=c)
        plt.title(title)
        plt.savefig("{}.png".format(plot_idx))
        plot_idx += 1
        if len(np.unique(roots)) == 1:
            break
    plt.clf()
    draw_2d_graph(nodes, new_edges)
    plt.savefig("{}.png".format(plot_idx))
    return 
    


nodes, edges = make_complete_2D_graph(30, 1)
get_mst_kruskal(nodes, edges)

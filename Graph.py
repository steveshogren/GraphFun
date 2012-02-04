__author__ = 'jack'
from os.path import exists
from subprocess import call

G = {
    'A': {'B': 10, 'D': 4, 'F': 10},
    'B': {'E': 5, 'J': 10, 'I': 17},
    'C': {'A': 4, 'D': 10, 'E': 16},
    'D': {'F': 12, 'G': 21},
    'E': {'G': 4},
    'F': {'H': 3},
    'G': {'J': 3},
    'H': {'G': 3, 'J': 5},
    'I': {},
    'J': {'I': 8},
    }

def printInGraphViz(G):
    dotContents = '';
    for v, pointsTo  in G.items():
        for u, weight in pointsTo.items():
            dotContents += v + ' -> ' + u + ' [label=' + str(weight) + '];'

    return dotContents


def printPathInGraphViz(G, start, end):
    dotContents = '';
    path = Dijkstra(G, start, end)
    for v, pointsTo  in G.items():
        for u, weight in pointsTo.items():
            color = ''
            if path.count(u) and path.count(v):
                color = ' color=red '
            dotContents += v + ' -> ' + u + ' [label=' + str(weight) + color + '];'

    return dotContents


def Dijkstra(G, start, end):
    dist = {}
    previous = {}
    for v in G.keys():
        dist[v] = float('inf')
        previous[v] = None
    dist[start] = 0
    unseen_nodes = G.keys()
    # calculate the shortest path from every node to the start
    while len(unseen_nodes) > 0:
        shortest = None
        u = ''
        for temp_node in unseen_nodes:
            if shortest is None:
                shortest = dist[temp_node]
                u = temp_node
            elif dist[temp_node] < shortest:
                shortest = dist[temp_node]
                u = temp_node
        unseen_nodes.remove(u)

        for v, child_dist in G[u].items():
            alt = dist[u] + child_dist
            if dist[v] > alt:
                dist[v] = alt
                previous[v] = u
    path = []
    u = end
    while previous[u] is not None:
        path.insert(0, u)
        u = previous[u]
    path.insert(0, start)
    return path

dotFile = 'dotTemp.dot'
f = open(dotFile, 'w')
f.write('digraph G {' + printPathInGraphViz(G, 'C', 'I') + '}')
f.close()
output_file = 'graph.png'
if exists(output_file):
    call(['rm', output_file])
call(['dot', '-Tpng', dotFile, '-o' + output_file])


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

def Dijkstra(G, source, end):
    dist = {}
    previous = {}
    for v in G.keys():
        dist[v] = -1
        previous[v] = ""
    dist[source] = 0
    unseen_nodes = G.keys()
    while len(unseen_nodes) > 0:
        shortest = None
        node = ''
        for temp_node in unseen_nodes:
           if shortest == None:
               shortest = dist[temp_node]
               node = temp_node
           elif dist[temp_node] < shortest:
               shortest = dist[temp_node]
               node = temp_node
        unseen_nodes.remove(node)

        for child_node, child_value in G[node].items():
            if dist[child_node] < dist[node] + child_value:
                dist[child_node] = dist[node] + child_value
                previous[child_node] = node
    path = []
    node = end
    while not (node == source):
        if path.count(node) == 0:
            path.insert(0, node)
            node = previous[node]
        else:
            break
    path.insert(0, source)
    return path

dotFile = 'dotTemp.dot'
f= open(dotFile, 'w')
f.write('digraph G {' +  printPathInGraphViz(G, 'C', 'I') + '}')
f.close()
output_file = 'graph.png'
if exists(output_file):
    call(['rm', output_file])
call(['dot', '-Tpng', dotFile, '-o' + output_file])


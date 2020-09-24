import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G,i):
    n = len(G.nodes())
    
    neighbours = [n for n in G.neighbors(i)]   
    neighbours_colours = []
    for neighbour in neighbours:
        neighbours_colours += G.nodes[neighbour]['colour']
        
    m = 1
    while m in neighbours_colours:
        m += 1
        
    return m
    
    
def greedy(G):
    global kmax
    
    n = len(G.nodes())
    
    for i in range(1,n+1):
        G.nodes[i]['colour'] = [0]

    for i in range(1,n+1):
        G.nodes[i]['colour'] = [find_smallest_colour(G,i)]
    
    colours = []    
    for i in range(1,n+1):
        colours += G.nodes[i]['colour']
        
    kmax = max(colours)

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)

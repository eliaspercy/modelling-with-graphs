import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    n = len(G.nodes())
    
    visited_nodes = []
    for i in range(1,n+1):
        if G.nodes[i]['visited'] == ['y']:
            visited_nodes += [i]
     
    neighbours = []
    for node in visited_nodes:
        neighbours += [n for n in G.neighbors(node)]
        
    neighbours.sort()
    for node in neighbours:
        if node not in visited_nodes:
            return node







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
    n = len(G.nodes())
    global kmax
    global visited_counter
    
    
    for i in range(1,n+1):
        G.nodes[i]['colour'] = [0]
        G.nodes[i]['visited'] = ['n']

    G.nodes[1]['colour'] = [find_smallest_colour(G,1)]
    G.nodes[1]['visited'] = ['y']
    
    x = 1
    while x < n:
        v = find_next_vertex(G)
        G.nodes[v]['colour'] = [find_smallest_colour(G,v)]
        G.nodes[v]['visited'] = ['y']
        x += 1 
    
    colours = []    
    for i in range(1,n+1):
        colours += G.nodes[i]['colour']
        
    kmax = max(colours)





    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

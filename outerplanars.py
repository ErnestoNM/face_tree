# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:02:28 2021

@author: Ernesto
"""

import networkx as nx
import numpy as np

def cycle_graph(num_vertx):
    vertx_list = list(range(1, num_vertx + 1))    
    G = nx.Graph()
    G.add_nodes_from(vertx_list)    
    for i in range(-1, nx.number_of_nodes(G) - 1):
        G.add_edge(vertx_list[i], vertx_list[i+1])        
    return(G)

def dfs_iter_id(G, v):
  visited = [False] * nx.number_of_nodes(G) 
  stack = [v]
  while len(stack) > 0:
    v = stack.pop()
    if visited[v-1] == False:
      G.nodes[v]['id'] = v
      G.nodes[v]['left'] = []
      G.nodes[v]['right'] = []
      visited[v-1] = True
      for w in list(G.adj[v]):
        if visited[w-1] == False:
          stack.append(w)
          
def this_edge_exist(G, node_i, node_j, edge):
    edge = list(edge)
    edge.sort()
    edge = tuple(edge)
    if (edge in Graph.nodes[node_i]['left']) or (edge in Graph.nodes[node_i]['right']) or (edge in Graph.nodes[node_j]['left']) or (edge in Graph.nodes[node_j]['right']):
        return True
    else:
        return False
    
def parenthesis_check():
    pass
          
def rndm_edges(G, chance):
  for i in range(1, nx.number_of_nodes(G) + 1):
    for j in range(1, nx.number_of_nodes(G) + 1):
      if i != j and j != i+1 and j != i-1 and not(i==1 and j==nx.number_of_nodes(G)) and not(i==nx.number_of_nodes(G) and j==1): #asegurar que sean una cuerda
        if this_edge_exist(G, i, j, (i, j)) == False:
            rndm_num = np.random.random_sample()
            if rndm_num < chance:
                G.add_edge(i, j)
                if i < j:
                    G.nodes[i]['left'].append((i,j))
                    G.nodes[j]['right'].append((i,j))
                else:
                    G.nodes[i]['right'].append((j,i))
                    G.nodes[j]['left'].append((j,i))
            
if __name__ == '__main__':
    Graph = cycle_graph(7)    
    dfs_iter_id(Graph, 1)
    rndm_edges(Graph, 0.2)
    for i in Graph.nodes:
        print(Graph.nodes(data=True)[i])
    nx.draw_circular(Graph, with_labels = True)
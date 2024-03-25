#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Enable multiple outputs of a cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'


# In[26]:


import networkx as nx
import matplotlib.pyplot as plt 
from networkx.algorithms import bipartite
import numpy 
import pandas as pd


# In[27]:


#NETWORK 3.A

G = nx.MultiGraph()
G.add_nodes_from([1,2,3,4,5,6,7])
edgelist1=[(1,4), (1,6), (1,6), (2,3), (2,5), (2,6), (2,6), (2,6), (2,7), (3,5), (4,7), (5,6), (5,7), (6,7)]
G.add_edges_from( edgelist1 )

pos = nx.spring_layout(G)  
# layout for all nodes 
# draw nodes, labels
nx.draw_networkx_nodes(G, pos, node_size = 200)
nx.draw_networkx_labels(G, pos)
# draw multi-edges
ax = plt.gca()
for e in G.edges:
    ax.annotate("",
                xy=pos[e[0]], xycoords='data',
                xytext=pos[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="-", 
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                ),
                                ),
                );

plt.savefig('MA214_assignment.png');


# In[29]:


#counting the number of nodes and edges, then build adjacency matrix


print('THe number of nodes is', G.number_of_nodes())

print('The number of edges is',G.number_of_edges())


A = nx.adjacency_matrix(G)
print('This is the adjacency Matrix:')
print(A.todense())


# In[30]:


#NETWORK 3.B

G1 = nx.DiGraph()
G1.add_nodes_from(['A','B','C','D','E','F'])
edgelist2=[('A','B'), ('A','D'), ('A','F'), ('B','C'), ('B','E'), ('C','A'), ('D','B'), ('D','E'), ('F','B'), ('F','C'), ('F','E')]
G1.add_edges_from(edgelist2)

pos = nx.circular_layout(G1)  
nx.draw(G1, with_labels=True, font_weight='bold');
plt.savefig('Net_Analysis_net3_b')


# In[31]:


#counting the number of nodes and edges, then build adjacency matrix


print('The number of nodes is', G1.number_of_nodes())

print('The number of edges is', G1.number_of_edges())

A = nx.adjacency_matrix(G1)
print('The adajency matrix is as follows:')
print(A.todense())


# In[36]:


#Bipartite Networks

G3 = nx.Graph()
# List nodes 
nodelist1=[101, 102, 103, 104, 105, 106, 107]
nodelist2=["P1", "P2", "P3", "P4", "P5"]
#Add nodes from mode one
G3.add_nodes_from(nodelist1, bipartite=0)
#Add nodes from mode two
G3.add_nodes_from(nodelist2, bipartite=1)
# Add edges between nodes from two modes
G3.add_edges_from([(101, "P1"), (101, "P2"), (101, "P4"), 
                  (102, "P1"), (102, "P3"), (102, "P4"), (102, "P5"),
                  (103, "P1"), (103, "P2"), 
                  (104, "P2"), (104, "P4"), (104, "P5"),
                  (105, "P3"),
                  (106, "P1"),(106, "P2"),
                  (107, "P3"),(107, "P5")]);

# Set the layout of the network
top = nx.bipartite.sets(G3)[0]
pos = nx.bipartite_layout(G3, top);
#method one allows us to create an image similar to the picture in the assignment with quares and circles

G3.add_nodes_from([101, 102, 103, 104, 105, 106, 107], bipartite=0)  # Set bipartite attribute to 0 for the first group of nodes
G3.add_nodes_from(["P1", "P2", "P3", "P4", "P5"], bipartite=1)  # Set bipartite attribute to 1 for the second group of nodes

pos = nx.bipartite_layout(G3, [101, 102, 103, 104, 105, 106, 107])  # Specify the nodes for the first group
nx.draw_networkx_nodes(G3, pos, nodelist=[101, 102, 103, 104, 105, 106, 107], node_shape='s', node_color='b', alpha=0.5)  # Square nodes for the specified group
nx.draw_networkx_nodes(G3, pos, nodelist=["P1", "P2", "P3", "P4", "P5"], node_shape='o', node_color='r', alpha=0.5)  # Circular nodes for the other group
nx.draw_networkx_edges(G3, pos)
nx.draw_networkx_labels(G3, pos)

plt.axis('off')
plt.show();


# In[37]:


# Draw the network using that layout (method 2 is simpilar and allows us to create the bipartite network with less code but the same shape on both sides)
nx.draw(G3, pos=pos, with_labels=True, node_size=300, 
        node_color=['cyan','cyan','cyan','cyan','cyan', 'cyan', 'cyan','yellow',
                    'yellow','yellow','yellow','yellow'], node_shape= 's');

plt.savefig('Net_Analysis_bi1')


# In[39]:


#incidence matrix

Incidence_m=bipartite.biadjacency_matrix(G3, row_order=nodelist1, 
                   column_order=nodelist2)
print('The incidence Matrix is as follows:')
print(Incidence_m.todense())


# In[43]:


GA = bipartite.projected_graph(G3, nodelist1)
nx.draw(GA, with_labels=True, node_size=300, node_color="green")
plt.savefig('Net_Analysis_biA')
print('The nodes for this network are as follows:', list(GA.nodes()))
print('The edges for this network are as follows:', list(GA.edges()));


# In[44]:


GB = bipartite.projected_graph(G3, nodelist2)
nx.draw(GB, with_labels=True, node_size=300, node_color="green")
plt.savefig('Net_Analysis_biB')
print('The nodes for this network are as follows:',list(GB.nodes()))
print('The edges for this network are as follows:',list(GB.edges()));


# In[ ]:





# In[ ]:





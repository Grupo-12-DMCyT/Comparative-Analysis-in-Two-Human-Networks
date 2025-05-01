import networkx as nx
import numpy as np
import pickle
import matplotlib.pyplot as plt

def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def read_graph_weighted(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_weighted_edges_from(array)
    return G

def get_graph_pos(filename):
  with open(filename, 'rb') as f:
    posData = pickle.load(f)
  return posData

def drop_weights(G):
    '''Drop the weights from a networkx weighted graph.'''
    for node, edges in nx.to_dict_of_dicts(G).items():
        for edge, attrs in edges.items():
            attrs.pop('weight', None)


#calcular eficientemente en grafos muy grandes aproximación a distancias mínimas medias, $<d>$**
#sil: esta función no la vamos a usar no necesitamos samplear (borren si ok)

def sample_path_lengths(G, nodes=None, trials=1000):   #solo para redes muy grandes calcula la media entre una cantidad limitada de pares porque entre miles no tendría sentido.
    if nodes is None:
        nodes = list(G)
    else:
        nodes = list(nodes)

    pairs = np.random.choice(nodes, (trials, 2))
    lengths = [nx.shortest_path_length(G, *pair)
               for pair in pairs]
    return lengths

def estimate_path_length(G, nodes=None, trials=1000):
    return np.mean(sample_path_lengths(G, nodes, trials))

# GRAFICOS  ------------------------------------------------------------------------------
def plotWeightedGraph(G,pos,colorMapping,magnification,nodeSize=45,ax=None):
  values = [v for n,v in colorMapping.items()]
  h=nx.draw_networkx_nodes(G,pos=pos,node_size=nodeSize, node_color = values,ax=ax  , cmap=plt.cm.Reds)
  nx.draw_networkx_labels(G,pos,{n:n for n in G.nodes()},font_size=7,font_color='white' , ax=ax)

  if ax is not None:
    ax.set_axis_off()

  edge_weights = nx.get_edge_attributes(G, "weight")
  edgeWidths=np.array(list(edge_weights.values()))
  edgeWidths=magnification*edgeWidths/np.max(edgeWidths)
  edgeWidths[edgeWidths>0]=edgeWidths[edgeWidths>0]-np.min(edgeWidths[edgeWidths>0])+.5

  nx.draw_networkx_edges(G, pos, edgelist=G.edges(),width=edgeWidths,edge_color='gray')
  plt.colorbar(h)

def plotGraph(G,pos,colorMapping,nodeSize=45,ax=None):
  values = [v for n,v in colorMapping.items()]
  h=nx.draw_networkx_nodes(G,pos=pos,node_size=nodeSize, node_color = values,  ax=ax )
  nx.draw_networkx_labels(G,pos,{n:n for n in G.nodes()},font_size=7,font_color='white', ax=ax)
  if ax is not None:
    ax.set_axis_off()

  edgeWidths=np.ones(G.number_of_edges())

  nx.draw_networkx_edges(G, pos, edgelist=G.edges(),width=edgeWidths,edge_color='red')
  plt.colorbar(h)

# Para resaltar un atributo de un nodo en el grafico
def plotNodeAttribute(G,pos,attribute,exaggeration): #definir el atributo para magnificarlo con esta función por ejemplo tamaño del nodo segun centralidad
  values = [v for n,v in attribute.items()]
  nsize = np.array (values)
  nsize = exaggeration*( nsize - min(nsize))/(max(nsize) - min(nsize))
  nx.draw(G,pos=pos, node_size = nsize, alpha=0.4,node_color = values, edge_color='gray')
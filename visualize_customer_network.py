"""
Visualize Customer Network Detection
Author: Ilias Kamal
Email: ilias.kamal@gmail.com
Date: March 30, 2023

Description: This script uses matplotlib to visualize a customer network.
"""

import matplotlib.pyplot as plt

# Set node positions using Kamada-Kawai layout algorithm
pos = nx.kamada_kawai_layout(G)

# Draw nodes with node size proportional to influence
influence = [G.nodes[n]['influence'] for n in G.nodes()]
node_sizes = [i * 5000 for i in influence]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, alpha=0.7)

# Draw edges with edge width proportional to influence
edge_widths = [G.edges[e]['influence'] for e in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.4)

# Add labels to nodes
labels = {n: n for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10)

# Add a colorbar legend for node size
cbar = plt.colorbar(plt.scatter([], [], c=influence, s=node_sizes, cmap='coolwarm'), shrink=0.5)
cbar.ax.set_ylabel('Influence', rotation=270, labelpad=10)

plt.axis('off')
plt.show()

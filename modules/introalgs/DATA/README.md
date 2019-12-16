//////////////////////////////////////

# DATASET STATISTICS:
No. of nodes: 3,360
No. of edges: 407,791

//////////////////////////////////////

# FILES:

The DATA folder has two files: Edges.csv and Nodes.csv

Nodes.csv contains the list of nodes that appear in Edges.csv and the attributes of each node.
The ID refers to the label of a node and each node is assigned two attributes
(attribute1 and attribute2). Example, node 0 has attribute1 as teen and attribute2 as baseball. The first row is a header of Nodes.csv.

Edges.csv contains the list of edges in an undirected graph. The first row is a header of Edges.csv

//////////////////////////////////////

# READING THE DATA:

The graph can be represented as an adjacency matrix (2D array) of size 3360 X 3360.

Assuming my_adj_matrix[][] represents the adjacency matrix of the graph. If an edge (i,j) exist in my list of edges, then the position my_adj_matrix[i][j] should be set to 1.

Since the graph is undirected, it is expected that the adjacency matrix  my_adj_matrix will be symmetric.

Even though there exist multiple ways of storing the attributes, one simpler approach will be to use any structure that supports key, value pairs (E.g. dictionary in python, Map in Java).  In such case, the keys will be the nodes in the graph and the values will be the attributes.

//////////////////////////////////////
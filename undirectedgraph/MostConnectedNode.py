# Find most connected nodes
# Assumption : Undirected Graph

def nodes_representation(arr):
    in_degree_nodes = {}
    max_var = -1
    nodes = []
    for i in arr:
        n1 = i[0]
        n2 = i[1]

        if in_degree_nodes.get(n1) is not None:
            count = in_degree_nodes.get(n1)
            in_degree_nodes[n1] = count + 1
            if max_var < count + 1:
                max_var = count + 1
        else:
            in_degree_nodes[n1] = 1
            if max_var < 1:
                max_var = 1

        if in_degree_nodes.get(n2) is not None:
            count = in_degree_nodes.get(n2)
            in_degree_nodes[n2] = count + 1
            if max_var < count + 1:
                max_var = count + 1
        else:
            in_degree_nodes[n2] = 1
            if max_var < 1:
                max_var = 1

    for i in in_degree_nodes:
        if in_degree_nodes.get(i) == max_var:
            nodes.append(i)

    nodes.sort()
    return nodes[0], max_var


arr = [('a', 'b'), ('a', 'c'), ('a', 'e'), ('a', 'g'), ('a', 'h'), ('b', 'c'), ('c', 'd'), ('b', 'e'), ('c', 'e')]
# Map : a -> 2 , b -> 3 , c -> 4 , d-> 1 , e -> 2
# MaxConnect variable : x
# List(c).sort()
most_connected_node, max_connection = nodes_representation(arr)
print(most_connected_node, max_connection)

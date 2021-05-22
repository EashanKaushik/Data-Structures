import graph
import sys

def dijkstra(graph, vertex):
    matrix = graph.return_matrix()
    # edge_list = graph.return_edge_list()
    number_of_nodes = graph.number_of_vertices()

    # vertex will have -1 rest will have 0
    parent = [0 if node!= vertex else -1 for node in range(number_of_nodes)]
    # vertex will have 0 rest will have sys.maxsizes
    cost = [sys.maxsize if node != vertex else 0 for node in range(number_of_nodes)]

    # perform relaxation for every node
    iteration = 0
    while iteration < number_of_nodes:

        for source, values in matrix.items():
            for destination, value in values.items():
                if value:
                    # relaxation condition
                     if cost[source] + matrix[source][destination] < cost[destination]:
                         cost[destination] = cost[source] + matrix[source][destination]
                         # destination will have new parent
                         parent[destination] = source

        iteration += 1

    return parent, cost


if __name__ == '__main__':
    graph = graph.Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 4, 3)
    graph.add_edge(4, 3, 2)
    graph.add_edge(3, 5, 1)
    graph.add_edge(4, 5, 5)
    # print(graph.return_edge_list())
    print(dijkstra(graph, 0))

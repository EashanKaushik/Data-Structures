import graph
import sys

def bellman_ford(graph, vertex):
    matrix = graph.return_matrix()
    edge_list = graph.return_edge_list()
    number_of_nodes = graph.number_of_vertices()

    # vertex will have -1 rest will have 0
    parent = [0 if node!= vertex else -1 for node in range(number_of_nodes)]
    # vertex will have 0 rest will have sys.maxsizes
    cost = [sys.maxsize if node != vertex else 0 for node in range(number_of_nodes)]

    # check for update after every iteration if no update we break
    update = False
    iteration = 0
    
    while iteration < number_of_nodes - 1:
        for source, destination in edge_list:
            # relaxation condition
            if cost[source] + matrix[source][destination] < cost[destination]:
                cost[destination] = cost[source] + matrix[source][destination]
                # destination will have new parent
                parent[destination] = source
                update = True

        # if no update was made in current iteration we return
        if not update:
            return parent, cost

        # if update was made we mode forward with loop unitl iteration < number_of_nodes - 1
        update = False
        iteration += 1

    # check for negative edge cycle condition
    for source, destination in edge_list:
        if cost[source] + matrix[source][destination] < cost[destination]:
            cost[destination] = cost[source] + matrix[source][destination]
            parent[destination] = source
            update = True

    # if update was made after number_of_nodes - 1 iteration's we return None i.e. cycle detected
    if update:
        return None

    return parent, cost


if __name__ == '__main__':
    graph = graph.Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)

    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 2, 7)
    graph.add_edge(1, 4, 5)
    graph.add_edge(4, 1, -2)
    graph.add_edge(1, 2, 8)
    graph.add_edge(2, 3, 9)
    graph.add_edge(2, 4, -3)
    graph.add_edge(1, 3, -4)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 0, 2)
    # print(graph.return_edge_list())
    bellman_ford(graph, 0)

class Graph:

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_matrix = {}

    def add_vertex(self, vertex):
        self.number_of_nodes += 1

        if vertex not in self.adjacent_matrix.keys():
            self.adjacent_matrix[vertex] = {key: value for key, value in zip(self.adjacent_matrix.keys(), [0] * (self.number_of_nodes - 1))}
            for key in self.adjacent_matrix.keys():
                self.adjacent_matrix[key][vertex] = 0

    def add_edge(self, vertex1, vertex2, value):
        self.adjacent_matrix[vertex1][vertex2] = value

    def return_matrix(self):
        return self.adjacent_matrix

    def return_edge_list(self):

        edge_list = list()

        for vertex1, values in self.adjacent_matrix.items():

            for vertex2, value in values.items():
                if value:
                    edge_list.append((vertex1, vertex2))

        return edge_list

    def number_of_vertices(self):
        return self.number_of_nodes
    
    def __str__(self):
        return f'{self.adjacent_matrix}'


if __name__ == '__main__':
    graph = Graph()
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
    print(graph)

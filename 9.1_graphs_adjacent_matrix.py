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

    def add_edge(self, vertex1, vertex2):
        self.adjacent_matrix[vertex1][vertex2] = 1
        self.adjacent_matrix[vertex2][vertex1] = 1

    def __str__(self):
        return f'{self.adjacent_matrix}'


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_vertex(0)
    graph.add_edge(2, 0)
    print(graph)

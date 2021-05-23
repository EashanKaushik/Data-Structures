class Graph:

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, vertex):
        self.number_of_nodes += 1

        if vertex not in self.adjacent_list.keys():
            self.adjacent_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjacent_list[vertex1].append(vertex2)
        self.adjacent_list[vertex2].append(vertex1)

    def __str__(self):
        return f'{self.adjacent_list}'


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

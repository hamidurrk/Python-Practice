class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_edges_count(self):
        return len(self.edges)

    def get_in_degree(self, node):
        in_degree = 0
        for start, end in self.edges:
            if end == node:
                in_degree += 1
        return in_degree

    def get_out_degree(self, node):
        x = self.graph_dict.get(node, [])
        return len(x)
    
    def get_degree(self, node):
        x = self.get_in_degree(node) + self.get_out_degree(node)
        return x

if __name__ == '__main__':

    edges= [
        ("7", "2"),
        ("7", "3"),
        ("7", "6"),
        ("2", "1"),
        ("3", "1"),
        ("10", "8"),
        ("10", "9"),
        ("8", "6"),
        ("8", "4"),
        ("5", "3"),
        ("5", "4"),
        ("9", "4"),
    ]

    route_graph = Graph(edges)

    nodes = []
    for edge in edges:
        for node in edge:
            if node not in nodes:
                nodes.append(node)
    print(nodes)

    for node in nodes:
        print("Node:", node)
        print("Degree:", route_graph.get_degree(node))
        print("In-Degree:", route_graph.get_in_degree(node))
        print("Out-Degree:", route_graph.get_out_degree(node))
        print("")

    # start = '6'
    # print("Node:", start)
    # print("Degree:", route_graph.get_degree(start))
    # print("In-Degree:", route_graph.get_in_degree(start))
    # print("Out-Degree:", route_graph.get_out_degree(start))
    # print("")

    print("Number of Edges:", route_graph.get_edges_count())
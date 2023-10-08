import random
import timeit
random.seed(1)


class Graph_random_to_high:

    def __init__(self, degree_sequence):

        # We use a dictionary to represent our graph.
        self.adjacency_list = {}

        # We created a list of visited vertices in the Depth First Search to use
        self.visited = []

        # Take the degree sequence and convert it to a list from text
        self.degree_sequence = self.read_input_txt(degree_sequence)

        # Create a list of vertices with their degrees
        self.vertices = [(i + 1, self.degree_sequence[i]) for i in range(len(self.degree_sequence))]

        # We hold the vertices in a variable to later use in edge interchange
        self.hold_vertices = self.vertices.copy()

        # number of edge interchanges
        self.number_of_interchange = 0

        # variables for timing
        self.start_time = 0
        self.real_time = 0

    def read_input_txt(self, degree_sequence):

        with open(degree_sequence, 'r') as file:
            string_to_list = file.read().split()
            number_list = [int(number) for number in string_to_list]
        return number_list

    def apply_HH_random_to_high(self):

        # we apply Havel-Hakimi to check if the algorithm can generate a graph

        sequence = self.degree_sequence
        sequence.sort(reverse=True)

        # The sum of all degrees has to be even, handshaking lemma
        if sum(sequence) % 2 != 0:
            return False

        while sequence:

            first_vertex_degree = random.choice(sequence)
            sequence.remove(first_vertex_degree)

            if len(sequence) < first_vertex_degree:
                return False

            for i in range(first_vertex_degree):
                sequence[i] -= 1

            sequence.sort(reverse=True)
            list(filter(lambda num: num != 0, sequence))

            # If we get a sequence that is all zeros, then the sequence is graphic

            if not sequence or sequence is None:
                return True

            if len(sequence) == 1 and sequence[0] != 0:
                return False

    def create_graph(self):

        # do preliminary check by using HH
        if self.apply_HH_random_to_high():

            # Add the vertices to the graph
            for vertex, degree in self.vertices:
                self.adjacency_list[vertex] = []

            # Create the graph by connecting vertices randomly, distributed to the highest degree

            while self.vertices and self.vertices[0][1] != 0:

                # Choose a vertex at random, distributed to the highest degree
                random_vertex = random.choice(self.vertices)

                # Remove the chosen vertex from the list
                self.vertices.remove(random_vertex)
                self.vertices.sort(key=lambda x: x[1], reverse=True)

                # Connect the chosen vertex to the next highest degree vertices
                for i in range(random_vertex[1]):
                    if i < len(self.vertices):

                        self.adjacency_list[random_vertex[0]].append(self.vertices[i][0])
                        self.adjacency_list[self.vertices[i][0]].append(random_vertex[0])
                        if self.vertices[i][1] > 0:
                            self.vertices[i] = (self.vertices[i][0], self.vertices[i][1] - 1)
                    # print(self.adjacency_list)

                # sort the list again after the distribution
                self.vertices.sort(key=lambda x: x[1], reverse=True)
                self.vertices = list(filter(lambda x: x[1] != 0, self.vertices))

        else:

            # if the algoirthm fails to generate a graph, we just print 0's and "Algo fails"

            print("Algo fails")
            outputs = ["0", "0", "0", "Algo fails"]
            with open("Group3-250-6225-Input-1-Output-1-HH_random_to_high.txt", "w") as file:

                for output in outputs:
                    line = ' '.join(str(i) for i in output)
                    file.write(line + '\n')
            exit()

    def depth_first_search(self, start, visited):

        # DFS
        visited.append(start)
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)

    def apply_dfs(self):

        # Applying the dfs to check whether the graph is connected or not

        visited = []
        self.depth_first_search(1, visited)

        # return 1 if connected, 0 o/w
        if len(visited) == len(self.adjacency_list):
            self.visited = visited
            return 1

        else:
            self.visited = visited
            return 0

    def pairwise_edge_interchange(self):

        # apply_dfs function gives the visited vertices, and we'll find the unvisited ones
        # we'll end up with a list such as [2, 3, 5], only indicating the numbers of the corresponding vertices
        unvisited = []
        for vertex, degree in self.hold_vertices:
            if vertex not in self.visited:
                unvisited.append(vertex)

        # after finding visited and unvisited vertices, we pick a vertex that's connected to the main graph

        connected_vertex = random.choice(self.visited)

        while len(self.adjacency_list[connected_vertex]) < 2:
            connected_vertex = random.choice(self.visited)

        # we pick a vertex that is adjacent to the selected vertex

        neighbor_of_the_connected = self.adjacency_list[connected_vertex][0]

        # we break the ties

        self.adjacency_list[neighbor_of_the_connected].remove(connected_vertex)
        self.adjacency_list[connected_vertex].pop(0)

        # we pick a vertex that is unvisited and a vertex that is adjacent to that vertex

        disconnected_vertex = random.choice(unvisited)
        neighbor_of_the_disconnected = self.adjacency_list[disconnected_vertex][0]

        # we break the ties

        self.adjacency_list[neighbor_of_the_disconnected].remove(disconnected_vertex)
        self.adjacency_list[disconnected_vertex].pop(0)

        # we re-connect them

        self.adjacency_list[disconnected_vertex].append(connected_vertex)
        self.adjacency_list[connected_vertex].append(disconnected_vertex)

        self.adjacency_list[neighbor_of_the_disconnected].append(neighbor_of_the_connected)
        self.adjacency_list[neighbor_of_the_connected].append(neighbor_of_the_disconnected)

        self.number_of_interchange += 1

    def make_connected(self):

        while not self.apply_dfs():
            self.pairwise_edge_interchange()

    def implementation(self):

        outputs = [str(self.apply_dfs()), str(self.number_of_interchange), str(self.real_time)]

        for neighbors in self.adjacency_list.values():
            neighbors.sort()

        for neighbors in self.adjacency_list.values():
            outputs.append(neighbors)

        with open("Group3-250-6225-Input-1-Output-1-HH_random_to_high.txt", "w") as file:

            for output in outputs:

                line = ' '.join(str(i) for i in output)
                file.write(line + '\n')


example = "Group3-200-3980-Input-4.txt"

graph = Graph_random_to_high(example)

graph.start_time = timeit.default_timer()


graph.create_graph()
graph.make_connected()

graph.real_time = timeit.default_timer() - graph.start_time

graph.implementation()



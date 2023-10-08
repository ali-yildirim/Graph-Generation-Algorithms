import random
import time
random.seed(4)

def apply_sequential_algorithm (input):


    start = time.time()
    Edge_list = []

    Candidate_list = []

    # converting input from string to list

    string_to_list = (input.split())
    degree_sequence = [int(i) for i in string_to_list]

    number_of_vertices = len(degree_sequence)

    # assigning the original degree sequence to a temporary variable 

    degree_sequence_temp = degree_sequence.copy()

    # Sequential Algortihm 

    while sum(degree_sequence) > 0:
    
    # Choose the least i with di a minimal positive entry

        i = degree_sequence.index(min([l for l in degree_sequence if l > 0]))
    # Forming candidate list, checking the if the ij is already in the edge list
        j_candidates = [j for j in range(number_of_vertices) if j != i and (i, j) not in Edge_list and degree_sequence[j] > 0] 

        if not j_candidates:
            break
            print("Not graphical")

    # Check if it is graphical by using Erdös-Gallai algoritm
        for j in j_candidates:

            degree_sequence[i] -= 1
            degree_sequence[j] -= 1

            for k in range(1,(number_of_vertices+1)):

                if (sum(degree_sequence[0:(k-1)])) <= (k*(k-1) + sum(min(k,d)for d in degree_sequence[(k-1):])) :

                    is_graphical = True

                else :

                    is_graphical = False

            if is_graphical == True :

                Candidate_list.append(j)

            degree_sequence = degree_sequence_temp.copy()
 
        # If the Candidate list is empty, it cannot construct a graph, so break
        if not Candidate_list:
            break
            # print("Not graphical")
        #Pick j with probability proportional to its degree until the degree of is 0
        while degree_sequence[i] > 0 and Candidate_list :

            j_probs = [degree_sequence[j] for j in Candidate_list]

            j = random.choices(Candidate_list, weights=j_probs)[0]
        # Add the edge(i,j) to Edge_list
            Edge_list.append((i, j))
        # Remove j from candidate list
            Candidate_list.remove(j)
        # Update degree_sequence
            degree_sequence[i] -= 1
            degree_sequence[j] -= 1

        degree_sequence_temp = degree_sequence.copy()
        Candidate_list = []


    #Check connectivity using BFS
    number_of_interchanges = 0
    visited = set()

    queue = [0]
    # From a dictionary to indicate the adjacent vertices
    adjacency_dict = {}

    for i in range(number_of_vertices):

        adjacency_dict[i] = []
    
    for edge in Edge_list:

        v1, v2 = edge

        adjacency_dict[v1].append(v2)

        adjacency_dict[v2].append(v1)

    while queue:

        vertex = queue.pop(0)

        visited.add(vertex)

        for neighbour in adjacency_dict[vertex]:

            if neighbour not in visited:

                queue.append(neighbour)
    # If all vertices can be visited by the algorithm, it can be said that the graph is connected
    if len(visited) == number_of_vertices:

        print(1)

    else :

        print(0)

    # If the graph is not connected, pairwise edge interchanges are needed
        while True:
    # 2 edges are chosen
            i, j = random.choice(Edge_list)
            k, l = random.choice(Edge_list)
    # Check if these 2 edges are not adjacent
            if (i == k or i== l) or (j == k or j==l):
                True
    # Do pairwise interchange
            else :
                adjacency_dict[k].remove(l)
                adjacency_dict[l].remove(k)
                adjacency_dict[k].append(i)
                adjacency_dict[l].append(j) 
                adjacency_dict[i].remove(j)
                adjacency_dict[j].remove(i)
                adjacency_dict[i].append(k)
                adjacency_dict[j].append(l) 
                Edge_list.append((k,i))
                Edge_list.remove((k,l))
                Edge_list.append((l,j))
                Edge_list.remove((i,j))
                number_of_interchanges += 1
    # Check if the new graph is connected
            visited = set()
            queue = [0]
            while queue:
                vertex = queue.pop(0)
                visited.add(vertex)
                for neighbour in adjacency_dict[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
            if len(visited) == number_of_vertices:
                break
            else :
                True
    # When the graph is connected, print the number of interchanges needed
    print(number_of_interchanges)

    end = time.time()
    print(end-start)
    # Print neighbors of each vertex
    for node in range(number_of_vertices):
        print(adjacency_dict[node])


example = open("z-7.txt", 'r')

apply_sequential_algorithm(example.read())

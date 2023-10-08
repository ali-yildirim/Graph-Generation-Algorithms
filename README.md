## Graph-Generation-Algorithms

This project was assigned by Tınaz Ekim Aşıcı as a semester project, for the course IE 456 Graph Theory and Its Applications. 

Down below are some definitions necessary to understand this project:
* A graph is a pair G = (V, E), where V is a set whose elements are called vertices, and E is a set of paired vertices, whose elements are called edges.
* The degree of a vertex is the number of neighboring vertices. 
* A degree sequence is a monotonic nonincreasing sequence of the vertex degrees of its graph vertices.
* Graph generation is creating graphs using predetermined degree sequences.
* Connectivity of a graph is the ability to start at a random vertex and travel all the other vertices without abruption.

In this project, we were given several graph generation algrithms. The task was to analyze the properties of these algorithms.

We analyzed our algorithms with respect to:

* The ability to generate a graph
* The time required to generated a graph
* The connectivity of the graph generated
* How many pairwise edge interactions necessary to make the generated graph connected if not already

The algorithms:

* Havel-Hakimi (Its 4 Variations)
* Sequential Algorithm

To check for connectivity, we deployed Depth First Search Algorithm.

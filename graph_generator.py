import sys
import random


class Graph(object):

    def __init__(self, num_of_nodes, p):
        self.num_of_nodes = num_of_nodes
        self.p = p

    def graph_generator(self):
        graph = {}
        nodes = []
        num_of_nodes = self.num_of_nodes

        # max_number_of_edges = (num_of_nodes ** 2 - num_of_nodes)/2
        for i in range(num_of_nodes):
            graph[i] = set([])

        for i in range(num_of_nodes):
            nodes.append(i)

            for node in range(num_of_nodes):
                for f_node in range(node + 1, num_of_nodes):
                    if f_node not in graph[node]:
                        p_node = random.random()
                        if p_node < self.p:
                            graph[node].add(f_node)
                            graph[f_node].add(node)
            return graph

        
def documentation():
    print '''
===== Graph Generator =====

python graph_generator.py <number of nodes> <probability 2 nodes be connected>

example:
python graph_generator.py 5 0.65
'''

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            num_of_nodes = int(sys.argv[1])
            conn_prob = float(sys.argv[2])
            ins = Graph(num_of_nodes, conn_prob)
            print Graph.graph_generator(ins)
        except ValueError:
            documentation()
    else:
        documentation()
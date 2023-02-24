from heapq import *

class Graph:

    graph_data : list
    edges : dict
    minty_path : list

    def __init__(self, path: str) -> None:
        self.graph_data = self.load_graph_data(path)
        self.edges = self.build_edges()
        self.minty_path = []

    
    def load_graph_data(self, path: str) -> list:
        new = open(path, "r")
        graph = []
        for i in new:
            next_node = i.replace("\n","").split(",")
            adj = []

            for j in next_node:
                if j == next_node[0]:
                    tmp = j.split()
                    adj.append((int(tmp[0]), int(tmp[1])))
                else:
                    tmp = j.replace(" ","",1).split()
                    adj.append((int(tmp[0]), int(tmp[1])))
            
            graph.append([adj])
        
        return graph

    
    def build_edges(self):
        edges = {}
        for n1, adjacents in enumerate(self.graph_data):
            for (_, n2) in adjacents[0]:
                eid = tuple(sorted((n1, n2))) 
                if eid not in edges:
                    edges[eid] = [(n1, n2)]
        
        return edges


    def find_minty_path(self):
        queue = [] # start a node, queue of one node
        heappush(queue, (0, 0))

        cost = {0: 0}
        # MINTY`S method loop
        while queue:
            _, n1 = heappop(queue)
            current = self.graph_data[n1]

            for next_node in current[0]:
                neigh_cost, n2 = next_node
                new_cost = cost[n1] + neigh_cost

                if n2 not in cost or new_cost < cost[n2]:  # undiscoverd

                    for t in self.minty_path:
                        if n1 not in t and n2 in t:
                            self.minty_path.remove(tuple(sorted((t[0],t[1]))))

                    heappush(queue, (new_cost, n2))
                    cost[n2] = new_cost
                    self.minty_path.append(tuple(sorted((n1,n2))))


    def get_minty_path(self):
        return self.minty_path

    
    def get_graph_data(self):
        return self.graph_data
    
    
    def get_edges(self):
        return self.edges
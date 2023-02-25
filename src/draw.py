import pygame
import random
from heapq import *
from graph import Graph

class Plot:

    screen : any
    clock : any
    display_size : tuple
    graph : Graph
    fps : int
    nodes_data : list
    edges_data : dict

    node_radius : int
    labels_color : tuple
    undiscovered_node_color : tuple
    discovered_node_outline : tuple
    current_node_fill : tuple
    discovered_node_fill : tuple
    undiscovered_node_fill : tuple
    completed_node_color : tuple
    undiscovered_edge_color : tuple


    def __init__(self, graph : Graph, screen : pygame.display, clock : pygame.time.Clock, fps : int, 
                coords: tuple = None,
                node_radius: int = 30,
                labels_color: tuple = (255, 255, 0),
                undiscovered_node_color: tuple = (100, 100, 100), 
                discovered_node_outline: tuple = (255, 255, 255),
                current_node_fill: tuple = (200, 200, 0),
                discovered_node_fill: tuple = (200,0,0),
                undiscovered_node_fill: tuple = (0, 0, 0),
                completed_node_color: tuple = (50,50,160),
                undiscovered_edge_color: tuple = (100, 100, 100),
                discovered_edge_color: tuple = (255, 255, 255)) -> None:
        
        self.clock = clock
        self.screen = screen
        self.display_size = screen.get_size()
        self.graph = graph
        self.fps = fps
        self.node_radius = node_radius
        self.nodes_data = self.add_coords(coords)
        self.edges_data = self.graph.get_edges()
        
        self.labels_color = labels_color
        self.undiscovered_node_color=undiscovered_node_color 
        self.discovered_node_outline=discovered_node_outline
        self.current_node_fill=current_node_fill
        self.discovered_node_fill=discovered_node_fill
        self.undiscovered_node_fill=undiscovered_node_fill
        self.completed_node_color=completed_node_color
        self.undiscovered_edge_color=undiscovered_edge_color
        self.discovered_edge_color=discovered_edge_color

        self.add_node_colors()
        self.add_edge_color()


    def add_coords(self, coords : dict):

        node_data = []

        if coords is None:
            nodes_count = len(self.graph.get_graph_data())
            while nodes_count:
                x = random.randint(self.node_radius,self.display_size[0]-self.node_radius)
                y = random.randint(self.node_radius,self.display_size[1]-self.node_radius)
                node_data.append([(x, y)])
                nodes_count -= 1
        else:
            tmp = sorted(coords.items())
            for _, coord in tmp:
                node_data.append([coord])
            
        return node_data
    

    def add_node_colors(self):
        for node in range(0, len(self.nodes_data)):
            self.nodes_data[node].extend([self.undiscovered_node_color, self.undiscovered_node_fill])

    
    def add_edge_color(self):
        for edge in self.edges_data.keys():
            self.edges_data[edge].append(self.undiscovered_edge_color)


    def circle_fill(self, xy : tuple, line_color : tuple, fill_color : tuple, radius : int, thickness : int, num):
        pygame.draw.circle(self.screen, line_color, xy, radius)
        pygame.draw.circle(self.screen, fill_color, xy, radius - thickness)
        self.screen.blit(num, num.get_rect(center = xy)) 

    
    def draw_graph(self):
        font = pygame.font.SysFont(None, 25)

        self.screen.fill((0, 0, 0,))

        for edge in self.edges_data.values(): # draw edges
            (n1, n2), color = edge
            pygame.draw.line(self.screen, color, self.nodes_data[n1][0], self.nodes_data[n2][0], 2)

            edge_cost = 0
            for edge in self.graph.get_graph_data()[n1][0]:
                if n2 in edge:
                    edge_cost = edge[0]
                
            cost = font.render(f"{edge_cost}", True, self.labels_color)
            self.screen.blit(cost, cost.get_rect(center = self.get_line_center(n1,n2)))

            for n, (xy, lcolor, fcolor) in enumerate(self.nodes_data): # draw nodes
                text = font.render(f"{n}", True, self.labels_color)
                self.circle_fill(xy, lcolor, fcolor, self.node_radius, 2, text)


    def get_line_center(self, n1 : int, n2 : int) -> float:
        x = (self.nodes_data[n1][0][0]+self.nodes_data[n2][0][0])/2
        y = (self.nodes_data[n1][0][1]+self.nodes_data[n2][0][1])/2
        return (x,y)

    
    def update(self):
        self.draw_graph()
        pygame.display.update()
        self.clock.tick(self.fps)

    
    def draw_minty_path(self):
        queue = []
        start = self.graph.get_start_node()
        heappush(queue, (0, start))

        cost = {start: 0}

        # MINTY`S method loop
        while queue:
            _, n1 = heappop(queue)
            current = self.nodes_data[n1]   
            current[1] = self.discovered_node_outline # current color for node
            current[2] = self.current_node_fill

            
            for next_node in self.graph.get_graph_data()[n1][0]:
                neigh_cost, n2 = next_node
                new_cost = cost[n1] + neigh_cost

                if n2 not in cost or new_cost < cost[n2]:  # undiscoverd

                    for visited_edge, _ in self.edges_data.items():
                        if n1 not in visited_edge and n2 in visited_edge:
                           self.edges_data[tuple(sorted((visited_edge[0],visited_edge[1])))][1] = self.undiscovered_node_color

                    heappush(queue, (new_cost, n2))
                    cost[n2] = new_cost
                    # discovered n2, color n2 and edge n1,n2
                    self.nodes_data[n2][1] = self.discovered_node_outline
                    self.nodes_data[n2][2] = self.discovered_node_fill
                    self.edges_data[tuple(sorted((n1,n2)))][1] = self.discovered_node_outline
                    self.update()
            
            # mark current as compete
            current[2] = self.completed_node_color
            self.update()
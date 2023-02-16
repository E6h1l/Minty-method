import pygame
import animation
from heapq import *
from graph_data import graph
from sys import exit

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
RADIUS = 30
FPS = 3

GREY = (100, 100, 100)  # undiscovered node or edge
WHITE = (255, 255, 255)  # discovered edge or node outline
YELLOW = (200, 200, 0)  # current node fill
RED = (200,0,0) # discovered node fill
BLACK = (0, 0, 0)  # undiscovered node fill
BLUE = (50,50,160) # completed node fill and completed edge


def run():
    # add start colors to graph
    for element in graph:
      element.extend([GREY, BLACK])

    edges = animation.build_edges(graph, GREY)
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    animation.draw_graph(graph, edges, screen) # initial
    animation.update(graph, edges, screen, clock, FPS)
    pygame.time.delay(2000) # wait 2 sec to start

    queue = [] # start a node, queue of one node
    heappush(queue, (0, 0))

    cost = {0: 0}

    while 1:
        
        for event in pygame.event.get():
            # MINTY`S method loop
            while queue:
                _, n1 = heappop(queue)
                current = graph[n1]   
                current[2] = WHITE  # current color for node
                current[3] = YELLOW

                for next_node in current[1]:
                    neigh_cost, n2 = next_node
                    new_cost = cost[n1] + neigh_cost

                    if n2 not in cost or new_cost < cost[n2]:  # undiscoverd

                        for t, _ in edges.items():
                            if n1 not in t and n2 in t:
                                edges[animation.edge_id(t[0],t[1])][1] = GREY

                        heappush(queue, (new_cost, n2))
                        cost[n2] = new_cost
                        # discovered n2, color n2 and edge n1,n2
                        graph[n2][2] = WHITE
                        graph[n2][3] = RED
                        edges[animation.edge_id(n1,n2)][1] = WHITE
                        animation.update(graph, edges, screen, clock, FPS)

                # mark current as compete
                current[3] = BLUE
                animation.update(graph, edges, screen, clock, FPS)

            if event.type == pygame.QUIT:
                exit()


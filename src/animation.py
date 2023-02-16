import pygame

# normalize id for either order
def edge_id(n1, n2): return tuple(sorted((n1, n2)))  


def build_edges(graph, color):
    edges = {} # edgeid: [(n1,n2), color]
    for n1, (_, adjacents, _, _) in enumerate(graph):
        for (_, n2) in adjacents:
            eid = edge_id(n1, n2)
            if eid not in edges:
                edges[eid] = [(n1, n2), color]
    
    return edges


def draw_graph(graph, edges, screen):
    count = 0
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"{count}", True, (255, 255, 0))

    screen.fill((0, 0, 0,))

    for e in edges.values(): # draw edges
        (n1, n2), color = e
        pygame.draw.line(screen, color, graph[n1][0], graph[n2][0], 2)

        w = 0

        for cost in graph[n1][1]:
            if n2 in cost:
                w = cost[0]
            
        cost = font.render(f"{w}", True, (255, 255, 0))
        screen.blit(cost, cost.get_rect(center = ((graph[n1][0][0]+graph[n2][0][0])/2,(graph[n1][0][1]+graph[n2][0][1])/2)))

    for xy, _, lcolor, fcolor in graph: # draw nodes
        circle_fill(xy, lcolor, fcolor, 25, 2, text, screen)
        count += 1
        text = font.render(f"{count}", True, (255, 255, 0))


def update(graph, edges, screen, clock, fps):
    draw_graph(graph, edges, screen)
    pygame.display.update()
    clock.tick(fps)


def circle_fill(xy, line_color, fill_color, radius, thickness, num, screen):
    pygame.draw.circle(screen, line_color, xy, radius)
    pygame.draw.circle(screen, fill_color, xy, radius - thickness)
    screen.blit(num, num.get_rect(center = xy))

def draw_text(text, font, color, xy, screen):
    img = font.render(text, True, color)
    screen.blit(img, xy)
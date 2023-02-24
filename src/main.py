import graph
import pygame
import draw
import env

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
PATH = env.get_graph_data_path()

description = """
  Find of optimal paths by the Minty method
  by Dmytro Prystaichuk
  """

nodes_coords = {0 : (70, 210),
       1 : (70, 350),
       2 : (140, 420),
       3 : (210, 70),
       4 : (210, 210),
       5 : (210, 490),
       6 : (280, 140),
       7 : (280, 280),
       8 : (350, 70),
       9 : (350, 350),
       10 : (350, 490),
       11 : (420, 140),
       12 : (420, 280),
       13 : (420, 420),
       14 : (490, 490),
       15 : (560, 420),
       16 : (630, 70),
       17 : (630, 210),
       18 : (700, 420)}

if __name__ == "__main__":
    try:    
        print(description)
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

        my_graph = graph.Graph(PATH)
        my_graph.find_minty_path()
        print(my_graph.get_minty_path())

        plot = draw.Plot(my_graph, screen, clock, fps=3, coords=nodes_coords)

        plot.draw_graph()
        plot.update()

        flag = True
        while True:
            for event in pygame.event.get():

                if flag:
                    plot.draw_minty_path()
                    plot.update()
                    flag = False
                
                if event.type == pygame.QUIT:
                    exit()

    except BaseException as ex:
        print(f"[ERROR]: something went totally wrong: {ex}")
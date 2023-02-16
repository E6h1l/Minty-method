# Minty's Algorithm

This is a Python implementation of Minty's algorithm for finding all shortest paths in a graph.

<image src="images/screen.png">


## Getting Started

To use this algorithm, you'll need Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

Also we need Python package **Pygame**.
You can see how to install Pygame in [official Pygame website](https://www.pygame.org/wiki/GettingStarted).

## Usage

To run the algorithm, simply execute the `main.py` file with the following command:
```
$ python main.py
```

The graph data should be stored in a `graph_data.py` file. For example:
```python
graph = [ 
# Node 0
[ (70, 210), # node`s (x,y) position on the screen
  [(2,1)] # (cost,adjacent nodes)
],
# Node 1
[ (70, 350), # Node 1
  [(2,0)]
]
]
```

This would represent a graph with two nodes (1 and 2) and one edge between them, with weight 2.

## License

This code is licensed under the MIT License. Feel free to use it for any purpose, commercial or non-commercial. If you use this code in your project, a link back to this repository would be appreciated but is not required.

## Author

### **[Dmytro Prystaichuk ( E6H1L )](https://github.com/E6h1l)**







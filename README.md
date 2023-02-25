# Minty's Algorithm

This is a Python implementation of Minty's algorithm for finding all shortest paths in a graph.

<image src="images/screen.png">


## Getting Started

To use this algorithm, you'll need Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

Also we need Python package **Pygame**.
You can see how to install Pygame in [official Pygame website](https://www.pygame.org/wiki/GettingStarted).

## Usage

The graph data should be stored in a `example.txt` file. For example:
```python
# Node 0
2 1, 3 2 # cost, adjacent nodes
# Node 1
2 0, 2 2
# Node 3
3 0, 2, 1
```
To run the algorithm 
you should set environment variable `GRAPH_DATA_PATH` :
```
$ export GRAPH_DATA_PATH='Path_to_graph_data'
```
After that execute the `main.py` file with the following command:
```
$ python main.py
```

This would represent a graph with three nodes (0, 1 and 2) and edges between them, with weights.

## License

This code is licensed under the MIT License. Feel free to use it for any purpose, commercial or non-commercial. If you use this code in your project, a link back to this repository would be appreciated but is not required.

## Author

### **[Dmytro Prystaichuk ( E6H1L )](https://github.com/E6h1l)**







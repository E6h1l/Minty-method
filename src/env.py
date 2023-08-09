import os

def get_graph_data_path():
    
    path = os.environ.get('GRAPH_DATA_PATH')
    
    if path is None:
        raise Exception('Path to Graph data is not provided')

    return path
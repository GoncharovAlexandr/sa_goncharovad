import networkx as nx
import pandas as pd
import csv
from io import StringIO

def main(file_path: str) -> str:
    edges = pd.read_csv(file_path, header=None)

    G = nx.DiGraph()
    for _, row in edges.iterrows():
        G.add_edge(row[0], row[1])

    nodes = list(G.nodes)

    result = {node: [0] * 5 for node in nodes}

    for node in nodes:
        result[node][0] = len(list(G.successors(node)))

        result[node][1] = len(list(G.predecessors(node)))

        result[node][2] = len(nx.descendants(G, node)) - result[node][0]

        result[node][3] = len(nx.ancestors(G, node)) - result[node][1]

        if result[node][1] > 0:
            parent = list(G.predecessors(node))[0]
            siblings = list(G.successors(parent))
            result[node][4] = len(siblings) - 1

    output = StringIO()
    writer = csv.writer(output)
    for node in nodes:
        writer.writerow([node] + result[node])

    return output.getvalue()

file_path = 'task2.csv'
output_csv = main(file_path)
print(output_csv)

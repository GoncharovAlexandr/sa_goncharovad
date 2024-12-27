import json
import numpy as np


def load_clusters(file_path):

    with open(file_path, 'r') as f:
        data = json.load(f)

    cluster_groups = []
    for group in data:
        if isinstance(group, list):
            cluster_groups.append(group)
        else:
            cluster_groups.append([group])

    total_elements = sum(len(group) for group in cluster_groups)
    matrix = np.ones((total_elements, total_elements), dtype=int)

    previous_elements = []
    for group in cluster_groups:
        for prior in previous_elements:
            for current in group:
                matrix[current - 1, prior - 1] = 0
        previous_elements.extend(group)

    return matrix


def extract_conflict_pairs(matrix):
    conflicting_pairs = []

    size = len(matrix)
    for row in range(size):
        for col in range(row + 1, size):
            if matrix[row, col] == 0 and matrix[col, row] == 0:
                pair = sorted([row + 1, col + 1])
                if pair not in conflicting_pairs:
                    conflicting_pairs.append(pair)

    return [pair[0] if len(pair) == 1 else pair for pair in conflicting_pairs]


def main(file_path1, file_path2):
    matrix1 = load_clusters(file_path1)
    matrix2 = load_clusters(file_path2)

    intersect_matrix = np.multiply(matrix1, matrix2)
    transposed_intersect = np.multiply(matrix1.T, matrix2.T)
    combined_matrix = np.maximum(intersect_matrix, transposed_intersect)

    conflicting_clusters = extract_conflict_pairs(combined_matrix)
    return conflicting_clusters


if __name__ == '__main__':
    result = main("example1.json", "example2.json")
    print(result)

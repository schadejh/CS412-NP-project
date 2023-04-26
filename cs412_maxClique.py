import itertools

def is_clique(graph, subset):
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            if subset[j] not in graph[subset[i]]:
                return False
    return True

def max_clique_bruteforce(graph):
    nodes = list(graph.keys())
    max_clique_size = 0
    max_clique = set()

    for subset_size in range(1, len(nodes) + 1):
        for subset in itertools.combinations(nodes, subset_size):
            if is_clique(graph, subset):
                if subset_size > max_clique_size:
                    max_clique_size = subset_size
                    max_clique = set(subset)
    return max_clique

#Test
graph = []
for i in input():
    graph[i]= input().split


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C'],
    'E': ['F'],
    'F': ['E'],
}

print(max_clique_bruteforce(graph))  # Should output: {'A', 'B', 'C', 'D'}
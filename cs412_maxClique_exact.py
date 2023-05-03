def find_cliques(graph):
    def expand(clique, candidates):
        for node in candidates:
            if all(node in graph[nbr] for nbr in clique):
                yield clique + [node]

    def search(cliques, candidates):
        if not candidates:
            return cliques
        for clique in expand(cliques[-1], candidates):
            cliques = search(cliques + [clique], [n for n in candidates if n in graph[clique[-1]]])
        return cliques

    return search([[]], list(graph.keys()))

def max_clique(graph):
    cliques = find_cliques(graph)
    return max(cliques, key=len)

if __name__ == '__main__':
    m = int(input().strip())
    edges = [tuple(input().strip().split()) for _ in range(m)]
    vertices = set(v for edge in edges for v in edge)
    graph = {v: set() for v in vertices}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    maxclique = max_clique(graph)
    print(maxclique)
    

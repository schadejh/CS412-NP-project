"""
    name: James Schader
    Approximation for Max Independent Set (MIS)
    MIS is complementary to Max Clique

    This program will find the Minimum Independent Set of
    the given graph. The given graph should be the complementary graph
    of the main graph in which a maximal clique is being sought.
"""

def getMIS(graph):
    nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]))
    # nodes are sorted by degree (ascending), so that v is selected
    # as a node with min degree in G

    mis = set()  # S <- ø
    rottenSet = set()  # this set is to mark rotten nodes, i.e. nodes
                       # that are known to have neighbors and won't work
                       # in this MIS
    for i in range(len(nodes)):  # while G is not empty do
        v = nodes[i]  # let v be a node of min degree in G
        if v not in rottenSet:
            mis.add(v)  # S <- S u {v}
            rottenSet.add(v)  # remove v...
        for n in list(graph[v]):
            rottenSet.add(n)  # and its neighbors from G
                              # here done by marking it as rotten
    # end 'while'
    return mis  # Output S


def main():

    graph = {}
    nodes = int(input())
    for _ in range(nodes):
        line = input()
        print('parsing:' + line)
        spline = line.split()
        
        graph[spline[0]] = spline[1:]

    # graph = {
    #     'A': ['B', 'C', 'D'],
    #     'B': ['A', 'C', 'D'],
    #     'C': ['A', 'B'],
    #     'D': ['A', 'B'],
    #     'E': ['F'],
    #     'F': ['E'],
    # }

    print(getMIS(graph))


if __name__ == "__main__":
    main()

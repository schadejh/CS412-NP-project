"""
    name: James Schader
    Approximation for Max Independent Set (MIS)
    MIS is complementary to Max Clique
"""


import itertools


def getMIS(g):
    s = set()
    removedSet = set()
    while len(g) > 0:  # while G is not empty do
        v = g.pop()  # TODO: let v be a node of minimum degree in G
        s.add(v)  # S <- S union {v}
        if v in g and v not in removedSet:
           removedSet.add(v)  # remove v...
        for n in list(v.getNeighbors()):  # and its neighbors from G
            if n not in removedSet:
                removedSet.add(n)

    print('final:')
    for v in s:
        print(v.getName())


def retry(graph):
    nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]))
    # nodes are sorted by degree (ascending)

    mis = set()
    rottenSet = set()
    for i in range(len(nodes)):
        v = nodes[i]
        if v not in rottenSet:
            mis.add(v)
            rottenSet.add(v)  # remove v and its neighbors...
        for n in list(graph[v]):
            rottenSet.add(n)
    
    return mis


    # max_clique_size = 0
    # max_clique = set()

    # for subset_size in range(1, len(nodes) + 1):
    #     for subset in itertools.combinations(nodes, subset_size):
    #         if subset_size > max_clique_size:
    #             max_clique_size = subset_size
    #             max_clique = set(subset)
    # return max_clique


def main():

    class node():
        def __init__(self, name, d, n):
            self.name = name
            self.degree = d
            self.neighbors = n
        
        def getName(self):
            return self.name

        def getDegree(self):
            return self.degree
        
        def getNeighbors(self):
            return self.neighbors
        
        def setNeighbors(self, newNeighbors):
            self.neighbors = newNeighbors

    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B'],
        'D': ['A', 'B'],
        'E': ['F'],
        'F': ['E'],
    }

    nA = node('', 3, [])
    nB = node('', 3, [])
    nC = node('', 3, [])
    nD = node('', 3, [])
    nE = node('', 3, [])
    nF = node('', 2, [])

    nA.setNeighbors([nE, nF])
    nB.setNeighbors([nE, nF])
    nC.setNeighbors([nE, nF])
    nD.setNeighbors([nE, nF])
    nE.setNeighbors([nA, nB, nC, nD])
    nF.setNeighbors([nA, nB, nC, nD])
    g = {nA, nB, nC, nD, nE, nF}

    # nC = node('c',1,[])
    # nA = node('a',1,[nC])
    # nB = node('b',0,[])
    # nC.setNeighbors([nA])
    # g = {nA,nB,nC}  # list of nodes, sorted ascending by degree

    # getMIS(g)

    print(retry(graph))


if __name__ == "__main__":
    main()

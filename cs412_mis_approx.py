"""
    name: James Schader
    Approximation for Max Independent Set (MIS)
    MIS is complementary to Max Clique
"""


def getMIS(g):
    s = set()

    while len(g) > 0:
        v = g.pop()
        s.add(v)
        if v in g:
            g.remove(v)
        for n in g[v]:
            if n in g:
                g.remove(n)

    print('final:')
    for v in s:
        print(v.getName())


def main():

    class node():
        def __init__(self, name, d, n):
            self.name = name
            self.degree = d
            self.neighbors = n

        def getNeighbors(self):
            return self.neighbors
        
        def getDegree(self):
            return self.degree
        
        def setNeighbors(self, newNeighbors):
            self.neighbors = newNeighbors
        
        def getName(self):
            return self.name

    # graph = {
    #     'A': ['B', 'C', 'D'],
    #     'B': ['A', 'C', 'D'],
    #     'C': ['A', 'B', 'D'],
    #     'D': ['A', 'B', 'C'],
    #     'E': ['F'],
    #     'F': ['E'],
    # }

    nC = node('c',1,[])
    nA = node('a',1,[nC])
    nB = node('b',0,[])
    nC.setNeighbors([nA])
    g = {nA,nB,nC}  # list of nodes, sorted ascending by degree

    getMIS(g)


if __name__ == "__main__":
    main()

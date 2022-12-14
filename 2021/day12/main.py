from collections import defaultdict


def get_input(filename):
    output = defaultdict()
    with open(filename) as filehandle:
        for line in filehandle:
            line = line.split("-")
            output[line[0]] = line[1].strip()

    return output


class GraphClass:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if (
            vertex1 in self.adjacencyList.keys()
            and vertex2 in self.adjacencyList.keys()
        ):
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
        else:
            print("bad vertex")

    def removeEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1].remove(vertex2)
        self.adjacencyList[vertex2].remove(vertex1)

    def removeVertex(self, vertex):
        for vert in self.adjacencyList[vertex]:
            self.removeEdge(vert, vertex)
            del self.adjacencyList[vertex]


def main():
    output = get_input("input/input.txt")
    Cave = GraphClass()
    for key, val in output.items():
        Cave.addVertex(key)
        Cave.addVertex(val)
        Cave.addEdge(key, val)
    print(Cave.adjacencyList)


if __name__ == "__main__":
    main()

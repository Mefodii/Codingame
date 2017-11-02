import sys
import math


def resetVisited(nodes):
    for node in nodes:
        node.visited = False


class Node:
    def __init__(self, V1):
        self.nodesConnected = []
        self.value = V1
        self.visited = False
        self.disable = False

    def __str__(self):
        return str(self.value)

    def propagate(self, limit):
        c = []
        bestNode = None
        self.visited = True
        longest = -1
        for node in self.nodesConnected:
            path = node.checkPropagate(limit) + 1
            if path > longest:
                longest = path
                bestNode = node
            else:
                node.disable = True

        if longest == -1:
            longest = 0
        c.append(bestNode)
        c.append(longest)
        return c

    def checkPropagate(self, limit):
        self.visited = True
        longest = -1
        for node in self.nodesConnected:
            if longest >= limit:
                return longest

            if not node.visited:
                longest = max(node.checkPropagate(limit) + 1, longest)

        if longest == -1:
            longest = 0

        return longest

    def printConnections(self):
        s = ""
        for c in self.nodesConnected:
            s += str(self) + " " + str(c) + "\n"
        return s

    def makeConnection(self, node):
        self.nodesConnected.append(node)
        node.nodesConnected.append(self)


n = int(input())
nodes = []
for i in range(n):
    a, b = [int(j) for j in input().split()]
    print(a, b, file=sys.stderr)
    addedA = False
    addedB = False
    nodeA = None
    nodeB = None
    for node in nodes:
        if node.value == a:
            addedA = True
            nodeA = node
        if node.value == b:
            addedB = True
            nodeB = node

    if not addedA:
        nodeA = Node(a)
        nodes.append(nodeA)
    if not addedB:
        nodeB = Node(b)
        nodes.append(nodeB)

    nodeA.makeConnection(nodeB)

print("", file=sys.stderr)


minimal = 999999

node = nodes[0]
go = True
while go:
    if not node.disable:
        results = node.propagate(minimal)
        node.disable = True
        if results[0] is None:
            go = False
        else:
            if results[1] < minimal:
                minimal = results[1]
                node = results[0]
                resetVisited(nodes)
            else:
                go = False
    else:
        go = False


print(minimal)
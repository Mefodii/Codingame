import sys
import math


class Tree:
    def __init__(self, values, level):
        self.value = values[0]
        self.children = []
        self.leaf = False
        self.level = level
        if (len(values) > 1):
            self.leaf = True
            self.children.append(Tree(values[1:], self.level + 1))

    def appendChildren(self, values):
        if self.leaf:
            added = False
            for child in self.children:
                if values[0] == child.value:
                    if (len(values) > 1):
                        child.appendChildren(values[1:])
                    added = True

            if not added:
                self.children.append(Tree(values, self.level + 1))
        else:
            self.leaf = True
            self.children.append(Tree(values, self.level + 1))

    def printTree(self):
        s = str(self.value)
        for child in self.children:
            s += child.printTree()
        if not self.leaf:
            s += "\n"

        return s

    def __len__(self):
        l = 1
        for child in self.children:
            l += len(child)
        return l


n = int(input())
trees = []
for i in range(n):
    telephone = input()
    added = False;

    for tree in trees:
        if telephone[0] == tree.value:
            tree.appendChildren(telephone[1:])
            added = True

    if not added:
        trees.append(Tree(telephone, 0))



print(sum(len(tree) for tree in trees))


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

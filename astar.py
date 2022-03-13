class Node():
    def __init__(self, parent=None, id=None):
        self.parent = parent
        self.id = id
        
        self.g = 0
        self.h = 0
        self.f = 0


def astar(start, end):
    startNode = Node(None, start)
    endNode = Node(None, end)

    open = []
    closed = []

    open.append(startNode)

    while len(open) > 0:
        currentNode = open[0]
        currentIndex = 0

        for index, item in enumerate(open):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index
        
        open.pop(currentIndex)
        closed.append(currentIndex)

        if currentNode.id == endNode.id:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.id)
                current = current.parent
            return path[::-1]
        
        children = []
        childPositions = [(currentNode.id - 1), (currentNode.id + 100), (currentNode.id + 1), (currentNode.id - 100)]

        for i in childPositions:
            newNode = Node(currentNode, i)
            children.append(newNode)

        for child in children:
            for closedChild in closed:
                continue

            child.g = currentNode.g + 1
            child.h = abs(child.id - endNode.id)
            child.f = child.g + child.h

            for openNode in open:
                if child == openNode and child.g > openNode.g:
                    continue
            open.append(child)

def main():
    path = astar(302,808)
    print(path)
if "__main__" == __name__:
    main()
class Node(object):
    left = None
    right = None
    item = None
    weight = 0

    def __init__(self, item, weight):
        self.item = item
        self.weight = weight

    def setChildren(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "%s - %s -- %s - %s" % (self.item, self.weight, self.left, self.right)

    def __lt__(self, other):
        return self.weight < other.weight
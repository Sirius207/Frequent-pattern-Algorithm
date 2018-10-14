class FPTree:
    def __init__(self):
        self.counts = 1
        self.children = None

    def insert_node(self, item):
        if self.children == None:
            self.children = {}
            self.children[item] = FPTree()
        elif item not in self.children:
            self.children[item] = FPTree()
        else:
            self.children[item].counts += 1

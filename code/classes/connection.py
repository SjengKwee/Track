class Connection(set):

    def __hash__(self):
        items = tuple(self)
        if hash(items[0]) > hash(items[1]):
            items = (items[1], items[0])
        return hash(items)

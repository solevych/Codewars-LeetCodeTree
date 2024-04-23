class NodeForQueue:
    def __init__(self, data, next = None):
        self.data=data
        self.next = next
        
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = NodeForQueue(item)
            self.head = self.tail
        else:
            self.tail.next =NodeForQueue(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head.data
            self.head = self.head.next
            return item
        return None


def tree_by_levels(node):
    res = []
    next = Queue()
    root = node
    
    if root is not None:
        res.append(root.value)
        
    while root:
        
        if root.left:
            res.append(root.left.value)
            next.add(root.left)
            if root.right:
                res.append(root.right.value)
                next.add(root.right)
        
        elif root.right:
            res.append(root.right.value)
            next.add(root.right)
        
        
        if next.is_empty():
            return res
        root = next.pop()
        
    return res
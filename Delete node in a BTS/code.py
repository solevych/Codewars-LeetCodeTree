# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

class Solution:
    @staticmethod
    def change_node(root):
        if root.left:
            if not root.left.left and not root.left.right:
                if not root.left.left:
                    root.left.left = root.right
                else:
                    root.left.right = root.right
                        
                    root = root.left
                    
        elif root.right:
            if not root.right.left and not root.right.right:
                if not root.right.left:
                    root.right.left = root.left
                else:
                    root.right.right = root.left

                root = root.right

    def deleteNode(self, root, key: int):
        if not root:
            return
        res=[]
        res.append(root.val)
        next = Queue()
        

        tree = root
        prev = TreeNode()
        while tree:
            if root.val == key:
                root = self.change_node(root)

                        
            if root.left:
                res.append(root.left.val)
                if root.left == key:
                    new_root = self.change_node(root.left)
                    root.left = new_root
                next.add(root.left)
                if root.right:
                    res.append(root.right.val)
                    next.add(root.right)
            
            elif root.right:
                res.append(root.right.val)
                if root.right == key:
                    new_root = self.change_node(root.right)
                    root.right = new_root
                next.add(root.right)
            
            if next.is_empty():
                break
            prev = root
            root = next.pop()


        tree_root = TreeNode(res.pop(0))
        tree = tree_root
        while res:
            tree.left = TreeNode(res.pop(0))
            next.add(tree.left)
            if res:
                tree.right = TreeNode(res.pop(0))
                next.add(tree.right)
            if not next.is_empty():
                tree = next.pop()
            else:
                break
        return tree_root
            

            
            

            
 
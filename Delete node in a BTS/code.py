# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class NodeForQueue:
#     def __init__(self, data, next = None):
#         self.data=data
#         self.next = next
        
# class Queue:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def is_empty(self):
#         return self.head is None

#     def add(self, item):
#         if self.head is None:
#             self.tail = NodeForQueue(item)
#             self.head = self.tail
#         else:
#             self.tail.next =NodeForQueue(item)
#             self.tail = self.tail.next

#     def pop(self):
#         if self.head:
#             item = self.head.data
#             self.head = self.head.next
#             return item
#         return None

class Solution:
    # @staticmethod
    # def change_node(root):
    #     if root.left:
    #         if not root.left.left and not root.left.right:
    #             if not root.left.left:
    #                 root.left.left = root.right
    #             else:
    #                 root.left.right = root.right
                        
    #                 root = root.left
                    
    #     elif root.right:
    #         if not root.right.left and not root.right.right:
    #             if not root.right.left:
    #                 root.right.left = root.left
    #             else:
    #                 root.right.right = root.left

    #             root = root.right

    def deleteNode(self, root, key: int):
        if not root:
            return
        if root.val ==  key:
            right = root.right
            if right:
                while right.left:
                    right = right.left
                right.left = root.left
                return root.right
            return root.left
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
            
 
def pre_order(node):
    res = []
    if node is None:
        return res
    res.append(node.data)
    return res + pre_order(node.left) + pre_order(node.right)


def in_order(node):
    res = []
    if node is None:
        return res
    res.append(node.data)
    return in_order(node.left) + res + in_order(node.right)
    


def post_order(node):
    res = []
    if node is None:
        return res
    res.append(node.data)
    return post_order(node.left)+ post_order(node.right) + res 

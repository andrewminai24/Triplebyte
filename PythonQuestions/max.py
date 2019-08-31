def max(node):
    if not node:
        return 0
    left = max_height(node.left)
    right = max_height(node.right)
    return max(left,right)

    print("node ",max)

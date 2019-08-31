def func(tree):
    nodes = [tree]
    for node in nodes:
        yield node
        nodes += node.childeren
    print(tree)

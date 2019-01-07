def lca(root, v1, v2):
    if (root.info >= v1 and root.info <= v2) \
       or (root.info >= v2 and root.info <= v1):
        return root
    elif root.right is None or root.info >= v1 and root.info >= v2:
        return lca(root.left, v1, v2)
    else:
        return lca(root.right, v1, v2)

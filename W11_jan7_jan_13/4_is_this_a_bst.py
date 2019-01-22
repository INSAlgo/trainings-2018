def check_bst_bounds(node, lower, upper):
    return ((node is None)
            or not (lower is not None and node.data <= lower
                    or upper is not None and node.data >= upper)
            and check_bst_bounds(node.left, lower, node.data)
            and check_bst_bounds(node.right, node.data, upper))

def check_binary_search_tree_(root):
    return check_bst_bounds(root, None, None)
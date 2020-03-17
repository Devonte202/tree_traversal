class binary_tree_node:
   def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def insert_left(tree_node, value):
    current_left = tree_node.left_child
    tree_node.left_child = binary_tree_node(value)
    tree_node.left_child.left_child = current_left
    return tree_node.left_child.value

def insert_right(tree_node, value):
    current_right = tree_node.right_child
    tree_node.right_child = binary_tree_node(value)
    tree_node.right_child.right_child = current_right
    return tree_node.right_child.value

def preorder(tree_node):
    if tree_node == None:
        return None
        
    print(tree_node.value)
    preorder(tree_node.right_child)
    preorder(tree_node.left_child)

def is_unival_tree(tree_node):
    node_set = set()
    def node_collector(tree_node):
        if tree_node == None:
            return None
            
        node_set.add(tree_node.value)
        node_collector(tree_node.right_child)
        node_collector(tree_node.left_child)
 
    node_collector(tree_node)
    
    if len(node_set) > 1:
        return False
    return True

def postorder(tree_node):
    if tree_node == None:
        return None
        
    postorder(tree_node.right_child)
    postorder(tree_node.left_child)
    print(tree_node.value)

def inorder(tree_node):
    if tree_node == None:
        return None
        
    inorder(tree_node.right_child)
    print(tree_node.value)
    inorder(tree_node.left_child)

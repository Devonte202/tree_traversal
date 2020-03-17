from exercises import binary_tree_node, insert_left, insert_right, is_unival_tree

def test_binary_tree_node():
    t = binary_tree_node('A')
    assert t.value == 'A'
    assert t.left_child == None
    assert t.right_child == None

def test_insert_left():
    t = binary_tree_node('A')
    insert_left(t,'B')
    t.left_child.value == 'B' 
    insert_left(t,'Z')
    t.left_child.value == 'Z' 
    t.left_child.left_child.value == 'B' 
    
    
def test_insert_right():
    t = binary_tree_node('A')
    insert_right(t,'C')
    t.right_child.value == 'C'
    insert_right(t,'Y')
    t.right_child.value == 'Y'
    t.right_child.right_child.value == 'C'

def test_is_unival_tree():
    treeOne = binary_tree_node('A')
    insert_left(treeOne,'B')
    insert_left(treeOne,'Z')
    insert_right(treeOne,'C')
    insert_right(treeOne,'Y')
    is_unival_tree(treeOne) == False
    treeTwo = binary_tree_node('A')
    insert_left(treeTwo,'A')
    insert_left(treeTwo,'A')
    insert_right(treeTwo,'A')
    insert_right(treeTwo,'A')
    is_unival_tree(treeTwo) == True
from node import Node


def test_no_children():
    parent_id = "100"
    node_id = "200"
    node_name = "example"
    node = Node(parent_id, node_id, node_name)

    assert int(parent_id) == node.parent_id
    assert int(node_id) == node.node_id
    assert node_name == node.node_name


def test_one_child():
    parent_id = "0"
    node_id = "100"
    node_name = "example parent"
    parent_node = Node(parent_id, node_id, node_name)
    parent_id = "100"
    node_id = "200"
    node_name = "example child"
    child_node = Node(parent_id, node_id, node_name)
    parent_node.add_child_node(child_node)

    children = parent_node.children

    assert 1 == len(children)
    assert int(parent_id) == children[0].parent_id
    assert int(node_id) == children[0].node_id
    assert node_name == children[0].node_name


def test_multiple_children():
    parent_id = "0"
    node_id = "100"
    node_name = "example parent"
    parent_node = Node(parent_id, node_id, node_name)

    for i in range(3):
        parent_id = "100"
        node_id = str(i)
        node_name = f"example child #{i+1}"
        child_node = Node(parent_id, node_id, node_name)
        parent_node.add_child_node(child_node)

    children = parent_node.children

    assert 3 == len(children)
    assert int(parent_id) == children[0].parent_id
    assert 0 == children[0].node_id
    assert "example child #1" == children[0].node_name

    assert int(parent_id) == children[1].parent_id
    assert 1 == children[1].node_id
    assert "example child #2" == children[1].node_name

    assert int(parent_id) == children[2].parent_id
    assert 2 == children[2].node_id
    assert "example child #3" == children[2].node_name


def test_null_parent_id():
    parent_id = "null"
    node_id = "200"
    node_name = "example"
    node = Node(parent_id, node_id, node_name)

    assert node.parent_id is None
    assert int(node_id) == node.node_id
    assert node_name == node.node_name

from node import Node


def test_no_children():
    parent_id = 100
    node_id = 200
    node_name = "example"
    node = Node(parent_id, node_id, node_name)

    assert node.parent_id == parent_id
    assert node.node_id == node_id
    assert node.node_name == node_name


def test_one_child():
    parent_id = 0
    node_id = 100
    node_name = "example parent"
    parent_node = Node(parent_id, node_id, node_name)
    parent_id = 100
    node_id = 200
    node_name = "example child"
    child_node = Node(parent_id, node_id, node_name)
    parent_node.add_child_node(child_node)

    children = parent_node.children

    assert len(children) == 1
    assert children[0].parent_id == parent_id
    assert children[0].node_id == node_id
    assert children[0].node_name == node_name


def test_multiple_children():
    parent_id = 0
    node_id = 100
    node_name = "example parent"
    parent_node = Node(parent_id, node_id, node_name)

    for i in range(3):
        parent_id = 100
        node_id = i
        node_name = f"example child #{i+1}"
        child_node = Node(parent_id, node_id, node_name)
        parent_node.add_child_node(child_node)

    children = parent_node.children

    assert len(children) == 3
    assert children[0].parent_id == parent_id
    assert children[0].node_id == 0
    assert children[0].node_name == "example child #1"

    assert children[1].parent_id == parent_id
    assert children[1].node_id == 1
    assert children[1].node_name == "example child #2"

    assert children[2].parent_id == parent_id
    assert children[2].node_id == 2
    assert children[2].node_name == "example child #3"

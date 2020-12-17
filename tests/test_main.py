from main import parse_input_string_into_node_elements, parse_node_element


def test_parse_input_string_into_node_elements():
    node0 = "null,1,parent"
    node1 = "1,1,child"
    input_string = f"{node0}|{node1}"

    node_elements = parse_input_string_into_node_elements(input_string)

    assert len(node_elements) == 2
    assert node_elements[0] == node0
    assert node_elements[1] == node1


def test_parse_input_string_into_node_elements_space_around_delimiter():
    node0 = "null,1,parent"
    node1 = "1,1,child"
    input_string = f"  {node0}  |\t{node1}  "

    node_elements = parse_input_string_into_node_elements(input_string)

    assert len(node_elements) == 2
    assert node_elements[0] == node0
    assert node_elements[1] == node1


def test_parse_node_element():
    parent_id = 0
    node_id = 1
    node_name = "node name"
    node_element = f"{parent_id},{node_id},{node_name}"

    node = parse_node_element(node_element)

    assert node.parent_id == parent_id
    assert node.node_id == node_id
    assert node.node_name == node_name


def test_parse_node_element_spaces_around_delimiter():
    parent_id = 0
    node_id = 1
    node_name = "node name"
    node_element = f"\t{parent_id} , {node_id}\t,   {node_name}   "

    node = parse_node_element(node_element)

    assert node.parent_id == parent_id
    assert node.node_id == node_id
    assert node.node_name == node_name

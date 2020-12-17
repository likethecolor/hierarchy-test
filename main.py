import re
import sys
from node import Node


def parse_input_str(input_str: str) -> list:
    """
    Parse the original string.  This is the function the `README.md` mentions.

    :param input_str: original input string
    :return: list of values used to build nodes
    """
    nodes = []
    node_elements = parse_input_string_into_node_elements(input_str)
    for node_element in node_elements:
        nodes.append(parse_node_element(node_element))
    add_child_nodes(nodes)
    return nodes


def parse_input_string_into_node_elements(input_str: str) -> list:
    """
    Parse the original input string into strings suitable for further parsing.

    :param input_str: original input string
    :return: list of node elements
    """
    node_elements = input_str.split('|')
    for i in range(len(node_elements)):
        node_elements[i] = node_elements[i].strip()

    return node_elements


def parse_node_element(node_str: str) -> Node:
    """
    Parse the node values found in each element of the original input.

    :param node_str: string containing values used to build a `Node`
    :return: list of `Node` values
    """
    if node_str is None or len(node_str.strip()) == 0:
        raise Exception(f"node string is empty")

    elements = re.split(r'\s*?,\s*', node_str)
    if len(elements) != 3:
        raise Exception(f"node string invalid format: '{node_str}'")

    if elements[0] == 'null':
        elements[0] = "-1"
    return Node(int(elements[0].strip()), int(elements[1].strip()), elements[2].strip())


def add_child_nodes(all_nodes: list):
    """
    Add to each `Node` its children.

    :param all_nodes: list containing all nodes
    """
    number_of_nodes = len(all_nodes)
    for i in range(number_of_nodes):
        current_node = all_nodes[i]
        for j in range(1, number_of_nodes):
            if all_nodes[j].parent_id == current_node.node_id:
                current_node.add_child_node(all_nodes[j])


def print_children(parent_node, children, level=0):
    """
    Print the node and its children.  Note, this is a recursive function.

    :param parent_node: a parent node
    :param children: the parent node's children
    :param level: level of recursion (used for printing leading spaces)
    """
    spaces = ' - ' * level
    print(f"{spaces}{parent_node}")
    for child in children:
        print_children(child, child.children, level + 1)


def main(input_str: str):
    nodes = parse_input_str(input_str)

    if nodes:
        print_children(nodes[0], nodes[0].children)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("input string is missing (e.g., python main.py input-string")

    main(sys.argv[1])

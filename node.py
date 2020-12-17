class Node:
    def __init__(self, parent_id: str, node_id: str, node_name: str):
        self._parent_id = Node._parse_id(parent_id)
        self._node_id = Node._parse_id(node_id)
        self._node_name = node_name
        self._children = []

    @property
    def parent_id(self):
        return self._parent_id

    @property
    def node_id(self):
        return self._node_id

    @property
    def node_name(self):
        return self._node_name

    @property
    def children(self):
        return self._children

    def add_child_node(self, a_node):
        self._children.append(a_node)

    @staticmethod
    def _parse_id(id_str):
        if id_str == 'null':
            id_str = None
        else:
            id_str = int(id_str)
        return id_str

    def __str__(self):
        return f'Node({self._parent_id},{self._node_id},{self._node_name}) [children:{len(self._children)}]'

    def __repr__(self):
        return f'Node({self._parent_id},{self._node_id},{self._node_name}) [children:{len(self._children)}]'

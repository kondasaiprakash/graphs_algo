# performs dfs on the adjacency list

class DepthFirstSearch:
    def __init__(self, adjacency_list, strat_node=None) -> None:
        self.adjacency_list = adjacency_list
        self.start_node = strat_node
        self.visited = []
        self.connected_nodes = {}
        if not self.start_node:
            if len(adjacency_list.keys()) > 0:
                self.start_node = adjacency_list.keys()[0]
            else:
                raise ValueError("adjacent list is empty")

    def initialize(self, adjacency_list=None):
        if adjacency_list:
            self.adjacency_list = adjacency_list
        self.visited = []

    def run_dfs(self, node, connect_node_id=-1):
        if node in self.visited:
            return
        print(f"node reached : {node}")
        self.visited.append(node)
        if connect_node_id > 0:
            if connect_node_id not in self.connected_nodes.keys():
                self.connected_nodes[connect_node_id] = [node]
            else:
                self.connected_nodes[connect_node_id].append(node)
        for neighbour in self.adjacency_list[node]:
            self.run_dfs(neighbour, connect_node_id=connect_node_id)

    def connected_components(self):
        self.initialize()
        connected_nodes = {}
        connected_nodes_visited = []
        connected_components_count = 0
        for node in self.adjacency_list.keys():
            if node not in self.visited:
                connected_components_count = connected_components_count + 1
                self.run_dfs(node, connect_node_id=connected_components_count)
                connected_nodes[connected_components_count] = []
                for visited_node in self.visited:
                    if visited_node not in connected_nodes_visited:
                        connected_nodes[connected_components_count].append(
                            visited_node)
                        connected_nodes_visited.append(visited_node)
        return connected_nodes

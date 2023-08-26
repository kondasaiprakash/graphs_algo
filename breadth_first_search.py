class BreadthFirstSearch:
    def __init__(self, adjacency_list, start=None, end=None) -> None:
        self.adjacency_list = adjacency_list
        self.start = start
        self.end = end
        self.visited = []
        self.prev_node = {}

    def initialize(self, adjacency_list=None, start=None, end=None):
        if adjacency_list:
            self.adjacency_list = adjacency_list
        if start:
            self.start = start
        if end:
            self.end = end
        self.visited = []
        self.prev_node = {}

    def run_bfs(self, start=None):
        self.initialize()
        bfs_queue = []
        if not start:
            start = self.start
        bfs_queue.append(start)
        self.visited.append(start)
        self.prev_node[start] = None
        while len(bfs_queue):
            node = bfs_queue.pop(0)
            for neigbhour in self.adjacency_list[node]:
                if neigbhour not in self.visited:
                    bfs_queue.append(neigbhour)
                    self.visited.append(neigbhour)
                    self.prev_node[neigbhour] = node

    def constructPathforNode(self, node):
        path = []
        path.append(node)
        while self.prev_node[node]:
            path.append(self.prev_node[node])
            node = self.prev_node[node]
        return path

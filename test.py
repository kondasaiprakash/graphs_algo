import depth_first_search
import breadth_first_search

adjacency_list = {}
adjacency_list['1'] = ['2', '4']
adjacency_list['2'] = ['3', '8']
adjacency_list['3'] = ['1']
adjacency_list['4'] = ['5', '6', '7', '8']
adjacency_list['5'] = []
adjacency_list['6'] = []
adjacency_list['7'] = ['5']
adjacency_list['8'] = []

test = 'bfs'
if test == 'dfs':
    dfs = depth_first_search.DepthFirstSearch(
        adjacency_list=adjacency_list, strat_node='1')
    dfs.run_dfs('1')

    cvalue = dfs.connected_components()
    print(cvalue)
    print(dfs.connected_nodes)

elif test == 'bfs':

    bfs = breadth_first_search.BreadthFirstSearch(
        adjacency_list=adjacency_list, start='1'
    )
    bfs.run_bfs()
    path = bfs.constructPathforNode(node='8')
    print(path)

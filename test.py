import depth_first_search

adjacency_list = {}
adjacency_list['1'] = ['2']
adjacency_list['2'] = ['3']
adjacency_list['3'] = ['1']
adjacency_list['4'] = ['5','6','7']
adjacency_list['5'] = []
adjacency_list['6'] = []
adjacency_list['7'] = ['5']
adjacency_list['8'] = []
dfs = depth_first_search.DepthFirstSearch(adjacency_list=adjacency_list, strat_node='1')
dfs.run_dfs('1')

cvalue = dfs.connected_components()
print(cvalue)
print(dfs.connected_nodes)
#Forward DFS by Behnam Heydarshahi, Jan 2015.

sample_graph = {'A': set(['B', 'C']),
         'B': set(['D']),
         'C': set(),
         'D': set(),
         'E': set(['B', 'F']),
         'F': set(['C'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
 	    print('visited ' + vertex)
            stack.extend(graph[vertex] - visited)
    return visited

reversed_graph = {
		'A': set(),
		'B': set(),
		'C': set(),
		'D': set(),
		'E': set(),
		'F': set(),
		}


#dfs(sample_graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
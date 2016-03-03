#Backward DFS by Behnam Heydarshahi, Feb. 2016
reversed_graph = {
		'A': set(),
		'B': set(),
		'C': set(),
		'D': set(),
		'E': set(),
		'F': set(),
		}


def getReverseGraph(graph , start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
	    for adjacent_node in graph[vertex]:
		    reversed_graph[adjacent_node].add(vertex);
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_backwards(graph, start):
	getReverseGraph(graph, start)
	dfs(reversed_graph, start)

getReverseGraph(sample_graph, 'A')

for key, value in reversed_graph.iteritems():
	print key  
	print' adjacents: ' 
	print value

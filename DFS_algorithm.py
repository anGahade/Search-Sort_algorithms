# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#
#     visited.add(start)
#
#     print(start)
#
#     for next_node in graph[start] - visited:
#         dfs(graph, next_node, visited)
#
#     return visited
#
#
# graph = {
#     '0': set(['1', '2']),
#     '1': set(['0', '3', '4']),
#     '2': set(['0']),
#     '3': set(['1']),
#     '4': set(['1', '3'])
# }
# dfs(graph, '0')


def dfs_2(graph, start):
    visited = set()
    stack = [start]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            stack.extend(reversed(graph[current_node]))


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_2(graph, 'A')

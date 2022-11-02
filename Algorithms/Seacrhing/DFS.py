# Implementation of the Depth First Search (BFS):
# - Runtime: O(V + E)
# - Space: O(V)
# Where is the number of vertex and E is the number of Edges

# We use the recursive approach here


from distutils.ccompiler import gen_preprocess_options


def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    print(start)

    for next in graph[start]:
        if next not in visited:
            DFS(graph, next, visited)
    return visited


if __name__ == '__main__':
    graph = {
        '0': set(['1', '2']),
        '1': set(['0', '3', '4']),
        '2': set(['0']),
        '3': set(['1']),
        '4': set(['2', '3'])
        }

    DFS(graph, '0')

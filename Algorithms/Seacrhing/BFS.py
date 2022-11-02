# Implementation of the Breadth First Search (BFS):
# - Runtime: O(V + E)
# - Space: O(V)
# Where is the number of vertex and E is the number of Edges

# We use a queue here

from collections import deque

def BFS(graph, root):

    queue = deque()
    visisted = set()

    visisted.add(root)
    queue.append(root)

    while queue:
        
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbor in graph[vertex]:
            if neighbor not in visisted:
                visisted.add(neighbor)
                queue.append(neighbor)

        
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    BFS(graph, 0)
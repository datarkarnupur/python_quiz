def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node,end=" ")

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
print("DFS traversal:")
dfs(graph,'A')
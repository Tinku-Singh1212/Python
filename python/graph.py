graph={"A":['B','C'],
      "B":['D','E'],
      "C":['F'],
      "D":[],
      "E":['F'],
      "F":[]
      }
visited=[]
que=[] 
def bfs(visited,graph,node):
  visited.append(node)
  que.append(node)

  while que:
    s=que.pop(0)
    print(s,end=" ")
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)  
        que.append(neighbour)
bfs(visited,graph,'A')

# add vertext
def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []

# create link between adjucent node
def edge(v , adj_v , w):
    global graph
    temp = (adj_v,w)
    graph[v].append(temp)

# adjucent node of vetex
def adj(v):
    global graph
    return graph[v]

H = {}

# add hurastic value
def h(v,w):
    global H
    H[v] = w

# show hurastic value
def hu(v):
    return H[v]

# to choose optimal path 
def astar(root , goal):
    open = [root]
    visited = []
    Parameter ={}
    Parameter[root] = 0
    path ={}
    path[root] = root
    i = 0
    while len(open)>0:
        n =None
        for v in open:
            if n==None or Parameter[v]+hu(v)<Parameter[n]+hu(n):
                n = v
                print(n)
        
        if n == goal:
            list = []
            print(path)
            while path[n] !=n:
                list.append(n)
                n = path[n]
            list.append(root)
            list.reverse()
            return list
        for (node , weight) in near(n):
            print("//",node)
            if node not in open and node not in visited:
                Parameter[node] = weight + hu(node)
                path[node] = n
                open.append(node)
            elif Parameter[node] >Parameter[n]+weight:
                Parameter[node]  =Parameter[n]+weight
                path[node] = n
                if node in visited:
                    visited.remove(node)
                    open.append(node)
        open.remove(n)
        visited.append(n)
        print(visited)


graph ={}
vertices_no = 0

# code add data
for _ in range(4):
    add_vertex(input(">"))
print("link")

link = int(input("Number of links>"))

for _ in range(link):
    edge(input("vertext>"),input("adj_vertext>"),int(input("weight>")))

print("Hurastic Value")

for _ in range(4):
    h(input("vertex>"),input("weight>"))

print("optimal path is:",astar(input("root>"),input("goal>")))

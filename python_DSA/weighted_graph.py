class Wgraph:
    def __init__(self,nodes=None,directed=False):
        self.graph={}
        self.directed=directed
        self.flag=False
        if nodes: self.graph={node : {} for node in nodes }
    
    def add_nodes(self,nodes=None):
        if nodes:
            self.graph=self.graph | {node : {} for node in nodes }

    def add_edge(self,node1,node2,weight=0):
        if node1 not in self.graph: print(f"{node1} is not in graph");return
        if node2 not in self.graph: print(f"{node2} is not in graph");return
        self.graph[node1][node2]=weight
        if not self.directed: self.graph[node2][node1]=weight

    def add_nodes_adjs(self,**nodes_adjs):
        for node,adjs in nodes_adjs.items():
            if node in  self.graph: self.graph[node]= self.graph[node] | adjs
            else: self.graph[node]=adjs
            for adj in adjs:
                if adj not in self.graph: self.graph[adj]={}
                if not self.directed: self.graph[adj]=self.graph[adj] | {node : adjs[adj]}

    def delete_nodes(self,*nodes):
        for node in nodes:
            if node not in self.graph: print(f'{node} not in graph');continue
            if not self.directed:
                for adj_node in self.graph[node]: self.graph[adj_node].pop(node)
            self.graph.pop(node)
    
    def delete_edge(self,node1,node2):
        if node1 not in self.graph: print(f"{node1} is not in graph");return
        if node2 not in self.graph: print(f"{node2} is not in graph");return
        if node2 not in self.graph[node1]:
            print(f"egde not found between {node1} and {node2}")
            return
        self.graph[node1].pop(node2)
        if not self.directed: self.graph[node2].pop(node1)

    def DFS_travesal(self,visited,start_node):
        if start_node not in visited:
            print(start_node)
            visited.append(start_node)
            for adj in self.graph[start_node]:
                self.DFS_travesal(visited,adj)

    def DFS_search(self,visited,start_node,node):
        if start_node not in visited and not self.flag:
            visited.append(start_node)
            if start_node == node:
                print("Node found")
                self.flag=True
                return
            for adj in self.graph[start_node]:
                self.DFS_search(visited,adj,node)
    
    def DFS_stack_travesal(self,start_node):
        visited=[]
        stack=[]
        stack.append(start_node)
        while stack:
            node=stack.pop()
            if node not in visited:
                print(node)
                visited.append(node)
                for adj in self.graph[node]:
                    if adj not in visited:
                        stack.append(adj)
        return visited      

    def DFS_stack_search(self,start_node,target_node):
        visited=[]
        stack=[]
        stack.append(start_node)
        while stack:
            node=stack.pop()
            if node not in visited:
                visited.append(node)
                if node == target_node:
                    return True
                for adj in self.graph[node]:
                    if adj not in visited:
                        stack.append(adj)
        return False      

    def dijkstras_algo(self,start_node):
        visited=[]
        total_nodes=len(self.graph)
        infinite=float('inf')
        table={node : [infinite,None] for node in self.graph}
        table[start_node][0]=0
        self.visit_node(start_node,visited,table)
        while len(visited) < total_nodes:
            unv_table={node : value[0] for node,value in table.items() if node not in visited }
            sorted_nodes=sorted(unv_table,key=unv_table.get)
            self.visit_node(sorted_nodes[0],visited,table)
        return table,visited
    
    def visit_node(self,node,visited,table):
        visited.append(node)
        adj_dist=[(adj , dist) for adj,dist in self.graph[node].items() if adj not in visited ]
        for adj,distance in adj_dist:
            if distance + table[node][0] < table[adj][0] :
                table[adj][0]=distance + table[node][0]
                table[adj][1]=node
            elif distance + table[adj][0] < table[node][0] :
                table[node][0]=distance + table[adj][0]
                table[node][1]=adj

    def shortest_path(self,table,end_node):
        if end_node not in table: print(f'{end_node} not in graph or table'); return
        total_distance=table[end_node][0]
        cur_node=end_node
        path=self.go(cur_node,table)
        return total_distance,path
    
    def go(self,cur_node,table):
        if cur_node is None: return []
        return self.go(table[cur_node][1],table) + [cur_node]

    def add_edges(self):
        while 1:
            node1=input("node1 : ")
            if node1=='q': return
            self.add_edge(node1,input("node2 : "),int(input("weight : ")))

    def BFS_travesal(self,start_node):
        if start_node not in self.graph : print(f'{start_node} not in graph'); return []
        visited=[]
        queue=[]
        queue.append(start_node)
        while queue:
            selected_node=queue.pop(0)
            if selected_node not in visited:
                print(selected_node)
                visited.append(selected_node)
                queue=[*queue,*self.graph[selected_node]]
        return visited

    def BFS_search(self,start_node,target_node):
        if start_node not in self.graph : print(f'{start_node} not in graph'); return False
        visited=[]
        queue=[]
        queue.append(start_node)
        while queue:
            selected_node=queue.pop(0)
            if selected_node not in visited:
                visited.append(selected_node)
                if selected_node == target_node:
                    return True
                queue=[*queue,*self.graph[selected_node]]
        return False
w=Wgraph(['A','B','C','D','E','F','G'])
w.add_nodes(['H','I','J','K','L','M'])
w.graph={'A': {'F': 1, 'B': 8, 'G': 5}, 'B': {'A': 8, 'G': 2, 'C': 16}, 'C': {'B': 16, 'H': 5, 'D': 4}, 'D': {'C': 4, 'H': 10, 'I': 11, 'E': 23}, 'E': {'D': 23, 'I': 12, 'M': 10}, 'F': {'A': 1, 'J': 1}, 'G': {'A': 5, 'J': 3, 'B': 2, 'K': 6}, 'H': {'K': 3, 'C': 5, 'L': 4, 'D': 10}, 'I': {'L': 18, 'D': 11, 'E': 12, 'M': 1}, 'J': {'F': 1, 'G': 3, 'K': 2}, 'K': {'J': 2, 'G': 6, 'L': 7, 'H': 3}, 'L': {'K': 7, 'H': 4, 'I': 18, 'M': 20}, 'M': {'L': 20, 'I': 1, 'E': 10}}
print(w.BFS_search('B','M'))
table,visited=w.dijkstras_algo('B')
print(w.graph)
print(table)
print(visited)
d,_path=w.shortest_path(table,'M')
print(f'shortest_path : {_path}')
print(f'total_distance : {d}')
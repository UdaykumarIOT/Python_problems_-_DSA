class Graph:
    def __init__(self,nodes=None,directed=False):
        self.graph={}
        self.directed=directed
        self.flag=False
        if nodes:

            self.graph={node : set() for node in nodes}
    
    def add_nodes(self,nodes=None):
        if nodes:
            self.graph=self.graph | {node : set() for node in nodes }

    def add_edge(self,node1,node2):
        if node1 not in self.graph:
            print(f"{node1} is not in graph")
            return
        if node2 not in self.graph:
            print(f"{node2} is not in graph")
            return
        self.graph[node1].add(node2)
        if not self.directed: self.graph[node2].add(node1)

    def add_nodes_adjs(self,**nodes_adjs):
        for node,adjs in nodes_adjs.items():
            if node in  self.graph:
                self.graph[node].update(adjs)
            else:
                self.graph[node]=set(adjs)

            for adj in adjs:
                if adj not in self.graph:
                    self.graph[adj]=set()
                if not self.directed:
                    self.graph[adj].add(node)
        
    def delete_nodes(self,*nodes):
        for node in nodes:
            if node not in self.graph:
                print(f'{node} not in graph')
                continue
            if not self.directed:
                for adj_node in self.graph[node]:
                    self.graph[adj_node].remove(node)
            self.graph.pop(node)
    
    def delete_edge(self,node1,node2):
        if node1 not in self.graph:
            print(f"{node1} is not in graph")
            return
        if node2 not in self.graph:
            print(f"{node2} is not in graph")
            return
        if node2 not in self.graph[node1]:
            print(f"edge not found between {node1} and {node2}")
            return
        self.graph[node1].remove(node2)
        if not self.directed:
            self.graph[node2].remove(node1)
    
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
    
    def Dijkstras_algo(self,start_node):
        visited=[]
        total_node=len(self.graph)
        infinite=float('inf')
        table={node : [infinite,None] for node in self.graph }
        table[start_node][0]=0
        self.visit_node(start_node,table,visited)
        while len(visited) < total_node:
            unv_table={node : value[0] for node,value in table.items() if node not in visited}
            sorted_nodes=sorted(unv_table,key=unv_table.get)
            self.visit_node(sorted_nodes[0],table,visited)
        return table,visited
    
    def visit_node(self,node,table,visited):
        visited.append(node)
        unv_adjs=[adj for adj in self.graph[node] if adj not in visited ]
        distance=1
        for adj in unv_adjs:
            if table[node][0] + distance < table[adj][0]:
                table[adj][0]=table[node][0]+distance
                table[adj][1]=node
            elif table[adj][0] + distance < table[node][0]:
                table[node][0]=table[adj][0]+distance
                table[node][1]=adj


    def shortest_distance(self,table,end_node):
        if end_node not in table: print(f'{end_node} not in table'); return
        shortest_dist=table[end_node][0]
        path=self.go(table,end_node)
        return path,shortest_dist
    
    def go(self,table,cur_node):
        if cur_node is None: return[]
        return self.go(table,table[cur_node][1]) + [cur_node]
    
    def add_edges(self):
        while 1:
            node1=input("node1 : ")
            if node1=='q': return
            self.add_edge(node1,input("node2 : "))


g=Graph(['A','B','C','D','E','F','G','H','I','J','K'])
g.add_edge('A','B')
g.add_edge('B','D')
g.add_edge('C','D')
g.add_edge('E','F')
g.add_edge('D','E')
g.add_edge('C','G')
g.add_edge('G','I')
g.add_edge('I','J')
g.add_edge('K','J')
g.add_edge('H','K')
g.add_edge('H','G')
print(g.BFS_search('G','A'))
table,visited=g.Dijkstras_algo('A')
path,dist=g.shortest_distance(table,'K')
print(table)
print(visited)
print(path)
print(dist)


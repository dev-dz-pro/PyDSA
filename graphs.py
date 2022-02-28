# DIRECTED & No CYCLE GRAPH

AIRPORTS = ["CHLF", "ALG", "ORN", "TIZI", "WRGL"]
ROUTES = [["CHLF", "WRGL"], 
        ["CHLF", "TIZI"], 
        ["ALG", "CHLF"], 
        ["ALG", "WRGL"], 
        ["ORN", "CHLF"], 
        ["ORN", "WRGL"], 
        ["TIZI", "ALG"], 
        ["TIZI", "ORN"]]

class Graph:
    def __init__(self):
        self.graph = self.create_graph()

    def has_route_bfs(self, frm: str, to: str): # breadth first search
        queue = [frm]
        visited = set()
        while queue:
            airport = queue.pop(0)
            print(airport) # to display visited airports
            if airport == to:
                return True
            if airport in self.graph:
                for d in self.graph[airport]:
                    if d not in visited:
                        queue.append(d)
                        visited.add(d)
        return False
    
    def has_route_dfs(self, frm: str, to: str): # depth first search
        stack = [frm]
        visited = set()
        while stack:
            airport = stack.pop()
            print(airport) # to display visited airports
            if airport == to:
                return True
            if airport in self.graph:
                for d in self.graph[airport]:
                    if d not in visited:
                        stack.append(d)
                        visited.add(d)
        return False


    def shortest_path_bfs(self, frm: str, to: str):
        pass

    def shortest_path_dfs(self, frm: str, to: str):
        pass
                
    @staticmethod
    def create_graph():
        ADJACENCY_LIST = {}
        my_set = set()
        for loc, dist in ROUTES:
            if loc not in my_set:
                my_set.add(loc)
                ADJACENCY_LIST[loc] = [dist]
            else:
                ADJACENCY_LIST[loc].append(dist)
        return ADJACENCY_LIST



if __name__ == '__main__':
    graph = Graph()
    print("--------------------- BFS - ALG -> ORN ---------------------")
    print(graph.has_route_bfs("ALG", "ORN"))
    print("--------------------- BFS - WRGL -> TIZI ---------------------")
    print(graph.has_route_bfs("WRGL", "TIZI"))
    print("--------------------- DFS - ALG -> ORN ---------------------")
    print(graph.has_route_dfs("ALG", "ORN"))
    print("--------------------- DFS - WRGL -> TIZI ---------------------")
    print(graph.has_route_dfs("WRGL", "TIZI"))
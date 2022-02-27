# DIRECTED SYCLE GRAPH

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
    def has_route(self, frm: str, to: str):
        graph = self.create_graph()
        if frm not in graph:
            return False
        queue = [frm]
        while queue:
            node = queue.pop(0)
            if node == to:
                return True
            if node in graph:
                for d in graph[node]:
                    queue.append(d)
                
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
    print(graph.has_route("ALG", "ORN"))
graph = {
    "P1": ["P2", "P3"],
    "P2": ["P4"],
    "P3": ["P4", "P5"],
    "P4": ["P5"],
    "P5": []
}

order = []
visited = set()
counter = {"depth": 0, "max_depth": 0}

def dfs(node):
    counter["depth"] += 1
    if counter["depth"] > counter["max_depth"]:
        counter["max_depth"] = counter["depth"]
    
    order.append(node)
    visited.add(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor)
            
    counter["depth"] -= 1

dfs("P1")
print("order:", order)
print("visited:", sorted(list(visited)))
print("max depth:", counter["max_depth"])

cycle_graph = {
    "A": ["B"],
    "B": ["A"]
}
order_cycle = []
visited_cycle = set()

def dfs_cycle(node):
    order_cycle.append(node)
    visited_cycle.add(node)
    for neighbor in cycle_graph.get(node, []):
        if neighbor not in visited_cycle:
            dfs_cycle(neighbor)

dfs_cycle("A")
print("cycle order:", order_cycle)

import queue as Q

dict_hn = {
    "Arad": 336, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Eforie": 161,
    "Fagaras": 178, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 98, 
    "Rimnicu_Vilcea": 193, "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, 
    "Vaslui": 199, "Zerind": 374
}

dict_gn = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Bucharest": {"Urziceni": 85, "Giurgiu": 90, "Pitesti": 101, "Fagaras": 211},
    "Craiova": {"Dobreta": 120, "Rimnicu_Vilcea": 146, "Pitesti": 138},
    "Dobreta": {"Craiova": 120, "Mehadia": 75},
    "Eforie": {"Hirsova": 86},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Giurgiu": {"Bucharest": 90},
    "Hirsova": {"Eforie": 86, "Urziceni": 98},
    "Iasi": {"Neamt": 87, "Vaslui": 92},
    "Lugoj": {"Mehadia": 70, "Timisoara": 111},
    "Mehadia": {"Dobreta": 75, "Lugoj": 70},
    "Neamt": {"Iasi": 87},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Pitesti": {"Rimnicu_Vilcea": 97, "Bucharest": 101, "Craiova": 138},
    "Rimnicu_Vilcea": {"Pitesti": 97, "Craiova": 146, "Sibiu": 80},
    "Sibiu": {"Oradea": 151, "Fagaras": 99, "Rimnicu_Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98},
    "Vaslui": {"Iasi": 92, "Urziceni": 142},
    "Zerind": {"Arad": 75, "Oradea": 71}
}

def get_fn(path):
    gn = sum(dict_gn[path[i]][path[i+1]] for i in range(len(path)-1))
    hn = dict_hn[path[-1]]
    return gn + hn

def astar(start,goal):
    q = Q.PriorityQueue()
    visited = set()

    q.put((get_fn([start]),[start]))

    while not q.empty():
        fn, path = q.get()
        city = path[-1]
        visited.add(city)

        if city == goal:
            total_cost = fn - dict_hn[city]
            return path,total_cost
        
        for neighbor in dict_gn[city]:
            if neighbor not in visited:
                q.put((get_fn(path+[neighbor]),path+[neighbor]))
    return None, 0

def main():
    start = "Arad"
    goal = "Bucharest"

    path,cost = astar(start,goal)
    if path:
        print("->".join(path))
        print(f"Cost was {cost}")
    else:
        print("No Path found!")

main()
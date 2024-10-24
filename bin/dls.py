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


def dls(start,goal,depth,visited,path):

    if depth <=0 :
        return False
    visited.add(start)
    path += [start]

    if start == goal:
        return path
    
    
    for city in dict_gn[start]:
        if city not in visited:
            found = dls(city,goal,depth-1,visited,path)
            if found:
                return found
    return False

def main():
    start ="Arad"
    goal = "Bucharest"
    depth = 7
    print(dls(start,goal,depth,set(),[]))
    found = dls(start,goal,depth,set(),[])
    if found:
        print("->".join(found))
    else:
        print("Failed to find path")

main()
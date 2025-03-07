import heapq
from collections import defaultdict

# Build the graph
edges = [
    ('Almeria', 'Granada', 167),
    ('Almeria', 'Murcia', 218),
    ('Murcia', 'Albacete', 146),
    ('Murcia', 'Alicante', 81),
    ('Alicante', 'Albacete', 167),
    ('Granada', 'Jaen', 92),
    ('Granada', 'Malaga', 123),
    ('Malaga', 'Sevilla', 206),
    ('Malaga', 'Cadiz', 235),
    ('Cadiz', 'Huelva', 210),
    ('Cadiz', 'Sevilla', 121),
    ('Cordoba', 'Sevilla', 140),
    ('Cordoba', 'Jaen', 120),
    ('Cordoba', 'CiudadReal', 195),
    ('Merida', 'Sevilla', 192),
    ('Merida', 'Badajoz', 64),
    ('Merida', 'Caceres', 75),
    ('Valencia', 'Alicante', 166),
    ('Valencia', 'Castellon', 74),
    ('Valencia', 'Cuenca', 199),
    ('Castellon', 'Tarragona', 187),
    ('Castellon', 'Teruel', 144),
    ('Teruel', 'Cuenca', 148),
    ('Teruel', 'Zaragoza', 171),
    ('Tarragona', 'Barcelona', 99),
    ('Barcelona', 'Lleida', 163),
    ('Barcelona', 'Gerona', 103),
    ('Lleida', 'Gerona', 229),
    ('Lleida', 'Huesca', 112),
    ('Lleida', 'Zaragoza', 152),
    ('Cuenca', 'Albacete', 144),
    ('CiudadReal', 'Toledo', 118),
    ('Zaragoza', 'Huesca', 74),
    ('Zaragoza', 'Pamplona', 178),
    ('Zaragoza', 'Soria', 159),
    ('Zaragoza', 'Guadalajara', 256),
    ('Pamplona', 'Huesca', 165),
    ('Madrid', 'Jaen', 331),
    ('Madrid', 'Albacete', 257),
    ('Madrid', 'Cuenca', 168),
    ('Madrid', 'Guadalajara', 60),
    ('Madrid', 'Burgos', 245),
    ('Madrid', 'Segovia', 92),
    ('Madrid', 'Avila', 109),
    ('Madrid', 'Caceres', 301),
    ('Madrid', 'Toledo', 72),
    ('Salamanca', 'Avila', 109),
    ('Salamanca', 'Caceres', 202),
    ('Salamanca', 'Zamora', 66),
    ('Avila', 'Segovia', 66),
    ('Valladolid', 'Segovia', 115),
    ('Valladolid', 'Leon', 136),
    ('Valladolid', 'Zamora', 100),
    ('Valladolid', 'Palencia', 51),
    ('Palencia', 'Burgos', 92),
    ('Soria', 'Burgos', 142),
    ('Soria', 'Guadalajara', 171),
    ('Soria', 'Logrono', 101),
    ('Vitoria', 'Logrono', 94),
    ('Vitoria', 'Burgos', 118),
    ('Vitoria', 'SanSebastian', 100),
    ('Vitoria', 'Bilbao', 62),
    ('Bilbao', 'SanSebastian', 101),
    ('Bilbao', 'Santander', 100),
    ('Burgos', 'Santander', 181),
    ('Santander', 'Oviedo', 192),
    ('Leon', 'Zamora', 141),
    ('Leon', 'Lugo', 223),
    ('Leon', 'Oviedo', 125),
    ('Lugo', 'Oviedo', 227),
    ('Lugo', 'Coruna', 98),
    ('Lugo', 'Pontevedra', 195),
    ('Oviedo', 'Coruna', 287),
    ('Santiago', 'Coruna', 75),
    ('Santiago', 'Pontevedra', 64),
    ('Pontevedra', 'Orense', 119),
    ('Orense', 'Zamora', 259),
]

graph = defaultdict(list)
for city_a, city_b, cost in edges:
    graph[city_a].append((city_b, cost))
    graph[city_b].append((city_a, cost))

heuristic = {
    'Almeria': 571,
    'Granada': 507,
    'Jaen': 439,
    'Cordoba': 419,
    'Malaga': 550,
    'Huelva': 525,
    'Sevilla': 487,
    'Cadiz': 586,
    'Murcia': 510,
    'Albacete': 383,
    'Alicante': 515,
    'Valencia': 441,
    'Castellon': 435,
    'Tarragona': 502,
    'Barcelona': 576,
    'Lleida': 445,
    'Gerona': 627,
    'Merida': 334,
    'Badajoz': 363,
    'Caceres': 280,
    'CiudadReal': 305,
    'Toledo': 208,
    'Cuenca': 280,
    'Guadalajara': 173,
    'Zaragoza': 319,
    'Teruel': 337,
    'Huesca': 362,
    'Logrono': 209,
    'Vitoria': 215,
    'Bilbao': 232,
    'SanSebastian': 292,
    'Santander': 215,
    'Oviedo': 212,
    'Coruna': 357,
    'Santiago': 343,
    'Pontevedra': 335,
    'Orense': 271,
    'Lugo': 278,
    'Madrid': 162,
    'Leon': 126,
    'Zamora': 87,
    'Salamanca': 109,
    'Segovia': 94,
    'Valladolid': 0,
    'Burgos': 114,
    'Palencia': 43,
    'Soria': 187,
    'Pamplona': 284,
    'Avila': 110,
}

def gbfs(graph, heuristic, start, target):
    edges = []
    heapq.heappush(edges, (heuristic[start], start))
    source = {}
    source[start] = None
    visited = set()
    
    while edges:
        current_prio, current = heapq.heappop(edges)
        
        if current in visited:
            continue
        visited.add(current)
        
        if current == target:
            break
        
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                if neighbor not in source:
                    source[neighbor] = current
                    heapq.heappush(edges, (heuristic[neighbor], neighbor))
    
    # Reconstruct path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = source.get(current, None)
    path.reverse()
    return path if path and path[0] == start else []

def astar(graph, heuristic, start, target):
    edges = []
    heapq.heappush(edges, (0 + heuristic[start], start))
    source = {}
    cost_so_far = {}
    source[start] = None
    cost_so_far[start] = 0
    
    while edges:
        current_prio, current = heapq.heappop(edges)
        
        if current == target:
            break
        
        for neighbor, cost in graph[current]:
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(edges, (priority, neighbor))
                source[neighbor] = current
    
    # Reconstruct path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = source.get(current, None)
    path.reverse()
    return path if path and path[0] == start else []

start = 'Malaga'
target = 'Valladolid'

gbfs_path = gbfs(graph, heuristic, start, target)
astar_path = astar(graph, heuristic, start, target)

print("gBest-First Search Path:", ' -> '.join(gbfs_path))
print("A* Search Path:", ' -> '.join(astar_path))
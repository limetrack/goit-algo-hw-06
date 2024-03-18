import networkx as nx

# Створення графа і додавання вагованих ребер
weighted_edges = [
    ("A", "B", 2), ("A", "C", 5), ("B", "C", 1), ("B", "D", 4), ("C", "E", 3),
    ("D", "E", 2), ("D", "F", 6), ("E", "F", 1), ("E", "G", 4), ("F", "G", 2),
    ("G", "H", 3), ("H", "A", 7)
]
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів від вершини A до всіх інших
dijkstra_paths = nx.single_source_dijkstra_path(G_weighted, source='A')

# Виведення найкоротших шляхів
for target, path in dijkstra_paths.items():
    print(f"Найкоротший шлях від A до {target}:", ' → '.join(path))

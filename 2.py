import networkx as nx

# Створення графу для моделювання транспортної мережі міста
G = nx.Graph()
edges = [
    ("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E"),
    ("D", "F"), ("E", "F"), ("E", "G"), ("F", "G"), ("G", "H"), ("H", "A")
]
G.add_edges_from(edges)

# Визначення початкової і кінцевої вершини
start_node = 'A'
end_node = 'G'

# Застосування DFS для знаходження шляху
dfs_path = nx.dfs_tree(G, source=start_node).edges()
dfs_path_list = [start_node] + [v for u, v in dfs_path if v == end_node or u == start_node]

# Застосування BFS для знаходження шляху
bfs_path = nx.bfs_tree(G, source=start_node).edges()
bfs_path_list = [start_node] + [v for u, v in bfs_path if v == end_node or u == start_node]

# Вивід результатів
print("DFS path:", dfs_path_list)
print("BFS path:", bfs_path_list)

# Аналіз шляхів
print("\nАналіз шляхів:")
print("DFS шлях більш прямолінійний і веде до швидкого досягнення цілі, якщо вона доступна через один із перших гілок, що досліджуються.")
print("BFS шлях може бути довшим, але забезпечує виявлення найкоротшого шляху в графі з невагованими ребрами.")

import networkx as nx
import matplotlib.pyplot as plt

# Створення графу для моделювання транспортної мережі міста
G = nx.Graph()

# Додавання вершин і ребер для прикладу (вершини можуть представляти зупинки або станції, а ребра - дороги або залізничні шляхи)
edges = [
    ("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E"),
    ("D", "F"), ("E", "F"), ("E", "G"), ("F", "G"), ("G", "H"), ("H", "A")
]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)
plt.title("Модель транспортної мережі міста")
plt.show()

# Аналіз основних характеристик графу
vertex_count = G.number_of_nodes()
edge_count = G.number_of_edges()
degrees = nx.degree(G)
average_degree = sum(dict(degrees).values()) / vertex_count

vertex_count, edge_count, average_degree

# Я створив модель транспортної мережі міста у вигляді графа. У цій мережі:
# Кількість вершин (станцій або зупинок): 8
# Кількість ребер (доріг або залізничних шляхів): 12
# Середній ступінь вершин (середня кількість з'єднань на вершину): 3.0
# Це означає, що в середньому кожна станція або зупинка з'єднана з трьома іншими станціями або зупинками у мережі. ​
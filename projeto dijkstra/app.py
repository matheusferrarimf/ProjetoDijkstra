#Importando libraries
from flask import Flask, render_template, request
from heapq import heapify, heappop, heappush

# Cria a aplicação Flask
app = Flask(__name__)

# Dicionário com lista de adjacência
graph = {
    "taio": {"rio do oeste": 257.4},
    "rio do oeste": {"taio": 257.4, "laurentino": 12, "presidente getulio": 250.8},
    "presidente getulio": {"rio do oeste": 250.8, "laurentino": 316.8, "rio do sul": 54, "ibirama": 18},
    "ibirama": {"presidente getulio": 18, "rio do sul": 39},
    "rio do sul": {"presidente getulio": 54, "ibirama": 39, "laurentino": 26, "lontras": 24, "aurora": 85.8},
    "laurentino": {"rio do oeste": 12, "presidente getulio": 316.8, "rio do sul": 26, "aurora": 36, "agronomica": 59.4, "trombudo central": 44},
    "trombudo central": {"laurentino": 44, "agronomica": 72.6, "braço do trombudo": 28},
    "braço do trombudo": {"trombudo central": 28},
    "agronomica": {"trombudo central": 72.6, "laurentino": 59.4, "aurora": 44, "ituporanga": 60, "agrolandia": 37.5},
    "aurora": {"agronomica": 44, "lontras": 54, "rio do sul": 85.8, "laurentino": 36},
    "lontras": {"aurora": 54, "rio do sul": 24},
    "agrolandia": {"agronomica": 37.5},
    "ituporanga": {"agronomica": 60, "petrolandia": 125.4, "imbuia": 37.5},
    "imbuia": {"ituporanga": 37.5},
    "petrolandia": {"ituporanga": 125.4}
}


class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0

        pq = [(0, source)]
        heapify(pq)

        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

        predecessors = {node: None for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors
    
    def shortest_path(self, source: str, target: str):
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        path.reverse()

        return path

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        cidade1 = request.form["cidade1"].lower()
        cidade2 = request.form["cidade2"].lower()

        
        G = Graph(graph)
        p = G.shortest_path(cidade1, cidade2)
        resultado = f"o menor caminho de {cidade1} para {cidade2} é {p}"

    return render_template("index.html", resultado=resultado, graph=graph)

if __name__ == "__main__":
    app.run(debug=True)



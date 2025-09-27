import heapq

# -------------------------
# Algoritmo de Dijkstra
# -------------------------
def dijkstra(grafo, origem):
    dist = {v: float("inf") for v in grafo}
    dist[origem] = 0
    pai = dict.fromkeys(grafo, None)

    fila = [(0, origem)]  # (distância, vértice)

    while fila:
        d, u = heapq.heappop(fila)
        if d > dist[u]:
            continue  # já encontrei melhor

        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pai[v] = u
                heapq.heappush(fila, (dist[v], v))

    return dist, pai


# -------------------------
# Algoritmo de Bellman-Ford
# -------------------------
def bellman_ford(grafo, origem):
    dist = {v: float("inf") for v in grafo}
    dist[origem] = 0

    pai = dict.fromkeys(grafo, None)

    vertices = list(grafo.keys())
    arestas = [(u, v, peso) for u in grafo for v, peso in grafo[u]]

    # Relaxar V-1 vezes
    for _ in range(len(vertices) - 1):
        atualizado = False
        for u, v, peso in arestas:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pai[v] = u
                atualizado = True
        if not atualizado:
            break

    # Detectar ciclo negativo
    for u, v, peso in arestas:
        if dist[u] + peso < dist[v]:
            raise ValueError("Ciclo negativo detectado!")

    return dist, pai


# -------------------------
# Exemplo prático
# -------------------------
# Grafo SEM pesos negativos (para Dijkstra)
grafo1 = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("D", 3)],
    "D": []
}

print("Dijkstra (origem A):")
dist, pai = dijkstra(grafo1, "A")
print("Distâncias:", dist)
print("Pais:", pai)
print()

# Grafo COM pesos negativos (para Bellman-Ford)
grafo2 = {
    "S": [("E", 8), ("A", 10)],
    "E": [("D", 1)],
    "D": [("A", -4), ("C", -1)],
    "C": [("B", -2), ("A", 2)],
    "B": [("A", 1)],
    "A": []
}

print("Bellman-Ford (origem S):")
dist, pai = bellman_ford(grafo2, "S")
print("Distâncias:", dist)
print("Pais:", pai)

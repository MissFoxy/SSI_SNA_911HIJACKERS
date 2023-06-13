import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Carica il file CSV
file911Associates = pd.read_csv("T:\\MAGISTRALE LEZIONI E MATERIALE\\[SSI] Sicurezza dei Sistemi Informativi\\DATASET911\\9_11_HIJACKERS_ASSOCIATES.csv")  # Assicurati che il tuo file CSV sia presente nella stessa directory del notebook o specifica il percorso completo
#file911Associates = pd.read_csv("T:\\MAGISTRALE LEZIONI E MATERIALE\\[SSI] Sicurezza dei Sistemi Informativi\\DATASET911\\9_11_HIJACKERS_PRIORCONTACTS.csv")

# Crea un grafo vuoto
G = nx.Graph()

# Aggiungi i nodi al grafo
nodi = file911Associates.columns[1:]  # Prendi i nomi dei nodi dalla prima riga del dataframe, escludendo la prima colonna
G.add_nodes_from(nodi)

# Aggiungi gli archi al grafo
for i, nodo1 in enumerate(nodi): #assegna ad i l'indice dell'elemento corrente e a nodo1 il valore dell'elemento corrente. Ciclo utilizzato per iterare sui nodi nella prima colonna della matrice.
    for j, nodo2 in enumerate(nodi):
        if file911Associates.iloc[i, j+1] == 1:
            G.add_edge(nodo1, nodo2)


print("Numero di nodi:", G.number_of_nodes())
print("Numero di archi:", G.number_of_edges())


#####################################################
############ DENSITÀ ################################
#####################################################

print("-----------------------------------------------------------------------------------------")
print("---------------------------------      DENSITà      -------------------------------------")
print("-----------------------------------------------------------------------------------------")

# Stampa il numero di nodi e archi del grafo
print("Numero di nodi:", G.number_of_nodes())
print("Numero di archi:", G.number_of_edges())
numeropossibiliarchi = (G.number_of_nodes() * (G.number_of_nodes() -1) )/2
print("Numero di tutti i possibili archi del grafo: ", numeropossibiliarchi)

#Densità:
densitàG = nx.density(G)
print("Densità del grafo: ", densitàG)

#Grado Medio
average_degree = sum(dict(G.degree()).values()) / len(G)
print("Grado Medio:", average_degree)

#Diametro
diametro = nx.diameter(G)
print("Diametro: ", diametro)


#####################################################
############ DEGREE CENTRALITY ######################
#####################################################

print("-----------------------------------------------------------------------------------------")
print("-----------------------      DEGREES E DEGREE CENTRALITY      ---------------------------")
print("-----------------------------------------------------------------------------------------")

# Calcola il grado di tutti i nodi
degrees = dict(G.degree())

# Calcola il grado medio dei nodi
avg_degree = sum(degrees.values()) / len(degrees)

# Ordina i valori del grado dei nodi in ordine decrescente
sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)

# Stampa il grado dei nodi
for nodo, grado in sorted_degrees[:10]:
    print("Nodo:", nodo, "Grado:", grado)

print("-----------------------------------")
# Stampa il grado medio dei nodi
print("Grado Medio dei Nodi:", avg_degree)

# Calcola la degree centrality di tutti i nodi
degree_centrality = nx.degree_centrality(G)

# Ordina i valori del grado dei nodi in ordine decrescente
degree_centrality_sorted = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

# Stampa i primi 10 nodi con la loro degree centrality
for i, (nodo, centrality) in enumerate(degree_centrality_sorted[:10]):
    print(str(i+1) + ". Nodo: " + str(nodo) + ", Degree Centrality: " + str(centrality))

#####################################################
############ BETWEENNESS ############################
#####################################################

print("-----------------------------------------------------------------------------------------")
print("-------------------------      BETWEENNESS CENTRALITY      ------------------------------")
print("-----------------------------------------------------------------------------------------")
#Betweenness Centrality dei Nodi:
node_betweenness = nx.betweenness_centrality(G)

#Ordino i valori di betweenness e li stampo
node_betweenness_sorted = sorted(node_betweenness.items(), key=lambda x: x[1], reverse = True)
for nodo, betwenness in node_betweenness_sorted[:10]:
    print("Il nodo ", nodo, "ha betwenness: ", betwenness)

print("-----------------------------------------------------------------------------------------")
print("------------------------      BETWEENNESS DEGLI ARCHI      ------------------------------")
print("-----------------------------------------------------------------------------------------")
#Betweenness Centrality degli archi:
edge_betweenness = nx.edge_betweenness_centrality(G)

#Ordino i valori di betweenness e li stampo
edge_betweenness_sorted = sorted(edge_betweenness.items(), key=lambda x: x[1], reverse = True)

for arco, betwenness in edge_betweenness_sorted[:10]:
    print("L'arco ", arco, "ha betwenness: ", betwenness)


#####################################################
############ CLOSENESS ##############################
#####################################################

print("-----------------------------------------------------------------------------------------")
print("--------------------------------      CLOSENESS      ------------------------------------")
print("-----------------------------------------------------------------------------------------")

#Closeness centrality
closenessG = nx.closeness_centrality(G)

#Ordino i valori di closeness e stampo i primi 10
closeness_sorted = sorted(closenessG.items(), key=lambda x: x[1], reverse = True)

for nodo, closeness in closeness_sorted[:10]:
    print("Nodo: ", nodo, "Closeness Centrality: ", closeness)

#####################################################
############ EIGENVECTOR ############################
#####################################################

print("-----------------------------------------------------------------------------------------")
print("--------------------------------      EIGENVECTOR      ----------------------------------")
print("-----------------------------------------------------------------------------------------")

# Eigenvector_centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

eigenvector_sorted = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)

for nodo, eigenvector in eigenvector_sorted[:10]:
    print("Nodo", nodo, " Eigenvector Centrality: ", eigenvector)
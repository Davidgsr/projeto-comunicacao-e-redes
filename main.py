import networkx as nx # biblioteca que carrega a rede
import matplotlib.pyplot as plt # biblioteca responsavél por desenhar o grafo

# Caminho da rede real
caminho_arquivo = "econ-mahindas.edges"

# === MEDIDAS DA REDE REAL ===
G_real = nx.read_edgelist(caminho_arquivo)
num_nos = G_real.number_of_nodes() # retorna o número de nós da rede
num_arestas = G_real.number_of_edges() # retorna o número de arestas da rede

# === CRIAÇÃO DA REDE ALEATÓRIA ===
G_rand = nx.gnm_random_graph(n=num_nos, m=num_arestas, seed=1) # cria uma rede aleatória de n nós e m arestas
# seed=1 é o ponto de partida, para que sempre seja gerado da mesma maneira a rede aleatória para organizarmos para plotar

# === LAYOUTS ===
# desenho dos grafos de forma que fiquem organizados visualmentes, o seed possui a mesma função acima
pos_real = nx.spring_layout(G_real, seed=1)
pos_rand = nx.spring_layout(G_rand, seed=1)

# === PLOTAGEM ===
fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # plotagem dos grafos lado a lado e as dimensões dos grafos

# === REDE REAL ===
axs[0].set_title("REDE REAL") # título do grafo
nx.draw_networkx_nodes(G_real, pos_real, node_size=10, node_color='blue', ax=axs[0]) # desenho dos nós
nx.draw_networkx_edges(G_real, pos_real, alpha=0.3, ax=axs[0]) # desenho das arestas
axs[0].set_axis_off() # esconde os eixos x e y na plotagem

# calcula o valor do CA (coeficiente de agrupamento do grafo real) e armezana na variavel
CAReal = nx.average_clustering(G_real) 


# textos com as medidas que encontramos da rede real
texto_real = (
    f"MEDIDAS\n\n"
    f"ORDEM:\n"
    f"COEF. AGRUPAMENTO: {CAReal:.5f}\n" # plotando o valor na caixa de texto, com 5 casas após a vírgula
    f"Nós: {num_nos}\n"
    f"Arestas: {num_arestas}\n"
)
fig.text(0.10, 0.05, texto_real, fontsize=10, bbox=dict(facecolor='white', alpha=0.7)) # plotagem da caixa de texto

# === Rede Aleatória ===
axs[1].set_title("REDE ALEATÓRIA") # título do grafo
nx.draw_networkx_nodes(G_rand, pos_rand, node_size=10, node_color='green', ax=axs[1]) # desenho dos nós
nx.draw_networkx_edges(G_rand, pos_rand, alpha=0.3, ax=axs[1]) # desenho das arestas
axs[1].set_axis_off() # esconde os eixos x e y na plotagem
 
# calcula o valor do CA (coeficiente de agrupamento do grafo aleatório) e armezana na variavel
CARand = nx.average_clustering(G_rand)

# textos com as medidas que encontramos da rede aleatória
texto_rand = (
    f"MEDIDAS\n\n"
    f"COEF. AGRUPAMENTO: {CARand:.5f}\n" # plotando o valor na caixa de texto, com 5 casas após a vírgula
    f"ORDEM:\n"
    f"Nós: {G_rand.number_of_nodes()}\n"
    f"Arestas: {G_rand.number_of_edges()}\n"
)
fig.text(0.55, 0.05, texto_rand, fontsize=10, bbox=dict(facecolor='white', alpha=0.7)) # plotagem da caixa de texto

plt.tight_layout() # arruma os espaços para que os grafos não fiquem espremidos
plt.show() # mostra a figura na tela

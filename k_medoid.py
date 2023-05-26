import numpy as np



def kmedoids(D, k, max_iter):
    # D est une matrice de distances n x n
    n = D.shape[0]
    
    # Initialisation aléatoire des médoides
    M = np.arange(n)
    np.random.shuffle(M)
    M = M[:k]
    
    # Initialisation des clusters et des coûts
    C = np.zeros(n)
    C_best = np.sum(D ** 2)
    
    # Boucle principale
    for _ in range(max_iter):
        # Assigner chaque point au médioïde le plus proche
        for i in range(n):
            distances = D[i, M]
            j = np.argmin(distances)
            C[i] = distances[j]
        
        # Trouver le meilleur nouveau médioïde pour chaque cluster
        M_new = np.zeros(k)
        for j in range(k):
            idx = (C == C[j])
            distances = np.sum(D[idx][:, idx], axis=1)
            j_new = np.argmin(distances)
            M_new[j] = np.where(idx)[0][j_new]
        
        # Vérifier si l'on a trouvé une meilleure solution
        C_new = np.sum(np.min(D[:, M_new], axis=1) ** 2)
        if C_new < C_best:
            M = M_new
            C_best = C_new
        else:
            break
    
    # Retourner les médoides et le coût final
    return M, C_best

data = np.random.rand(20,5)
n_clusters = 3

medoids, clusters = kmedoids(data,n_clusters,0)
print("Medoides: ")
print(medoids)
print("Clusters: ")
print(clusters)


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Charger les données Iris
iris = load_iris()
X = iris.datal
y = iris.target

# Clusteriser les données avec k-medoids
M, C = kmedoids(X, 3)

# Afficher les résultats en 3D
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=48, azim=134)
colors = np.array(['#ff7f0e', '#2ca02c', '#1f77b4'])

for c in range(3):
    ax.scatter(X[C == c, 0], X[C == c, 1], X[C == c, 2], c=colors[c])

ax.scatter(X[M, 0], X[M, 1], X[M, 2], marker='*', c='#d62728', s=1000)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
plt.show()

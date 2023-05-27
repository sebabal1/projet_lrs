---
author: "Bal Sebastien"
date: 2022-2023
documentclass: memoire-umons
title: DBSCAN
subtitle: Memoire subtitle
directeur: Mr Ben Thaieb
service: Master Sciences informatique
classoption:
  - oneside
toc: true
graphics: true
header-includes: |
  \usepackage{algpseudocode}

biblatex: true
biblio-title: Bibliography title
bibliography:
  - src/memoire-umons/ref.bib
---

\chapter{Introduction}

\chapter{Les bases et notion de vocabulaire}

Dans ce chapitre, nous allons mettre les bases de la clusterisation et les notions de vocabulaire pour la bonne compréhension de la suite de l'article.

### Base de données Spatiale

Ce terme est associé à la gestion d'ensembles d'objets dans l'espace plutôt qu'à des images ou des représentations graphiques de l'espace. Elle permet de stocker des informations dans l'espace telle que des bâtiments, des routes et des montagnes.

### Cluster

Un cluster est un ensemble qui contient des points de données similaires. Ces données sont regroupées suivant des critères définis par l'algorithme de clustering.

### Densité

Une densité est une mesure de la compacité des points de données dans un cluster.

### Algorithmes de regroupements

Les algorithmes de regroupement, tels que définit par Kaufman et Rousseeuw en 1990, se divisent en deux catégories : les algorithmes de partitionnement et les algorithmes hiérarchiques.

Un algorithme de partitionnement cherche à diviser une base de données D en n objets en un ensemble de k clusters, dans lequel k est un paramètre d'entrée fixé à l'avance. Comme première étape, l'algorithme de partitionnement va créé une partion initiale à partir de la base de données D, pour l'utiliser dans une méthode itérative afin d'optimiser une fonction objective. Dans ces algorithmes, chaque cluster est représenté soit par le centre de gravité du cluster comme le fait très bien k-means, soit par l'un des objets du cluster situé près de son centre comme k-medoid. Cette méthode en deux étapes faites par ces algorithmes permet de déterminer dans un premier temps k qui minimise la fonction objective, ensuite à attribuer à chaque objet du cluster dont le représentant est le plus proche de lui.

Un algorithme hiérarchique permet de créer une décomposition hiérarchique de la base de données D. Celle-ci est représentée par un dendogramme, qui est un arbre divisant itérativement D en sous-ensemble plus petits jusqu'à ce que chaque sous-ensemble ne contienne plus qu'un seul objet. Chaque noeud de l'arbre représente un cluster de D. Le dendogramme peut être construit de deux manières différentes : soit en partant des feuilles pour arriver à la racine (approche agglomérative), soit en partant de la racine pour arriver aux feuilles (approche divisive), en fusionnant ou divisant les clusters à chaque étape.

Contrairement aux algorithmes de partitionnement, les algorithmes hiérarchiques ne nécessitent pas de paramètre d'entrée k. Par contre, une condition d'arrêt doit être définie pour indiquer quand le processus de fusion ou de division doit s'arrêter.

### K-Means

L'algorithme K-Means vise à regrouper un ensemble de données en un certain nombre de clusters pré-définis par l'utilisateur. Cette méthode de clustering non hiérarchique commence en sélectionnant aléatoirement K centres de clusters, puis chaque point de données est ensuite attribué au centre du cluster le plus proche. Les centres des clusters sont ensuite mis à jour en utilisant les points de données nouvellement attribués et le processus se répète jusqu'à ce que les centres des clusters convergent vers une solution stable ou que le nombre d'itérations maximum soit atteint.

### K-Medoid

L'algorithme K-Medoid est une méthode de clustering qui vise à diviser un ensemble de données en un nombre prédéfini de clusters. Il utilise des objets réels de chaque cluster, ce qui rend l'algorithme plus résistant aux valeurs aberrantes. Celui-ci commence par sélectionner k objets de l'ensemble de données comme médoides initiaux, qui sont les objets qui minimisent la distance moyenne aux autres objets dans leur cluster. Ensuite, chaque objet est assigné au medoide le plus proche et les medoides sont mis à jour en choisissant le nouvel objet qui minimise la somme des distances entre lui et tous les autres objets de son cluster. Le processus est répété jusqu'à ce que les medoides ne changent plus ou que le nombre maximum d'itérations soit atteint.

### CLARANS

Ng et Han en 1994 ont exploré les algorithmes de partitionnement pour l'extraction de connaissances à partir de bases de données spatiales. Ils ont présenté une méthode améliorée de K-Medoid appelée CLARANS (Clustering Large Application based on RANdomized Search), qui est plus efficace et performant que les anciennes méthodes de K-Medoid. Malheureusement, elle est très couteuse en temps et en exécution pour de grandes bases de données, car elle implique des appels en O(n). CLARANS suppose également que tous les objets à regrouper peuvent résider en mémoire principale en même temps, ce qui n'est pas toujours possible pour de grandes bases de données.

\chapter{L'algorithme DBSCAN}
Nous allons parler dans ce chapitre de l'algorithme DBSCAN (Density Based Spatial Clustering of Applications with Noise), celui-ci est conçu pour détecter les clusters et le bruit dans une base de données spatiale. Il permet d'identifier des points aberrants et de les écartés de la solution finale.

L'idée la plus importante est le fait de prendre, pour chaque point d'un cluster, un voisinage d'un rayon donné, celui-ci doit contenir au moins un nombre minimum de points (MinPts), de sorte que la densité dans le voisinage dépasse un seuil déterminé (Eps).

Pour que l'algorithme fonctionne correctement, il a besoin de prendre deux paramètres en entrée. Ceux-ci sont MinPts, représenté par le nombre minimum de points situé à une distance inférieure ou égale à Eps, celui-ci est la distance qui permet de définir les points voisins d'un point donné.
Il peut bien entendu en prendre quatre paramètre en entrée. Dans l'article "A Denity Based Algorithm for discovering clusters ...", les auteurs nous montrent qu'ils utilisent quatre paramètres à l'algorithme, une liste de points venant d'une base de données spatiale, la distance Eps pour définir les voisins, un nombre minimum de points requis pour qu'un soit considéré comme central et que son voisinage soit dense, et une fonction pour calculer la distance entre deux points.

DBSCAN permet de distinguer trois types de points, les points centraux, les points frontières et les points aberrants. Les points centraux sont ceux qui contiennent un voisinage dense, les points frontières sont ceux qui font partie du voisinage d'un point central, et les point aberrants sont ni centraux, ni frontières, ce sont des points de bruits.

Lorsque l'on applique l'algorithme de clustering DBSCAN à un ensemble de données, les points centraux sont déterminés en fonction de leur proximité avec d'autres points dans l'ensemble. Les points qui sont à une distance inférieure ou égale à une valeur Eps sont regroupés ensemble dans un même cluster, mais leur étiquette de cluster peut être différente selon l'ordre dans lequel les clusters sont découverts. Les points qui se trouvent à la frontière de plusieurs clusters différents sont assignés au premier cluster découvert. Chaque cluster contient au moins un point central, mais peut contenir moins de points si certains des points centraux sont situés à une distance inférieure ou égale à Eps de points situés à la frontière d'un autre cluster. HDBSCAN est un modèle amélioré qui résout ce problème en éliminant la notion de point frontière. Ce modèle est donc capable de produire des clusters plus homogènes et plus cohérents.

## Approche mathématique de l'algorithme

L'article présente plusieurs définitions :

**Définition 1** (Voisinage Eps d'un point) :

Un voisinage Eps d'un point p, ce note $N_{Eps}(p)$, avec un ensemble d'onjets D, $N_{Eps}(p) = \{q \in D \mid distance(p,q) \leq Eps\}$

Lorsque tous les points qui sont inférieurs ou égaux à Eps sont inclus dans un même voisinage, il peut y avoir une confusion entre les différents clusters. Pour éviter cette confusion, il est recommandé de sélectionner un point central pour chaque cluster et de garantir que tous les points dans ce cluster se trouvent dans le voisinage de Eps de ce point central.

**Définition 2** (directemennt densité-atteignable)

Si un point q satisfait la condition de densité-atteignable directe par rapport à Eps et MinPts depuis un point q, alors on peut dire que p est directement densité-atteignable à partir de q.

Pour satisfaire les conditions il faut que ça respecte ceci :

1. $p \in N_{Eps}(q)$

2. $\mid N_{Eps}(q)\mid \geq MinPts$

**Définition 3** (Densité-atteignable)

La densité-atteignabilité d'un point p par rapport à un point q en utilisant Eps et MinPts est établie s'il existe une séquence de points $p_{1}$ à $p_{n}$, telle que $p_{1} = q$, $p_{n} = p$ et que chaque point $P_{i+1}$ est directement densité-atteignable à partir de $P_{i}$.

Afin d'établir l'accessibilité entre deux points tels que p et q, il est nécessaire qu'une séquence de points reliant p à q soit présente, et que chaque point de cette séquence soit densité-atteignable à partir du précédent. De cette façon, p et q deviennent densité-atteignables à partir d'autres points.

**Définition 4**(Densité-connecté)

Pour que deux points soient densité-connectés entre eux par rapport à Eps et MinPts, il faut qu'il y ait un point o qui permette à la fois à p et q d'être densité-atteignables par rapport à Eps et MinPts.

**Définition 5**(Cluster)

Un ensemble de points présent dans une base de données de points D. Un cluster C par rapport à Eps et MinPts est un sous-ensemble non vide de D qui répond aux conditions ci-dessous :

1. $\forall p,q$ : si $p \in C$ et q est densité-atteignable depuis p, alors $q \in C$(Maximalité).
2. $\forall p,q \in C :p$ est densité-connecté à q par rapport à Eps et MinPts(Connectivité).

**Définition 6**(Bruit)

En partant de $C_{1}, ...,C_{k}$ des clusters de l'ensemble de données D par rapport à Eps et MinPtsi, i=1,...,k. On peut définir le bruit comme un ensemble de points dans l'ensemble de données D ne faisant partie d'aucun cluster Ci, en d'autres mots, $\{p \in D \mid \forall i$ : $p \notin C_{i}\}$

Le seul moment où on peut etre certain qu'un point est aberrant est que son eps-voisinage ne contient qu'un seul point lui même. un point aberrant est un point qui ne fait partie d'aucun cluster.

A présent, on fait s'occuper des lemmes, ceux-ci vont permettre de définir le comportement de notre algorithme.

**Lemme 1**

Un point p dans D et $\mid N_{Eps}(p)\mid \geq$ MinPts. Alors l’ensemble $O = o \mid o \in D$ et o est densité-atteignable depuis p par rapport à Eps et MinPts est un cluster par rapport à Eps et MinPts.

Ce qui signifie que l'on construit le cluster en partant de p, puis en y ajoutant tous les points qui sont à une densité-atteignable depuis p et qui respectent les critères de distance Eps et de densité minimal MinPts.

**Lemme 2**

Soit C un cluster par rapport à Eps et MinPts et p un point quelconque dans C avec $\mid N_{Eps}(p)\mid \geq MinPts$. Alors C est égal à l'ensemble $O = \{o \mid o$ est densité-atteignable depuis p par rapport à Eps et MinPts $\}$.

Celui-ci permet de définir que chaque point peut récupérer tous les points atteignables à partir de n'importe quel point central. Ce qui signifie que le cluster contient tous les points qui sont distances atteignables d'un point central.

À partir des lemmes définit plus haut, la présentation de l'algorithme va être possible :

Function DBSCAN (Points : Points[], eps : float, minPts : int)

\begin{algorithmic}
\State $cluster \gets 1$
\For{$i = 1 \to Points.size$}
\State $point \gets Points[i]$
\If{$point.idCluster = Null$}
\State $voisins \gets rechercheV(point, Points,Eps)$
\If{$voisins.taille \geq minPts$}
\State $point.idCluster \gets cluster$
\State $etendreCluster(voisins,Points, cluster,eps, minPts)$
\State $cluster \gets cluster+1$
\Else
\State $point.cluster \gets 0$
\EndIf
\EndIf
\EndFor
\end{algorithmic}

Function etendreCluster(voisins : Points[], points : Points[], cluster : int, eps : int, minPts : int)
\begin{algorithmic}
\For {$point \to voisins$}
\If {$point.clu = NIL$}
\State $point.clu \gets cluster$
\State $voisinLocal \gets rechercheV(point, points, eps)$
\If {$voisinLocal.taille \geq minPts$}
\State $voisinLocal \gets voisins \cup voisinLocal$
\EndIf
\EndIf
\EndFor
\end{algorithmic}

L'algorithme commence par initialiser tous les points comme n'étant pas classifiés. Par la suite, il prend chaque point non classé, vérifie s'il est possible de former un cluster à partir de ce point en utilisant la fonction etendreCluster. S'il en est capable, alors il est nouveau identifiantCluster est attribué et l'algorithme continue à chercher d'autres points pour le cluster qu'il vient de commencer à créer.

La fonction etendreCluster permet de récupérer tous les points dans un voisinage à une distance Eps à partir du point actuel. Pour chaque points dnas le tableau des voisins, on vérifie si le points n'a pas déjà été assigné à un cluster. S'il est non assigné(NIL), on lui attribue l'identifiant du cluster en cours "cluster". Par la suite, on effectue une recherche du voisinage autour de ce point en utilisant la fonction rechercheV. Si le nombre de voisins trouvés est supérieur ou égal à MinPts, on ajoute ces voisins au tableau des voisins explorer. Une fois que tous les points du tableau ont été traité, la fonction se termine.

\chapter{Le bon choix des paramètres de DBSCAN}

## MinPts

Le paramètre de MinPts, permet un qualité du cluster et de la performance. Malheureusement, il n'y a pas de méthode universelle pour la déterminer, c'est pourquoi cela dépend de la nature des données et des objectifs de l'analyse. Il est important de bien définir la bonne valeur pour minimiser le bruit.

Dans l'article "ADBSCAN: Adaptive Density-based...", une approche adaptive est fait pour utiliser une mesure de densité locale pour estimer le nombre de voisins dans un rayon donné autour de chaque point. Cette mesure de densité est utilisée pour calculer une valeur de MinPts locale pour chaque point, qui est ensuite utilisé dans DBSCAN. Grâce à cela, il est possible d'identifier avec succès des clusters avec des densités variables dans différents ensembles de données.

## Eps

Le paramètre de Eps, est aussi un choix délicat pour le bon fonctionnement de DBSCAN. Ce paramètre est aussi important, si cette mesure n'est pas bonne cela peut entrainer des regroupements incorrects ou une division en plusieurs clusters.

Il y a plusieurs méthodes pour sélectionner la valeur de Eps, en utilisant une base de donnée sur la densité, par essais erreurs ou pour notre cas qui nous intéresse, en utilisant la méthode k-distance. L'article de Ester et al. (To do) propose une procédure qui repose sur la notion de la fonction k-dist, celle-ci mesure la distance entre chaque points d'une base de données et son k-ième voisin le plus proche. Avec cette fonction, on construit un graphe qui fournit des informatiosns sur la densité des points et la présence de points abérrants.

Afin de déterminer la valeur de Eps, on identifie le premier "creux" dans le graphe de la fonction k-dist. Ce creux correspond au point de seuil où tous les points situés à sa gauche sont considérés comme appartenant aux clusters dans la base de données.

Ainsi, en trouvant ce point de seuil, on définit la valeur d'Eps qui sépare les points aberrant des points appartenant aux clusters dans la base de données.

Dans l'article de Ester et al. \footfullcite{einstein} (to do), on constate que la valeur de k, une fois à 4, dans le graphe k-dist pour des données bidimensionnelles ne change pas grandement. À partir, de la valeur k=3, le graphe ne change que très peu lui aussi. C'est pour cette raison, qu'Ester et al. (to do) décident de garder par défaut la valeur de k=4 pour MinPts pour calculer le graphe k-dist.

![Graphique k-dist du schéma 6 \label{k_dist}](src/memoire-umons/images/k_dist_sample_6.png)


![Graphique avec des données triées pour la db \ref{k_dist}](src/memoire-umons/images/graphique_trie_4_dist_schema_6.png)



\chapter{Performances}

## Complexité de la fonction rechercheV

Cette fonction utilisée dans l'algorithme de DBSCAN permet de rechercher des voisins, celle-ci dépend généralement de l'algorithme d'accès spatial utilisé pour organiser les données. En règle générale, ce sont les arbres R\*-trees qui sont utilisés pour accélérer la recherche des voisins. Cette complexité montrée par Martin et al. (To do ), démontre que cette complexité est fréquemment en $\mathcal{O}(log (n + k))$, dans lequel n est le nombre total de points dans la base de données et k le nombre moyen de voisins dans le voisinage.

Dans leur article Ester et al. (to do) prétendent que leur algorithme DBSCAN se termine en $\mathcal{O}(n\cdot log (n))$. Cependant il s'avère que cette affirmation est incorrecte, comme l'a récemment souligné Gunawan (to do 11) l'algorithme de (Ester) s'exécute en $O(n^2)$ dans le pire des cas, indépendamment des paramètres Eps et MinPts.

## Comparaison entre DBSCAN et CLARANS

Dans cette partie, on va s'intéresser aux performances entre DBSCAN et CLARANS, celui-ci était le premier et seul algorithme de regroupement dans le but d'extraire des connaissances d'une base de données.

Comme CLARANS et DBSCAN sont deux algorithmes de regroupement distincts, il n'existe pas de mesure quantitative commune permettant d'évaluer précisément leur classification. L'évaluation faite ici est principalement visuelle

Une construction de différentes bases de données sont utilisées pour comparer visuellement l'exécution de DBSCAN avec celui de CLARANS. Les données sont générées aléatoirement en suivant certains modèles, ceux-ci vont permettre une meilleure visualisation des différents algorithmes. Ils sont visibles sur \ref{all_schemas}.
 
![Différentes base de données \label{all_schemas}](src/memoire-umons/images/echantillons_all.png)



Dans un premier temps, l'exécution de lalgorithme de CLARANS, le paramètre k est choisit pour aider l'algorithme a trouvé plus facilement les différents clusters. Cela à était fait par essaies erreurs jusqu'au moment ou l'algorithme parrassait regrouper plusieurs clusters visible facilement à l'oeil. On peut remarquer le résultat sur la figure \ref{clarans_all}.


![Résultats de CLARANS sur les bases de données \label{clarans_all}](src/memoire-umons/images/clarans_all.png)

Dans le diagramme 6, il est observé que CLARANS forme trois clusters, cependant, à première vue, on peut constater qu'il y a en réalité deux regroupements au total. Cela met en évidence le fait que CLARANS n'est pas aussi efficace dans l'identification des clusters, en particulier lorsque ces derniers ne contiennent pas la même quantité de points.

Dans le diagramme 4, il est remarqué que tous les clusters ne sont pas correctement identifiés, certains sont même divisés en deux. Tous les points sont inclus, ce qui indique également que CLARANS ne gère pas efficacement les points de bruit.

En ce qui concerne le diagramme 5, les clusters sont représentés de manière précise.

En ce qui concerne le diagramme 3, les clusters sont identifiés, à l'exception d'un cluster qui est divisé en deux. Malgré la proximité des points, on peut clairement constater les limites de CLARANS.


Passons maintenant à l'examen des regroupements à l'aide de l'algorithme DBSCAN \ref{dbscan_all}. Dans les diagrammes un, trois, quatre et six, nous observons la présence de regroupements comportant un nombre variable de points et qui démontrent également une résistance au bruit.

Dans les diagrammes deux et cinq, on rencontre un problème lié à la différence de densité entre les clusters existants. Cette disparité pose un défi car quelle que soit la valeur d'Eps choisie, il y aura des difficultés. Les clusters les plus denses peuvent être identifiés correctement, même si certains points sont considérés comme aberrants. En revanche, les clusters moins denses peuvent être identifiés correctement, mais tous les clusters présentant une grande densité et étant proches d'autres clusters seront regroupés en un seul cluster par DBSCAN. Dans l'article publié par Pearson Education(todo), un modèle HDBSCAN permet de résoudre ce problème de densité.


![Résultats de DBSCAN sur les bases de données \label{dbscan_all}](src/memoire-umons/images/dbscan_all.png)




\chapter{Conclusion}

### Bibliographie

Source pour K-means : l'algorithme K-means est "Introduction to Data Mining" de Tan, Steinbach, et Kumar.
Source pour K-medoid : k-medoid est "Pattern Recognition and Machine Learning" de Christopher M. Bishop.
Source pour K-medoid : Han, J., Pei, J., Kamber, M., & Tan, P. N. (2011). Data mining: concepts and techniques (3rd ed.). Morgan Kaufmann.

Source pour la partie DBSCAN + HDBSCAN : Le livre "Introduction to Data Mining" de Tan, Steinbach et Kumar, publié par Pearson Education, mentionne l'algorithme DBSCAN et explique comment il fonctionne pour regrouper les données en clusters en fonction de leur proximité. Il mentionne également la notion de points centraux et de points à la frontière, ainsi que le problème de l'affectation de ces points à des clusters différents.

L'article "Hierarchical Density-Based Clustering" de Campello, Moulavi et Sander, publié dans le Journal of Machine Learning Research, présente le modèle HDBSCAN comme une amélioration de DBSCAN pour résoudre le problème des points à la frontière. L'article explique comment HDBSCAN fonctionne en éliminant la notion de point frontière et en utilisant une hiérarchie de clusters pour produire des clusters plus homogènes et plus cohérents

Source pour les 4 paramètres : Ankerst, M., Breunig, M. M., Kriegel, H.-P., & Sander, J. (1999). OPTICS: Ordering points to identify the clustering structure. In ACM SIGMOD Record (Vol. 28, No. 2, pp. 49-60). ACM.

Source pour lemme 2 : Article scientifique : "Density-Based Clustering in Spatial Databases: A Review" par Rezaei et Aghabozorgi, publié en 2015 dans le journal "International Journal of Database Theory and Application". Le lemme 2 est discuté en section 3.1 de cet article : https://sci-hub.ru/https://link.springer.com/article/10.1023/A:1009745219419

https://sci-hub.ru/https://link.springer.com/chapter/10.1007/978-3-642-37456-2_14

Source pour MinPts et Eps sur le choix des valeurs : https://arxiv.org/ftp/arxiv/papers/1809/1809.06189.pdf

11 : . Gunawan. A faster algorithm for DBSCAN. Master’s thesis,
Technische University Eindhoven, March 2013.

Ester et al : M. Ester, H. Kriegel, J. Sander, and X. Xu. A density-based
algorithm for discovering clusters in large spatial databases with
noise. In SIGKDD, pages 226–231, 1996

Complexité : https://www.cse.cuhk.edu.hk/~taoyf/paper/sigmod15-dbscan.pdf

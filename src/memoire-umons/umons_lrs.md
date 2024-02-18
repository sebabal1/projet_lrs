---
author: "Bal Sébastien"
date: 2023-2024
documentclass: memoire-umons
title: Les cliques maximales dans les graphes dispersés 
subtitle: Lecture et rédaction scientifiques
directeur: Mr Mélot
department: Informatics
discipline: Informatics
service: Master Sciences Informatique
classoption:
  - oneside
toc: true
graphics: true
header-includes: |
  \usepackage{algpseudocode}
  \usepackage[french]{babel}
biblatex: true
biblio-title: Bibliographie
bibliography:
  - src/memoire-umons/ref.bib
---

\chapter{Introduction}

Dans cette partie, une brève mise en bouche du sujet avec une partie qui présentera les différents mots de vocabulaire que l'on utilisera dans l'article. Ensuite, une mise en avant du fonctionnement de l'algorithme ainsi qu'une démonstration de différents schémas et de l'utilisation des données pour montrer l'efficacité de cet algorithme. Une explication sera fournie avec des commentaires sur l'algorithme qui sera intégré avec python ainsi que les graphes qui auront été générés.

\chapter{Les bases et notions de vocabulaire}

## Graphes
*Un graphe* est composé d'un ensemble de points, appelés sommets, ceux-ci sont reliés entre eux par des lignes que l'on appelle des arêtes. Un sommet est représenté par un point et une arête par une ligne.

On donne généralement comme définition pour un graphe cette notation : $G = (V,E)$.
$G$ est un couple $(V,E)$ dans lequel, $V$ est un ensemble fini de sommets et $E$ est un ensemble d'arêtes, où chaque arête est un sous-ensemble de sommets de $V$ noté : $\{v_{i}, v_{j}\} \in V^2$.

Une arête est une entité caractérisée par une paire de sommets $\{v_{i}, v_{j}\}$. Ces deux sommets sont considérés comme adjacents. L'ensemble de ces sommets adjacents ${v_{i}} \in V$ est représenté sous la notation $Adj(v_{i}) = \{v_{i} \in V, \{v_{i},v_{j}\} \in E\}$

![Représentation d'un graphe \label{graphe}](src/memoire-umons/images_graph/graph.png){ width=250px }
 

## Une Clique

*Une clique*, au point de vue de la théorie des graphes, représente un sous-ensemble de sommets dans lequel chaque paire de sommets est reliée\cite{peay1974}.*La taille d'une clique* est un ensemble de $k$ nœuds dans lequel chaque paire de nœuds est reliée par une arête. Ceux-ci sont tous connectés, on parle de *sous-graphe* complet.

Un sous-graphe est un graphe se trouvant dans un autre graphe, la figure \ref{clique} représente un sous-graphe en vert dans un graphe en bleu.

Sur la figure \ref{clique}, on peut constater un graphe qui possède 7 sommets, les sommets en vert, numéroté 2,3,5, forment une clique de taille 3. Plusieurs méthodes existent pour détecter des cliques dans un graphe donné, celles-ci sont généralement complexes à utiliser. L'application la plus importante dans la détection de cliques est de trouver le nombre maximum de cliques dans un graphe. 

![Représentation d'une Clique \label{clique}](src/memoire-umons/images_graph/find_cliques.png){ width=250px }

## Dégénérescence 

*La dégénérescence* dans la théorie des graphes, est un paramètre. Celle-ci est la plus petite valeur ($k$) de façon qu'il soit $k$-dégénéré, sous-graphe contenant au moins un sommet de *degré* supérieur à $k$\cite{buchanan2013}. Comme le défini Wikipédia\cite{degree_wiki}, *un degré* d'un sommet dans la théorie des graphes, c'est le nombre de liens (arêtes) reliant ce sommet. 

L'article de Seidman\cite(seidman), présente qu'un $k$-core doit avoir au moins $k+1$ points, ainsi que les points des différents $k$-core ne peuvent pas être adjacents. Prenons les exemples qui suivent, en changeant la valeur de $k$, on obtient différent sous-graphe.

Le premier graphe est celui avec $k=0$, cela reprend tous les points du graphe à la figure \ref{0-core}. 

![Dégénérescence 0 \label{0-core}](src/memoire-umons/images_graph/k_0_degenerescence.png){width=250px}

Le graphe de la figure \ref{1-core} illustre un graphe de dégénérescence avec $k=1$. Tous les sommets sont inclus dans l'ensemble de ce sous-graphe, étant donné que chaque sommet est adjacent à au moins un autre sommet. La non-conformité à la condition $k=1$ surviendrait si un sommet n'était pas relié à un autre. Par exemple, le sommet $J$ ne respecte pas cette condition, car il est isolé, n'ayant aucune arête incidente avec d'autres sommets.

![Dégénérescence 1 \label{1-core}](src/memoire-umons/images_graph/k_1_degenerescence.png){width=250px}
  
Dans le graphe de la figure \ref{2-core}, avec $k=2$, nous notons que les sommets $A$ et $J$ ne sont pas inclus dans le sous-graphe. Ces sommets sont affichés en rouge pour indiquer qu'ils ne satisfont pas la contrainte de degré minimal égal ou supérieur à 2, conforme à la définition d'un 2-core.

![Dégénérescence 2 \label{2-core}](src/memoire-umons/images_graph/k_2_degenerescence.png){width=250px}

Pour une dégénérescence dans laquelle $k=3$, le graphe à la figure \ref{3-core}, ne regroupe pas dans le sous-graphe les sommets $A$, $F$ et $J$. Pour cette dernière représentation, c'est le point $F$ qui ne rentre pas dans les bonnes conditions.

![Dégénérescence 3 \label{3-core}](src/memoire-umons/images_graph/k_3_degenerescence.png){width=250px}

La valeur maximum qui a été trouvée pour le graphe à la figure \ref{3-core}, est la valeur de $k=3$, si $k=4$ alors tous les sommets ne feraient plus partie du sous-graphe, car aucun ne respectera la condition minimum de 3 arêtes. 

La dégénérescence d'un graphe offre une mesure de sa structure interne, en mettant en évidence des sous-ensembles rassemblant des sommets. Cependant, malgré sa pertinence sur l'analyse des réseaux, la dégénérescence seule ne suffit pas toujours à capturer toutes les subtilités de la connectivité dans un graphe. Ainsi, dans le prochain chapitre, nous explorerons l'algorithme de Bron-Kerbosh, une méthode efficace pour identifier et explorer les cliques maximales dans un graphe, offrant ainsi une perspective plus approfondie sur ses motifs de connectivité.



\chapter{Algorithme de Bron-Kerbosh}

\chapter{Présentation de l'algorithme de l'article}

\chapter{Conclusion}

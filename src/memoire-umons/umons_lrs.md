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

*Une clique*, au point de vue de la théorie des graphes, représente un sous-ensemble de sommets dans lequel chaque paire de sommets est reliée\cite{peay1974}.*La taille d'une clique* est un ensemble de $k$ noeuds dans lequel chaque paires de noeuds est reliée par une arête. Ceux-ci sont tous connectés, on parle de *sous-graphe* complet.

Un sous-graphe est un graphe se trouvant dans un autre graphe, la figure \ref{clique} représente un sous-graphe en vert dans un graphe en bleu.

Sur la figure \ref{clique}, on peut constater un graphe qui possède 7 sommets, les sommets en vert, numéroté 2,3,5, forment une clique de taille 3. Plusieurs méthodes existent pour détecter des cliques dans un graphe donné, celles-ci sont généralement complexes à utiliser. L'application la plus importante dans la détection de cliques est de trouver le nombre maximum de clique dans un graphe. 

![Représentation d'une Clique \label{clique}](src/memoire-umons/images_graph/find_cliques.png){ width=250px }

## Dégénérescence 

*La dégénérescence* d'un graphe permet de mesurer sa "rareté", elle permet d'indiquer à quel point un graphe est loin d'être dense. Un graphe $\{d\}$-dégénère est un graphe dans lequel chaque sous-graphe possède au moins un sommet de degré au plus de $\{d\}$. En grande majorité, la dégénérescence est comprise entre le degré minimum et le degré maximum ($\{d\}$).

Un graphe est dit $d$-dégénéré si chaque sous-graphe (non-vide) contient au moins un sommet de degré supérieur à $d$. La dégénérescence dans un graphe est la plus petite valeur de $d$ telle qu'il soit $d$-dégénéré. Dans l'article de Buchanan en 2013 \cite{buchanan2013}, tout graphe $d$-dégénéré admet un certain ordre au niveau de ces sommets ($\{v_{1}\}$, ...,$\{v_{n}\}$) dans lequel chaque sommet $\{v_{i}\}$ a plus de $d$ voisins.



*La dégénérescence* dans la théorie des graphes, est un paramètre. Celle-ci est la plus petite valeur ($k$) de façon qu'il soit $k$-dégénéré, sous-graphe contenant au moins un sommet de *degré* supérieur à $k$\cite{buchanan2013}. Comme le défini Wikipédia\cite{degree_wiki}, *un dégré* d'un sommet dans la théorie des graphes, c'est le nombres de liens (arêtes) reliant ce sommet. 



\chapter{Algorithme de Bron-Kerbosh}

\chapter{Présentation de l'algorithme de l'article}

\chapter{Conclusion}

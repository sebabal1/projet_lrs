---
author: "Bal Sébastien"
date: 2023-2024
documentclass: memoire-umons
title: All Maximal Cliques in Sparse Graphs
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

biblatex: true
biblio-title: Bibliographie
bibliography:
  - src/memoire-umons/ref_cliques.bib
---

\chapter{Introduction}

\chapter{Les bases et notions de vocabulaire}

## Graphes
Un graphe est composé d'un ensemble de points, appelés sommets, ceux-ci sont reliés entre eux par des lignes que l'on appelle des arêtes. Un sommet est représenté par un point et une arête par une ligne.

On donne généralement comme définition pour un graphe cette notation : $G = (V,E)$.
G est un couple (V,E) dans lequel, V est un ensemble fini de sommets et E est un ensemble d'arêtes, où chaque arête est un sous-ensemble de sommets de V noté : $\{v_{i}, v_{j}\} \in V^2$.

Une arête est une entité caractérisée par une paire de sommets $\{v_{i}, v_{j}\}$, elle est fréquemment représentée visuellement par la différence vectorielle entre ces deux sommets, c'est-à-dire $\{v_{i} - v_{j}\}$. Ces deux sommets sont considérés comme adjacents dans le contexte de l'arête. L'ensemble de ces sommets adjacents ${v_{i}} \in V$ est représenté sous la notation $Adj(v_{i}) = \{v_{i} \in V, \{v_{i},v_{j}\} \in E\}$

![Représentation d'un graphe \label{graphe}](src/memoire-umons/images_graph/graphe_1.png)
 

## Une Clique

Une clique, au point de vue de la théorie des graphes, représente un sous-ensemble de sommets dans lequel chaque paire de sommets est reliée. Ceux-ci sont tous connectés, on parle de sous-graphe complet. Sur la figure \ref{clique}, on peut constater un graphe qui possède 7 sommets, les sommets en rouge, numéroté 2,3,5, définissent la notion de sous-graphe complet. Plusieurs méthodes existent pour détecter des cliques dans un graphe donné, celles-ci sont généralement complexes à utiliser. Le problème le plus important dans la détection de clique est de trouver une structure de clique hiérarchique dans un réseau. 

Une autre définition, Luce et Perry \ref{peay1974}, une clique d'un graphe G est un sous-graphe complet maximal de G \ref{peay1974}. Une clique se forme à partir d'un groupe spécifique de points dans le graphe où chaque paire de points à l'intérieur du groupe est directement reliée, et aucun point en dehors de ce groupe n'a de connexions avec tous les points à l'intérieur.

![Représentation d'une Clique \label{clique}](src/memoire-umons/images_graph/clique_1.png)

## Dégénérescence 

La dégénérescence d'un graphe permet de mesuré sa "rareté", elle permet d'indiquer à quel point un graphe est loin d'être dense. Un graphe $\{d\}$-dégéréré est un graphe dans lequel chaque sous-graphe possède au moins un sommet de degré au plus de $\{d\}$. En grande majorité, la dégénérescence est comprise entre le degré minimum et le degré maximum ($\{d\}$).

Un graphe est dit $\{d\}$-dégénéré si chaque sous-graphe (non-vide) contient au moins un sommet de dégré suppérieur à $\{d\}$. La dégénérescence dans un graphe est la plus petite valeur de $\{d\}$ telle qu'il soit d$\{d\}$-dégénéré. Dans l'article de Buchanan en 2013 \footfullcite{buchanan2013}, tout graphe $\{d\}$-dégénéré admet un certain ordre au niveau de ces sommets ($\{v_{1}\}$, ...,$\{v_{n}\}$) dans lequel chaque sommets $\{v_{i}\}$ a plus de $\{d\}$ voisins.



\chapter{Algorithme de Bron-Kerbosh}

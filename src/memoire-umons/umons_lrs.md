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

Ajouter une image de la représentation d'un graphe
 



## Une Clique

Une clique, au point de vue de la théorie des graphes, représente un sous-ensemble de sommets dans lequel chaque paire de sommets est reliée. Ceux-ci sont tous connectés, on parle de sous-graphe complet. Sur la figure \ref{}, on peut constater un graphe qui possède X sommets, les sommets en rouge, numéroté X, définissent la notion de sous-graphe complet. 

Ajouter une image d'un graphe avec un clique


## Une Maximale Clique

## Sparse Graphs

## Degenerescence

\chapter{Algorithme de Bron-Kerbosh}

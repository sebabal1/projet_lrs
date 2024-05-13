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
*Un graphe* est composé d'un ensemble sommets, ceux-ci sont reliés entre eux par des arêtes. Au niveau de la représentation, un sommet est représenté par un point et une arête par une ligne.

On donne généralement comme définition pour un graphe cette notation : $G = (V,E)$.
$G$ est un couple $(V,E)$ dans lequel, $V$ est un ensemble fini de sommets et $E$ est un ensemble d'arêtes, où chaque arête est un sous-ensemble de sommets de $V$ noté : $\{v_{i}, v_{j}\} \in V^2$.

Une arête est une entité caractérisée par une paire de sommets $\{v_{i}, v_{j}\}$. Ces deux sommets sont considérés comme adjacents. L'ensemble des sommets adjacents à un sommet ${v_{i}} \in V$ est représenté sous la notation $Adj(v_{i}) = \{v_{i} \in V, \{v_{i},v_{j}\} \in E\}$

![Représentation d'un graphe \label{graphe}](src/memoire-umons/images_graph/graph.png){ width=250px }
 

## Une Clique

*Une clique*, au point de vue de la théorie des graphes, représente un sous-ensemble de sommets dans lequel chaque paire de sommets est reliée ~\cite{peay1974}.*La taille d'une clique* est la cardinalité d'un ensemble de $k$ nœuds dans lequel chaque paire de nœuds est reliée par une arête. Ceux-ci sont tous connectés, on parle de *sous-graphe* complet.

Un sous-graphe est un graphe se trouvant dans un autre graphe, la figure \ref{clique} représente un sous-graphe en vert dans un graphe en bleu. Dans nos exemples, les sous-graphes mentionnés sont des sous-graphes induit, Wikipedia cite, un sous-grape est obtenu en restreignant le graphe à un sous-ensemble de sommets et en conservant toutes les arêtes entre sommets de ce sous-ensemble ~\cite{graphe_induit_wiki}. Dans la suite de l'article, la notion de sous-graphe fait référence à une sous-graphe induit sauf mention contraire.

Ce qui amène a définir deux notions qui sont importantes au niveau des cliques, la clique maximale et la clique maximum. Une clique $C$ est dite maximale s'il n'existe pas de clique plus grande contenant $C$~\cite{bomze1997evolution}, ce qui signifie qu'une clique maximale ne peut pas être étendue en ajoutant un autre sommet du graphe tout en maintenant sa propriété de clique. Une clique (maximale) est dite maximum si elle contient plus de sommets parmi toutes les cliques~\cite{bomze1997evolution}.

La figure \ref{clique} représente un graphe qui possède 7 sommets, les sommets en vert, numéroté 2,3,5, forment une clique de taille $k=3$. Plusieurs méthodes existent pour détecter des cliques dans un graphe donné, celles-ci sont généralement complexes à utiliser. L'application la plus importante dans la détection de cliques est de trouver le nombre maximum de cliques dans un graphe. 

Dans le cadre de ce travail, on vise à identifier et énumérer toutes les cliques maximales d'un graphe donné. Un exemple illustratif est présenté dans la figure \ref{clique}, où l'on a identifié 6 cliques : les ensembles de sommets ${1,2}$, ${3,4}$, ${4,6}$,${5,6}$,${6,7}$ et ${2,3,5}$. Parmi ces cliques, celle qui contient le plus grand nombre de sommets est la dernière, ${2,3,5}$, qui est une clique maximum car elle contient 3 sommets.


![Représentation d'une Clique \label{clique}](src/memoire-umons/images_graph/find_cliques.png){ width=250px }

## Dégénérescence 

*La dégénérescence* dans la théorie des graphes, est un paramètre, celle-ci est la plus petite valeur de $k$ pour qu'un graphe soit $k$-dégénéré. Un graphe est $k$-dégénéré si au moins un sommet de *degré* est supérieur à $k$~\cite{buchanan2013}. Comme le défini Wikipédia~\cite{degree_wiki}, *un degré* d'un sommet dans la théorie des graphes, c'est le nombre d'arêtes reliant ce sommet. 

Le principe de décomposition en $k$-core consiste à trouver le sous-graphe le plus grand d'un réseau, dans lequel chaque noeud a au moins $k$ voisins dans le sous-graphe. Le processus de fonctionnement pour la décomposition est que l'on supprime récursivement les noeuds ayant des degrés inférieurs à la valeur de $k$ ~\cite{kong2019k}. Dans l'article de Seidman~\cite{seidman}, il explique qu'un $k$-core doit avoir au moins $k+1$ noeuds. Pour bien comprendre, prenons l'exemple d'un groupe social, dans lequel $k$ représente le nombre minimum de relations qu'un noeud doit avoir pour être inclus dans le $k$-core. Si nous avons 2-core, ce qui signifie que chaque personne dans ce 2-core a au moins 2 relations avec d'autres personnes dans le 2-core. Si nous n'avons que deux personnes dans ce 2-core. Cela signifie que chaque personne de ce 2-core a au plus 1 relation avec une autre personne dans le 2-core. Mais si chaque personne à 2 relations, cela signifie qu'il doit y avoir au moins quatre relations au total dans le 2-core. Ce qui implique qu'il doit y avoir au moins 3 personnes dans le 2-core. C'est pour cette raison qu'un $k$-core doit avoir au moins $k + 1$ noeuds.

Pour illustrer cela plus clairement, examinons les figures suivantes (voir les exemples de la figure \ref{0-core} à \ref{3-core}). En ajustant la valeur de $k$, nous obtenons différents sous-graphes. Analysons ceux-ci de façon détaillé, le premier graphe, celui de la figure \ref{0-core},est celui avec $k=0$, cela signifie que tous les sommets peuvent être sélectionné puisqu'il n'y a pas de contrainte au niveau du degré de dégénérescence. Les sommets qui sont sélectionnés sont en bleu. 

![Dégénérescence 0 \label{0-core}](src/memoire-umons/images_graph/k_0_degenerescence.png){width=250px}

Le graphe de la figure \ref{1-core} illustre un graphe de dégénérescence avec $k=1$. La non-conformité à la condition $k=1$ surviendrait si un sommet n'était pas relié à un autre. Le sommet $J$ ne respecte pas la condition de dégénérescense, il est isolé, n'ayant aucune arête incidente avec d'autres sommets. Il apparait en rouge sur notre figure. En revanche, tous les autres sommets en bleu sont inclus dans l'ensemble de ce sous-graphe, étant donné que chaque sommets est adjacent à au moins un autre sommet.

![Dégénérescence 1 \label{1-core}](src/memoire-umons/images_graph/k_1_degenerescence.png){width=250px}
  
Dans le graphe de la figure \ref{2-core}, avec $k=2$, nous notons que les sommets $A$ et $J$ ne sont pas inclus dans le sous-graphe. Ces sommets sont affichés en rouge pour indiquer qu'ils ne satisfont pas la contrainte de degré minimal égal ou supérieur à 2, conforme à la définition d'un 2-core.

![Dégénérescence 2 \label{2-core}](src/memoire-umons/images_graph/k_2_degenerescence.png){width=250px}

Pour une dégénérescence dans laquelle $k=3$, le graphe à la figure \ref{3-core}, ne regroupe pas dans le sous-graphe les sommets $A$, $F$ et $J$. Pour cette dernière représentation, c'est le point $F$ qui ne rentre pas dans les bonnes conditions.

![Dégénérescence 3 \label{3-core}](src/memoire-umons/images_graph/k_3_degenerescence.png){width=250px}

La valeur maximum qui a été trouvée pour le graphe à la figure \ref{3-core}, est la valeur de $k=3$, puisque si $k=4$ alors tous les sommets ne feraient plus partie du sous-graphe, car aucun ne respectera la condition minimum de 3 arêtes. 

La dégénérescence d'un graphe offre une mesure de sa structure interne, en mettant en évidence des sous-ensembles rassemblant des sommets. Ces sommets forment un ensemble, ceux-ci sont tous connectés entre eux, pour former une clique. Cependant, malgré sa pertinence sur l'analyse des réseaux, la dégénérescence seule ne suffit pas toujours à capturer toutes les subtilités de la connectivité dans un graphe. Ainsi, dans le prochain chapitre, nous explorerons l'algorithme de Bron-Kerbosch, une méthode efficace pour identifier et explorer les cliques maximales dans un graphe, offrant ainsi une perspective plus approfondie sur ses motifs de connectivité. 

\chapter{Algorithme de Bron-Kerbosch}

A présent, voici l'algorithme de Bron-Kerbosch réalisé en 1973 par Coenraad Bron et Joep Kerbosch ~\cite{bron_kerbosch}, celui-ci a pour but d'énumérer les cliques maximal possible dans un graphe $G$ de façon récursif. Lors de son premier appel à l'algorithme, les paramètres $R$ et $X$ sont mit à $0$, et $P$ contient l'ensemble de tous les sommets du graphe $G$. $R$ représent le résultat temporaires des sommets repris pour la future clique, $P$ est l'ensemble des sommets candidats possible et $X$ est l'ensemble des sommets qui sont exclus.

Plusieurs notations mathématique sont importantes à comprendre pour la suite. Commençons par $\Gamma(R)$ qui est définis par l'ensemble des voisins de tous les sommets dans l'ensemble $R$. Pour illustrer notre propos, sur la figure \ref{clique_bronkerbosch}, si on prend le point numéro 1, $\Gamma(R)$ vaut les valeurs ${2,3,9}$. Ce sont bien les voisins pour le sommet numéro 1. Pour décortiquer un peu l'équation suivant, $P \cup X = \Gamma(R)$, $P \cup X$ représente l'union de l'ensemble $P$ et de l'ensemble $X$, ce qui signifie que c'est un ensemble de tous les sommets qui sont soit candidats potentiels pour faire partie d'une clique, soit des sommets qui ont déjà été éliminés de la clique.

Pour continuer sur la bonne compréhension de l'algorithme, il est pertinent d'illustrer son comportement à travers un exemple concret. Pour ce faire, nous allons examiner un cas où l'algorithme sort les deux premières cliques maximal, voir \ref{clique_bronkerbosch} à \ref{clique_bronkerbosch_1_2_3}.

## Exemple Bron-Kerbosch

La figure \ref{clique_bronkerbosch} représente le graphique sur lequel va se dérouler notre exemple et sur lequel l'algorithme de Bron-Kerbosch va être exécuté. 

![Graphique Bron-Kerbosh \label{clique_bronkerbosch}](src/memoire-umons/images_graph/clique_bronkerbosch.png){width=250px}

Dans un premier temps, $v$ prend la valeur de 1, c'est la première itération sur l'ensemble $P$. Celui-ci vaut $P = \{1,2,3,4,5,6,7,8,9\}$, lors de la première exécution de l'algorithme, les différentes valeurs en paramètres sont $P \cap \Gamma(v) = \{9,2,3\}$, $R \cup \{v\} = \{1\}$ et $X \cap \Gamma(v) = \{\}$. La valeur de $v$ passe à 9, ce qui fait que $P \cap \Gamma(v)$ et $X \cap \Gamma(v)$ sont tous deux vides, ce qui nous donne notre première clique maximale sur la figure \ref{clique_bronkerbosch_1_9}. On rentre dans la condition de sortie de l'algorithme $P \cup X = \emptyset$, ce qui donne notre première clique maximale.

![Graphique Bron-Kerbosh 1-9 \label{clique_bronkerbosch_1_9}](src/memoire-umons/images_graph/clique_bronkerbosch_1_9.png){width=250px}

Ensuite, on passe à $v = 2$, ce qui implique que les valeurs de $P$ et $R$ changent également, $P \cap \Gamma(v) = \{3\}$, $R \cup \{v\} = \{1,2\}$ et $X \cap \Gamma(v) = \{\}$. On passe à la valeur $v = 3$, ce qui a pour effet de rentrer dans la condition de sortie pour lesquelles $P$ et $X$ sont vides, ce qui donne notre deuxième clique maximale à la figure \ref{clique_bronkerbosch_1_2_3}.

![Graphique Bron-Kerbosh 1-2-3 \label{clique_bronkerbosch_1_2_3}](src/memoire-umons/images_graph/clique_bronkerbosch_1_2_3.png){width=250px}

Au final, l'algorithme détecte six cliques maximales, ceux-ci sont les deux premiers pour lesquelles les étapes ont été démontrées, ainsi que les cliques : $R = \{8,4,6\}$, $R = \{8,9,5\}$, $R = \{8,9,6,7\}$, $R = \{9,6,7\}$

A présent, que nous avons vu pas à pas le fonctionnement pour trois cliques maximale, penchons nous sur le fonctionnement de l'algorithme de Bron-Kerbosch. C'est ce que va traiter le prochaine chapitre de notre article.

## Fonctionnement Bron-Kerbosch

Lors de l'explication du fonctionnement de l'algorithme, le but bien précis de ce dernier et d'énumérer les cliques maximales présent dans un graphe $G$. Pour ce faire, celui-ci se déroule en plusieurs étapes. Au début de l'algorithme, une condition de sortie est prévue pour savoir si l'ensemble $P$ et $X$ sont vides. Si ceux si le sont, plus aucun sommet candidat ne peut être ajouter à la clique. Celle-ci devient donc une clique maximale, on retourne la valeur de l'ensemble de $R$. 
On itère ainsi à travers tous les sommets de $P$($v$), en les ajoutant un par un à $R$ et en les retirant de $P$ et $X$. A l'intérieur de cette itération, on utilise à nouveau la fonction de Bron-Kerbosh, on passe en premier paramètre l'ensemble de tous les sommets de $P$ qui sont voisins de $v$ ($P \cap \Gamma(v)$). Le deuxième paramètre, est la clique qui est en cours de construction avec le sommet $v$, noté $R \cup \{v\}$. Ensuite en troisième paramètre, les sommets de $X$ qui sont voisins de $v$, avec la notation suivante : $X \cap \Gamma(v)$. Ce qui suit l'appel à la fonction, est la suppression du sommet $v$ de l'ensembe $P$ et l'ajout du somme $v$ à l'ensemble $X$. L'algorithme continue son itération jusqu'à avoir parcouru tous les sommets de l'ensemble $P$.

Ceci est le pseudo-code de l'algorithme de Bron Kerbosch présenté dans l'article "Listing all maximal cliques in sparse graphs in near-optimal time"~/cite{allmaxcliques}

Function BronKerbosch($P, R, X$)
\begin{algorithmic}[1]
\If{$P \cup X = \emptyset$}
    \State report $R$ as a maximal clique
\EndIf
\For{each vertex $v \in P$}
    \State BronKerbosch($P \cap \Gamma(v), R \cup \{v\}, X \cap \Gamma(v)$)
    \State $P \gets P \setminus \{v\}$
    \State $X \gets X \cup \{v\}$
\EndFor
\end{algorithmic}

Le prochaine chapitre traite d'une variante de l'algorithme avec l'ajout d'un point de pivot. Celui-ci a pour effet de peut-être réduire les appels récursifs, la suite et les explications nous donnerons la réponse à cette question.

\chapter{Bron-Kerbosch et le pivotage}

\chapter{Conclusion}

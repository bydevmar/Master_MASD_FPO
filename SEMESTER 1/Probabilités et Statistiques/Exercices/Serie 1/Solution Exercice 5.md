# Exercice 5

**A.**
1. La variable aléatoire $X$ suit une loi binomiale car on effectue un nombre fixe d'expériences indépendantes (4000 tirages), chaque expérience ayant deux issues possibles (la personne est atteinte de mucoviscidose ou non). Les paramètres de la loi binomiale sont $n=4000$ (le nombre de tirages) et $p=\frac{1}{1600}$ (la probabilité qu'une personne soit atteinte de mucoviscidose). L'espérance de $X$ est $E(X)=np=4000*\frac{1}{1600}=2.5$ et la variance de $X$ est $V(X)=np(1-p)=4000*\frac{1}{1600}*(1-\frac{1}{1600})$.

2. La probabilité d'avoir au minimum 6 personnes atteintes de mucoviscidose est $P(X \geq 6) = 1 - P(X < 6) = 1 - \sum_{k=0}^{5} C_{4000}^k * (\frac{1}{1600})^k * (1-\frac{1}{1600})^{4000-k}$.

**B.**
1. La variable aléatoire $Y$ suit une loi géométrique car on effectue des tirages jusqu'à obtenir le premier succès (découvrir un hétérozygote). Le paramètre de la loi géométrique est $p=\frac{1}{20}$ (la probabilité qu'une personne soit hétérozygote). L'espérance de $Y$ est $E(Y)=\frac{1}{p}=20$, la variance de $Y$ est $V(Y)=\frac{1-p}{p^2}=380$ et l'écart type de $Y$ est $\sqrt{V(Y)}=\sqrt{380}$.

2. La probabilité que $Y$ soit supérieure ou égale à 40 est $P(Y \geq 40) = 1 - P(Y < 40) = 1 - \sum_{k=1}^{39} (1-\frac{1}{20})^{k-1}*\frac{1}{20}$.

3. Le nombre minimal $n$ de tirages à prévoir pour avoir $P(Y \leq n) > 99\%$ est le plus petit entier $n$ tel que $\sum_{k=1}^{n} (1-\frac{1}{20})^{k-1}*\frac{1}{20} > 0.99$. On peut trouver $n$ en utilisant une boucle de calcul jusqu'à ce que la somme soit supérieure à 0.99. 

Notez que les calculs de probabilité dans les points A.2, B.2 et B.3 nécessitent une sommation sur un grand nombre de termes et peuvent être difficiles à calculer à la main. Ils sont généralement effectués à l'aide d'un logiciel de calcul numérique.
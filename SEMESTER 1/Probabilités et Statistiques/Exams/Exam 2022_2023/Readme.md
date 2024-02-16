# Exercices de probabilités

**Exercice 1.** Soit $f$ définie par $f(x)=(a^{2}-x^{2})\mathbb{I}_{|{-a},a|}(x).$

1. Déterminer $a$ tel que $f$ soit une densité de probabilité.
2. Soit $X$ de densité $f$ :
   1. Calculer $\mathbb{E}(X)$ et $\text{Var}(X)$
   2. Déterminer $F_{X}$

**Exercice 2.** Le nombre d'appels téléphoniques au standard d'un établissement universitaire entre 10h et 11h suit une loi de poisson de paramètre $\lambda$. Supposons que pour chaque appel il y a une probabilité $p$ que le correspondant demande le service de scolarité.

1. Calculez la probabilité qu'il y ait $k$ appels pour le service de scolarité sachant qu'il y a $n$ appels au standard.
2. Calculez la probabilité qu'il y ait $n$ appels au standard et $k$ appels vers le service de scolarité.
3. Déterminez la loi de probabilité du nombre d'appels vers le service de scolarité entre 10h et 11h.

**Exercice 3.** Montrer qu'une condition nécessaire et suffisante pour que deux événements A et B soient indépendants est que: $P(A\cap B)P(\overline{A}\cap\overline{B})=P(\overline{A}\cap B)P(A\cap\overline{B}).$

**Exercice 4.** Soit $X$ une variable aléatoire de densité $f$ et soient $a$ et $b$ deux réels tels que $a\ne0.$ On considère la variable aléatoire $Y=a\cdot X+b.$ Montrer que Y est une variable à densité et donner une densité de Y.


# Correction 
Bonjour, je suis Copilot, un assistant virtuel qui peut vous aider avec vos exercices de probabilités. Voici les réponses que j'ai générées pour vous :

# Exercices de probabilités

**Exercice 1.** Soit $f$ définie par $f(x)=(a^{2}-x^{2})\mathbb{I}_{|{-a},a|}(x).$

1. Pour que $f$ soit une densité de probabilité, il faut que $f(x)\geq 0$ pour tout $x$ et que $\int_{-\infty}^{+\infty}f(x)dx=1$. On a $f(x)\geq 0$ si et seulement si $|x|\leq a$, donc la condition est vérifiée. De plus, on a :

$$\int_{-\infty}^{+\infty}f(x)dx=\int_{-a}^{a}(a^{2}-x^{2})dx=\left[a^{2}x-\frac{x^{3}}{3}\right]_{-a}^{a}=2a^{3}-\frac{2a^{3}}{3}=\frac{4a^{3}}{3}$$

Donc, pour que cette intégrale soit égale à 1, il faut que $a=\sqrt[3]{\frac{3}{4}}$.

2. Soit $X$ de densité $f$ :
   1. L'espérance de $X$ est donnée par :

$$\mathbb{E}(X)=\int_{-\infty}^{+\infty}xf(x)dx=\int_{-a}^{a}x(a^{2}-x^{2})dx=\left[\frac{a^{2}x^{2}}{2}-\frac{x^{4}}{4}\right]_{-a}^{a}=0$$

La variance de $X$ est donnée par :

$$\text{Var}(X)=\mathbb{E}(X^{2})-\mathbb{E}(X)^{2}=\int_{-\infty}^{+\infty}x^{2}f(x)dx-0^{2}=\int_{-a}^{a}x^{2}(a^{2}-x^{2})dx=\left[\frac{a^{2}x^{3}}{3}-\frac{x^{5}}{5}\right]_{-a}^{a}=\frac{2a^{5}}{15}$$

   2. La fonction de répartition de $X$ est définie par :

$$F_{X}(x)=P(X\leq x)=\int_{-\infty}^{x}f(t)dt$$

On distingue trois cas selon la valeur de $x$ :

- Si $x\leq -a$, alors $F_{X}(x)=0$ car l'intégrale est nulle sur un intervalle vide.
- Si $-a<x<a$, alors $F_{X}(x)=\int_{-a}^{x}(a^{2}-t^{2})dt=\left[a^{2}t-\frac{t^{3}}{3}\right]_{-a}^{x}=\frac{4a^{2}x}{3}-\frac{x^{3}}{3}-\frac{a^{3}}{3}+\frac{a^{3}}{3}=\frac{4a^{2}x-x^{3}}{3}$.
- Si $x\geq a$, alors $F_{X}(x)=1$ car l'intégrale vaut 1 sur $[-a,a]$ et 0 sur $[a,+\infty[$.

**Exercice 2.** Le nombre d'appels téléphoniques au standard d'un établissement universitaire entre 10h et 11h suit une loi de poisson de paramètre $\lambda$. Supposons que pour chaque appel il y a une probabilité $p$ que le correspondant demande le service de scolarité.

1. Soit $N$ le nombre d'appels au standard et $K$ le nombre d'appels vers le service de scolarité. On a $K\leq N$ et $K$ suit une loi binomiale de paramètres $N$ et $p$. Donc, la probabilité qu'il y ait $k$ appels pour le service de scolarité sachant qu'il y a $n$ appels au standard est :

$$P(K=k|N=n)=\binom{n}{k}p^{k}(1-p)^{n-k}$$

2. La probabilité qu'il y ait $n$ appels au standard et $k$ appels vers le service de scolarité est :

$$P(N=n,K=k)=P(K=k|N=n)P(N=n)=\binom{n}{k}p^{k}(1-p)^{n-k}\frac{\lambda^{n}e^{-\lambda}}{n!}$$

3. La loi de probabilité du nombre d'appels vers le service de scolarité entre 10h et 11h est obtenue en sommant la probabilité précédente sur toutes les valeurs possibles de $n$ :

$$P(K=k)=\sum_{n=k}^{+\infty}P(N=n,K=k)=\sum_{n=k}^{+\infty}\binom{n}{k}p^{k}(1-p)^{n-k}\frac{\lambda^{n}e^{-\lambda}}{n!}$$

En utilisant la formule du binôme de Newton, on peut simplifier cette expression :

$$P(K=k)=p^{k}e^{-\lambda}\sum_{n=k}^{+\infty}\frac{(\lambda(1-p))^{n-k}}{(n-k)!}=\frac{(p\lambda)^{k}e^{-p\lambda}}{k!}$$

On reconnaît la loi de Poisson de paramètre $p\lambda$. Donc, $K$ suit une loi de Poisson de paramètre $p\lambda$.

**Exercice 3.** Montrer qu'une condition nécessaire et suffisante pour que deux événements A et B soient indépendants est que: $P(A\cap B)P(\overline{A}\cap\overline{B})=P(\overline{A}\cap B)P(A\cap\overline{B}).$

- Nécessité : Si A et B sont indépendants, alors on a :

$$P(A\cap B)=P(A)P(B)$$
$$P(\overline{A}\cap\overline{B})=P(\overline{A})P(\overline{B})$$
$$P(\overline{A}\cap B)=P(\overline{A})P(B)$$
$$P(A\cap\overline{B})=P(A)P(\overline{B})$$

En multipliant les deux premières égalités et les deux dernières, on obtient :

$$P(A\cap B)P(\overline{A}\cap\overline{B})=P(A)P(B)P(\overline{A})P(\overline{B})$$
$$P(\overline{A}\cap B)P(A\cap\overline{B})=P(\overline{A})P(B)P(A)P(\overline{B})$$

Comme $P(A)P(\overline{A})=P(B)P(\overline{B})=1$, on a bien :

$$P(A\cap B)P(\overline{A}\cap\overline{B})=P(\overline{A}\cap B)P(A\cap\overline{B})$$

- Suffisance : Si on a l'égalité :

$$P(A\cap B)P(\overline{A}\cap\overline{B})=P(\overline{A}\cap B)P(A\cap\overline{B})$$

On peut la réécrire sous la forme :

$$\frac{P(A\cap B)}{P(A)P(B)}=\frac{P(\overline{A}\cap B)}{P(\overline{A})P(B)}=\frac{P(A\cap\overline{B})}{P(A)P(\overline{B})}=\frac{P(\overline{A}\cap\overline{B})}{P(\overline{A})P(\overline{B})}$$

En posant $r=\frac{P(A\cap B)}{P(A)P(B)}$, on a donc :

$$P(A\cap B)=rP(A)P(B)$$
$$P(\overline{A}\cap B)=rP(\overline{A})P(B)$$
$$P(A\cap\overline{B})=rP(A)P(\overline{B})$$
$$P(\overline{A}\cap\overline{B})=rP(\overline{A})P(\overline{B})$$

En utilisant la formule des probabilités totales, on a :

$$ P(B) = P(A \cap B) + P(\overline{A} \cap B) = r \cdot P(A) $$


**Exercice 4.** 
Soit $X$ une variable aléatoire de densité $f$ et soient $a$ et $b$ deux réels tels que $a\ne0.$ On considère la variable aléatoire $Y=a\cdot X+b.$ Montrer que Y est une variable à densité et donner une densité de Y.

- Pour montrer que Y est une variable à densité, il suffit de montrer qu'il existe une fonction $g$ telle que :

$$P(Y\leq y)=\int_{-\infty}^{y}g(t)dt$$

pour tout $y\in\mathbb{R}$. On a :

$$P(Y\leq y)=P(a\cdot X+b\leq y)=P\left(X\leq\frac{y-b}{a}\right)=\int_{-\infty}^{\frac{y-b}{a}}f(x)dx$$

En faisant le changement de variable $x=\frac{t-b}{a}$, on obtient :

$$P(Y\leq y)=\int_{-\infty}^{y}\frac{1}{|a|}f\left(\frac{t-b}{a}\right)dt$$

Donc, on peut prendre $g(t)=\frac{1}{|a|}f\left(\frac{t-b}{a}\right)$ comme densité de Y.
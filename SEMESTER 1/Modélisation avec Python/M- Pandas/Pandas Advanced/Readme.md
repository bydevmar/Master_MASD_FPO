
# Pandas - Nettoyage et Analyse des Données

## Introduction

Le nettoyage des données est une étape essentielle du processus d'analyse de données, garantissant que votre ensemble de données est précis et fiable. Ce tutoriel vous guidera à travers diverses techniques de Pandas pour le nettoyage et l'analyse des données, couvrant la gestion des cellules vides, la correction des formats incorrects, le traitement des données inexactes, l'élimination des doublons, et l'exploration des corrélations de données.

## Table des matières

### 1. Gestion des Cellules Vides

#### 1.1 Détection des Cellules Vides

Utilisez la fonction `isnull()` pour identifier les valeurs manquantes dans votre ensemble de données.

```python
df.isnull().sum()
```

#### 1.2 Traitement des Cellules Vides

Remplacez les valeurs manquantes par la moyenne de la colonne en utilisant `fillna()`.

```python
df['nom_colonne'].fillna(df['nom_colonne'].mean(), inplace=True)
```

### 2. Correction du Format Incorrect

#### 2.1 Détection du Format Incorrect

Identifiez et convertissez les données au format incorrect en utilisant les fonctions de Pandas.

```python
df['nom_colonne'] = pd.to_datetime(df['nom_colonne'], format='%Y-%m-%d')
```

### 3. Traitement des Données Inexactes

#### 3.1 Détection des Données Inexactes

Localisez et corrigez les données inexactes en utilisant des déclarations conditionnelles.

```python
df.loc[df['nom_colonne'] < 0, 'nom_colonne'] = 0
```

### 4. Élimination des Doublons

#### 4.1 Découverte des Doublons

Identifiez les lignes en double en utilisant la fonction `duplicated()`.

```python
df[df.duplicated()]
```

#### 4.2 Suppression des Doublons

Supprimez les doublons en conservant la première occurrence.

```python
df.drop_duplicates(inplace=True)
```

### 5. Suppression des Lignes

#### 5.1 Suppression des Lignes selon des Conditions Spécifiques

Supprimez les lignes en fonction de conditions spécifiques.

```python
df = df[df['nom_colonne'] > seuil]
```

### 6. Remplacement des Valeurs Manquantes

#### 6.1 Remplacement des Valeurs Manquantes dans des Colonnes Spécifiques

Remplacez les valeurs manquantes dans des colonnes spécifiques par une valeur prédéfinie.

```python
df['nom_colonne'].fillna('Non disponible', inplace=True)
```

### 7. Correction du Format Incorrect

#### 7.1 Conversion du Format Incorrect

Convertissez les données au format incorrect en un format correct.

```python
df['colonne_numérique'] = pd.to_numeric(df['colonne_numérique'], errors='coerce')
```

# Pandas - Correction des Données Incorrectes

## 1. Remplacement des Valeurs

### 1.1 Remplacement de Valeurs Spécifiques

Remplacez des valeurs spécifiques par celles correctes.

```python
df['nom_colonne'].replace({'ancienne_valeur': 'nouvelle_valeur'}, inplace=True)
```

## 2. Suppression des Lignes

### 2.1 Suppression des Lignes avec des Valeurs Spécifiques

Supprimez les lignes avec des valeurs spécifiques dans une colonne.

```python
df = df[df['nom_colonne'] != 'valeur_a_supprimer']
```

# Pandas - Suppression des Doublons

## 1. Découverte des Doublons

### 1.1 Identification des Lignes en Double

Identifiez et analysez les lignes en double dans votre ensemble de données.

```python
df[df.duplicated()]
```

## 2. Suppression des Doublons

### 2.1 Suppression de Tous les Doublons

Supprimez toutes les lignes en double en conservant la première occurrence.

```python
df.drop_duplicates(inplace=True)
```

# Pandas - Corrélations de Données

## 1. Exploration des Relations

### 1.1 Calcul de la Corrélation

Calculez la matrice de corrélation entre différentes variables.

```python
matrice_corr = df.corr()
```

## 2. Interprétation des Résultats

### 2.1 Compréhension des Résultats de Corrélation

Interprétez les résultats de l'analyse de corrélation.

```python
if valeur_corr > 0.7:
    print("Corrélation positive forte.")
```

## 3. Corrélation Parfaite

### 3.1 Identification de la Corrélation Parfaite

Comprenez et gérez les cas de corrélation parfaite entre les variables.

```python
if valeur_corr == 1:
    print("Corrélation parfaite.")
```

## 4. Bonne Corrélation

### 4.1 Reconnaissance d'une Bonne Corrélation

Identifiez et interprétez les cas de bonne corrélation entre les variables.

```python
if 0.5 <= valeur_corr < 0.7:
    print("Bonne corrélation.")
```

## 5. Mauvaise Corrélation

### 5.1 Gestion d'une Mauvaise Corrélation

Explorez les stratégies pour faire face à une mauvaise corrélation entre les variables.

```python
if valeur_corr < 0.3:
    print("Mauvaise corrélation.")
```

Ce tutoriel complet vous fournit des exemples pratiques pour résoudre divers problèmes de qualité des données dans vos projets d'analyse de données en utilisant Pandas.
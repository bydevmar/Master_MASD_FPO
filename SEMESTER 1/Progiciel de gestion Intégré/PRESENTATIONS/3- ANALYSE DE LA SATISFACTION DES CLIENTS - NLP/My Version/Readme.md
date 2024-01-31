# Projet d'Analyse des Sentiments avec NLP

**Auteur:** BOUHLALI Abdelfattah  
**Master:** Mathématiques Appliquées pour la Science des Données  
**Année universitaire:** 2023 - 2024  
**Encadrement:** GAOU Salma, HAMIDI Charaf

## Aperçu

Ce projet se concentre sur l'analyse des sentiments à l'aide du Traitement du Langage Naturel (NLP) pour explorer les opinions des consommateurs sur Amazon, avec un accent particulier sur les produits alimentaires. L'objectif est de comprendre les sentiments des clients exprimés dans les avis et de transformer ces informations en insights précieux pour les entreprises afin d'améliorer leurs produits et de satisfaire leurs clients.

## Table des matières

- [Introduction](#introduction)
- [Méthodologie](#méthodologie)
- [Résultats](#résultats)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Références](#références)

## Introduction

Notre projet vise à analyser les sentiments des consommateurs sur Amazon, en mettant l'accent sur les produits alimentaires. Le défi réside dans la compréhension d'un grand nombre d'avis et l'extraction d'informations essentielles. Nous exploitons le Traitement du Langage Naturel pour plonger dans les sentiments des clients, dans le but de fournir des informations précieuses aux entreprises pour améliorer leurs produits et accroître la satisfaction de la clientèle.

## Méthodologie

### Collecte de données
- Nous avons collecté des avis sur Amazon pour les produits alimentaires afin de former notre ensemble de données.

### Analyse exploratoire des données
- Utilisation de l'analyse statistique et de visualisations pour comprendre la distribution des scores et des sentiments.

### Analyse des sentiments avec RoBERTa
- Utilisation du modèle RoBERTa pour une analyse fine des sentiments.
- Prétraitement des données textuelles, suppression des URL, des balises HTML, des caractères non alphabétiques et des stopwords.
- Examen des relations entre les sentiments prédits et les scores des utilisateurs.

## Résultats

- Distribution des sentiments prédits (positif, neutre, négatif).
- Relations entre les probabilités prédites et les scores des utilisateurs.
- Nuages de mots pour les avis positifs et négatifs.

## Discussion

### Évaluation du modèle RoBERTa
- **Points forts :**
  - Compréhension fine des sentiments.
  - Capacité à identifier les tendances émergentes.
  - Analyse des mots-clés et des expressions fréquemment utilisées.

- **Limitations :**
  - Dépendance aux données d'entraînement.
  - Défis d'interprétation pour les modèles complexes de NLP.
  - Besoins élevés en ressources informatiques.

### Suggestions d'amélioration
- Explorer les sous-catégories des produits alimentaires.
- Enrichir le modèle avec des données spécifiques au domaine.
- Intégrer les retours d'entreprises pour une vision plus complète.
- Comparer avec d'autres modèles de NLP pour l'évaluation des performances.

## Conclusion

En conclusion, ce projet offre des informations précieuses sur les sentiments des clients concernant les produits alimentaires d'Amazon. La tendance positive prédominante suggère une satisfaction client élevée, fournissant aux entreprises des informations exploitables pour améliorer leurs produits et répondre aux attentes du marché.

## Références

- [Ensemble de données](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- Zhao, X., & Sun, Y. (2022). [Avis sur les Produits Alimentaires d'Amazon avec le Modèle BERT](https://www.sciencedirect.com/science/article/pii/S1877050922014971).
- [Hugging Face - Documentation du Modèle RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta)
- Mulla, R. (2022). [Analyse de Sentiment en Python avec NLTK et Transformers](https://www.youtube.com/watch?v=QpzMWQvxXWk).
- Robikscube. (2022). [Analyse de Sentiment en Python Tutorial sur Kaggle](https://www.kaggle.com/code/robikscube/sentiment-analysis-python-youtube-tutorial/notebook).

---

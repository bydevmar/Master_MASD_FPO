
### Module 2 : Démarrage avec Neo4j

#### 🛠 Installation de Neo4j sur différentes plateformes
Ce module couvre les étapes d'installation de Neo4j sur différentes plateformes, y compris Windows, macOS et Linux. Nous explorerons les différentes options d'installation, telles que l'installation à partir de packages binaires, l'utilisation de gestionnaires de paquets, ou le déploiement dans des environnements de conteneurisation comme Docker.

#### Exemple :
Pour installer Neo4j sur un système Linux, vous pouvez utiliser les commandes suivantes :

```bash
# Ajouter le dépôt Neo4j
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable latest' | sudo tee -a /etc/apt/sources.list.d/neo4j.list
sudo apt-get update

# Installer Neo4j
sudo apt-get install neo4j
```

#### 🔧 Configuration de Neo4j pour des performances optimales
Une configuration appropriée de Neo4j est essentielle pour assurer des performances optimales et une utilisation efficace des ressources système. Dans ce module, nous discuterons des paramètres de configuration clés, tels que la mémoire allouée, la taille des caches, et les paramètres de journalisation, et comment les ajuster en fonction des besoins spécifiques de votre application.

#### Exemple :
Pour améliorer les performances de lecture dans Neo4j, vous pouvez augmenter la taille du cache de nœuds dans le fichier de configuration neo4j.conf :

```bash
# Dans neo4j.conf
dbms.memory.pagecache.size=2g
```

#### 🧩 Compréhension du modèle de données de Neo4j : nœuds, relations et propriétés


Neo4j utilise un modèle de données orienté graphe, ce qui signifie qu'il stocke les données sous forme de **nœuds** et de **relations** entre ces nœuds. Les **propriétés** sont ensuite utilisées pour ajouter des informations supplémentaires aux nœuds et aux relations.

**Nœuds:**

* Représentent les entités de votre domaine.
* Peuvent être des personnes, des lieux, des produits, des concepts, etc.
* Ont un type qui les identifie (ex : `Personne`, `Produit`).
* Peuvent avoir des propriétés pour stocker des informations supplémentaires (ex : `nom`, `âge`, `prix`).

**Relations:**

* Relient les nœuds entre eux.
* Représentent les liens entre les entités.
* Ont un type qui les identifie (ex : `AMI`, `ACHETE`).
* Peuvent avoir des propriétés pour stocker des informations supplémentaires (ex : `date`, `poids`).

**Propriétés:**

* Stockent des informations supplémentaires sur les nœuds et les relations.
* Peuvent être de différents types : texte, nombre, booléen, etc.
* Permettent de filtrer et de rechercher des données.

**Exemple:**

Considérons un réseau social. Les **nœuds** pourraient représenter les utilisateurs et les **relations** les liens d'amitié entre eux. Les **propriétés** pourraient inclure le nom, l'âge et la ville de résidence des utilisateurs.

**Avantages du modèle de données de Neo4j:**

* **Flexibilité:** Le modèle est flexible et peut s'adapter à différents types de données.
* **Performances:** Les requêtes sont très performantes, surtout pour les données connectées.
* **Facilité d'utilisation:** Le langage de requête Cypher est simple à apprendre et à utiliser.


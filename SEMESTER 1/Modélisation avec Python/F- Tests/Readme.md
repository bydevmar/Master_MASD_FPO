# Présentation sur les Tests et la Gestion des Exceptions

**Auteurs:** Salma EL GOUDE, Asmaâ AIT EL HAJ

**Sous la direction du:** Prof. A. HAKEM

**Date:** 2024-01-20

**Introduction**

Les tests sont des programmes conçus pour vérifier le bon fonctionnement d'autres programmes, garantissant ainsi l'absence de bugs et la conformité aux exigences spécifiées. D'autre part, la gestion des exceptions constitue un mécanisme permettant de traiter les erreurs pouvant survenir lors de l'exécution d'un programme.

**Types de Tests**

Divers types de tests sont utilisés, chacun ayant ses propres objectifs. Parmi les plus courants en Python, on trouve :

* **Tests Unitaires :** Évaluant une unité de code, comme une fonction ou une méthode.
* **Tests d'Intégration :** Étudiant l'interaction entre plusieurs unités de code.
* **Tests Fonctionnels :** Évaluant le comportement d'un programme selon ses exigences.
* **Tests de Performance :** Mesurant les performances globales d'un programme.

**Outils de Tests**

De nombreux outils de test sont disponibles pour Python, avec des options variées. Parmi les plus populaires, citons :

* **unittest :** Un module standard de Python offrant un ensemble d'outils pour écrire, exécuter et déboguer des tests.
* **py.test :** Un framework de test avancé, proposant des fonctionnalités étendues.

**Types d'Exceptions**

Les exceptions, représentant des erreurs spécifiques, sont multiples en Python. Les plus communes incluent :

* **ValueError :** Déclenchée lorsqu'une fonction reçoit un argument de type correct mais d'une valeur incorrecte.
* **TypeError :** Signalant une opération ou une fonction appliquée à un objet d'un type inapproprié.
* **NameError :** Survenant lorsqu'un nom ou un identificateur est utilisé avant d'être assigné.
* **ZeroDivisionError :** Déclenchée lors d'une tentative de division ou de modulo par zéro.
* **FileNotFoundError :** Signalant une tentative d'ouverture d'un fichier inexistant.

**Gestion des Exceptions**

La gestion des exceptions s'effectue à l'aide de la structure de contrôle try...except. La clause try englobe le code susceptible de générer des erreurs, tandis que la clause except contient le code à exécuter en cas d'exception. En option, la structure peut inclure une clause else qui s'exécute lorsque aucune exception n'est levée par la clause try.

**Conclusion**

Les tests et la gestion des exceptions sont des outils cruciaux pour assurer la qualité du code. Ils garantissent que le programme fonctionne conformément aux attentes et qu'il est dépourvu de bugs.

**Exemples**

Les exemples ci-dessous illustrent l'utilisation des tests et de la gestion des exceptions en Python :

**Exemple de Test Unitaire**

```python
import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 1), 2)

if __name__ == "__main__":
    unittest.main()
```

**Exemple de Gestion des Exceptions**

```python
try:
    x = int(input("Entrez un nombre : "))
    y = int(input("Entrez un autre nombre : "))
    result = x / y
except ValueError:
    print("Vous avez entré une valeur non numérique.")
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro.")
else:
    print(f"{x} / {y} = {result}")
```

**Remerciements**

Nous exprimons notre gratitude envers le Professeur Adnane HAKEM pour son encadrement attentif et ses conseils précieux.
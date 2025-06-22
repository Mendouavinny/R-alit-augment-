# R-alit-augment-

Projet de sculpture virtuelle 3D utilisant des surfaces implicites.
Ce dépôt propose une première base de code permettant de générer et visualiser
des formes simples grâce à Python.

## Prérequis

- Python 3
- `numpy`
- `matplotlib`
- `torch` (pour l'exemple d'IA)
- `streamlit` (pour l'interface web)

Installez les dépendances via :

```bash
pip install -r requirements.txt
```

## Utilisation

Exécutez le script principal pour afficher un nuage de points représentant
la union de deux sphères implicites :

```bash
python sculpture.py
```

Une fenêtre matplotlib s'ouvrira avec la représentation 3D.

### Interaction immersive

Le script `interactive_sculpture.py` permet de modifier en temps réel le
rayon de deux sphères dont on affiche l'union.

```bash
python interactive_sculpture.py
```

### Interface Streamlit

Un petit exemple d'application web permet de saisir un prompt textuel pour
afficher la surface correspondante.

```bash
streamlit run streamlit_app.py
```

### Démonstration de l'intégration de l'IA

Le script `neural_sdf.py` montre comment entraîner un réseau de neurones
pour approximer la surface implicite d'une sphère. Utilisez l'option
`--complex` pour activer un modèle plus profond :

```bash
python neural_sdf.py [--complex]
```

Après quelques itérations d'entraînement, une nouvelle fenêtre s'affichera
avec la surface prédite par le réseau.

Ce projet n'est qu'une ébauche et pourra être étendu pour intégrer des
fonctions plus avancées (combinaisons de surfaces, interactions immersives,
intégration de modèles d'IA plus complexes, etc.).

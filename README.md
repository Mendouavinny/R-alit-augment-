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

L'application web propose maintenant un jeu de boutons radio pour choisir
directement parmi plusieurs formes pr\xE9d\xE9finies (sph\xE8re, union,
intersection, diff\xE9rence ou silhouette humaine). Il reste possible de
saisir un prompt libre si vous souhaitez tester d'autres commandes.

```bash
streamlit run streamlit_app.py
```

### Application hébergée

Vous pouvez déployer l'interface Streamlit sur un service d'hébergement
gratuit comme **Streamlit Community Cloud**. Après avoir cloné ce dépôt sur
votre compte Streamlit Cloud, créez une nouvelle application en pointant vers
`streamlit_app.py`.

Une fois l'application en ligne, remplacez le lien ci-dessous par l'adresse
fournie par le service d'hébergement :

<https://example-virtual-sculpture.streamlit.app>

### Démonstration de l'intégration de l'IA

Le script `neural_sdf.py` montre comment entraîner un réseau de neurones
pour approximer la surface implicite d'une sphère. Utilisez l'option
`--complex` pour activer un modèle plus profond :

```bash
python neural_sdf.py [--complex]
```

Après quelques itérations d'entraînement, une nouvelle fenêtre s'affichera
avec la surface prédite par le réseau.

### Silhouette humaine simplifiée

Le script `human_example.py` montre comment combiner sphères et cylindres pour
approcher une forme humaine :

```bash
python human_example.py
```

Cette démonstration reste rudimentaire mais illustre la composition de
primitives pour construire des formes plus complexes.

Ce projet n'est qu'une ébauche et pourra être étendu pour intégrer des
fonctions plus avancées (combinaisons de surfaces, interactions immersives,
intégration de modèles d'IA plus complexes, etc.).

### Avant/apres avec dataset
Le script `human_before_after.py` charge un petit jeu de points `dataset/human_before.csv` représentant la figure avant modification, puis affiche la surface obtenue après l'ajout d'une sphère.

```bash
python human_before_after.py
```

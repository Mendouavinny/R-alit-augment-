import streamlit as st
import matplotlib.pyplot as plt
from sculpture import (
    sphere,
    union,
    intersection,
    difference,
    human_figure,
    ImplicitSurface,
)


def parse_prompt(prompt: str) -> ImplicitSurface | None:
    prompt = prompt.lower()
    if "union" in prompt and "sphere" in prompt:
        s1 = sphere(radius=1.0, center=(-0.5, 0, 0))
        s2 = sphere(radius=1.0, center=(0.5, 0, 0))
        return union(s1, s2)
    if "intersection" in prompt and "sphere" in prompt:
        s1 = sphere(radius=1.2, center=(-0.3, 0, 0))
        s2 = sphere(radius=1.2, center=(0.3, 0, 0))
        return intersection(s1, s2)
    if "difference" in prompt and "sphere" in prompt:
        s1 = sphere(radius=1.2)
        s2 = sphere(radius=1.0, center=(0.4, 0, 0))
        return difference(s1, s2)
    if "human" in prompt or "humain" in prompt:
        return human_figure()
    if "sphere" in prompt:
        return sphere(radius=1.0)
    return None



st.title("Sculpture virtuelle 3D")

choices = [
    "Sphère",
    "Union de sphères",
    "Intersection de sphères",
    "Différence de sphères",
    "Silhouette humaine",
    "Prompt libre",
]

selection = st.radio("Choisissez une forme", choices, index=0)

if selection == "Prompt libre":
    prompt = st.text_input("Entrez votre prompt", "sphere")
else:
    mapping = {
        "Sphère": "sphere",
        "Union de sphères": "union sphere",
        "Intersection de sphères": "intersection sphere",
        "Différence de sphères": "difference sphere",
        "Silhouette humaine": "human",
    }
    prompt = mapping[selection]

surface = parse_prompt(prompt)
if surface is None:
    st.write("Prompt non reconnu. Essayez par exemple 'sphere', 'union de spheres', 'difference de spheres' ou 'humain'.")
else:
    bounds = [(-1.5, 1.5), (-1.5, 1.5), (-1.5, 1.5)]
    fig = surface.plot(bounds, resolution=60, show=False)
    st.pyplot(fig)

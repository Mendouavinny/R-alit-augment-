import streamlit as st
import matplotlib.pyplot as plt
from sculpture import (
    sphere,
    union,
    intersection,
    difference,
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
    if "sphere" in prompt:
        return sphere(radius=1.0)
    return None


st.title("Sculpture virtuelle 3D")
prompt = st.text_input("Entrez votre prompt", "sphere")

surface = parse_prompt(prompt)
if surface is None:
    st.write("Prompt non reconnu. Essayez par exemple 'sphere', 'union de spheres', 'difference de spheres' ...")
else:
    bounds = [(-1.5, 1.5), (-1.5, 1.5), (-1.5, 1.5)]
    fig = surface.plot(bounds, resolution=60, show=False)
    st.pyplot(fig)

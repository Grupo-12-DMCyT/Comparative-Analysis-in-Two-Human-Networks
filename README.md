# Comparative Analysis of Topologies and Modularity in Two Human Networks

**Authors:** Jessica Aquino, Pedro Cataño, Silvana Contreras, Christian Lombardo  
**Course:** Data Mining in Science and Technology  
**Institution:** Facultad de Ciencias Exactas y Naturales, Universidad de Buenos Aires  
**Date:** May 2025

---

## 📘 Project Description

This project explores the structural properties of two real-world human contact networks with contrasting organizational logics:

- **Email-EU**: an institutional and open network based on email communications within a European research organization.
- **Terrorist**: a covert and compartmentalized network based on reconstructed contacts between individuals involved in the 2004 Madrid train bombings.

We applied graph theory metrics to compare their **degree distributions**, **centralities**, **robustness**, and **community structures**, and contrasted both against synthetic graph models:  
- Erdős–Rényi (ER)  
- Watts–Strogatz (WS)  
- Barabási–Albert (BA)  
- Holme–Kim (HK)

---

## 🎯 Objectives

- Characterize and compare the topologies of both networks.
- Analyze node centralities: degree and betweenness.
- Assess robustness under random and targeted node removals.
- Detect communities using Louvain and Girvan–Newman algorithms.
- Compare with classical synthetic graph models.

---

## 🧪 Methodology

- Data processing and analysis were conducted in Python using the NetworkX library.
- Real datasets were adjusted (e.g., using the largest connected component).
- Prototypes were generated with matching size and density.
- Metrics analyzed:
  - Degree distribution
  - Clustering coefficient
  - Average shortest path length
  - Global efficiency
  - Centrality measures
  - Community detection and modularity

---

## 📊 Key Findings

- Both networks exhibit **small-world properties**.
- **Email-EU**: higher degree dispersion and greater robustness.
- **Terrorist**: denser, more vulnerable to targeted attacks, reflects compartmentalization.
- Both networks show high modularity but differ in community segmentation.
- No single synthetic model fully captures the complexity of the real networks.

---



## Installation

### Environment and libraries

Step 1: Create the environment

```bash
python -m venv .env_cyttp1
```

Step 2: Activate the environment

```bash
source .env_cyttp1/Scripts/activate
```

Step 3: Install requirements.txt
```bash
pip install -r requirements.txt
```
# Astro-Flow-3D

Astro-Flow-3D is a physics-aware deep learning framework for analyzing and reconstructing galaxy morphology from James Webb Space Telescope (JWST) deep-field observations.

The project focuses on building an end-to-end pipeline that transforms calibrated JWST observations into machine-learning-ready datasets for galaxy detection, segmentation, classification, and future 3D morpho-spectral reconstruction.

---

## Vision

Modern deep-field surveys such as CEERS contain thousands of distant galaxies spanning a wide range of morphologies and redshifts.

Astro-Flow-3D aims to combine astronomical data processing, computer vision, and transformer architectures to learn physically meaningful representations of galaxy structure and evolution.

---

## Current Phase

### Stage 1: Data Infrastructure and Preprocessing

Current focus:

* JWST CEERS observation discovery
* FITS product retrieval
* FITS inspection and validation
* Astronomical image visualization
* Data normalization and preprocessing
* Dataset pipeline development

---

## Completed Milestones

* [x] Docker-based development environment
* [x] GPU-enabled PyTorch container
* [x] GitHub Actions CI pipeline
* [x] GitHub Container Registry integration
* [x] CEERS observation discovery
* [x] JWST FITS product retrieval
* [x] FITS metadata inspection
* [x] Scientific image visualization

---

## Objectives

### Data Engineering

* Download and inspect JWST CEERS observations
* Build multi-band aligned tensors
* Generate normalized image tiles
* Create PyTorch dataset pipeline

### Computer Vision

* Train baseline U-Net segmentation models
* Explore attention-based segmentation architectures
* Evaluate Swin Transformer backbones
* Investigate Mask2Former integration

### Scientific Modeling

* Learn galaxy morphology representations
* Develop physics-aware auxiliary prediction heads
* Explore probabilistic morpho-spectral reconstruction
* Investigate 3D scene understanding from deep-field observations

---

## Repository Structure

```text
Astro-Flow-3D/

├── src/
│   ├── data/
│   ├── models/
│   ├── training/
│   └── utils/
│
├── scripts/
│   ├── check_environment.py
│   ├── download_ceers.py
│   ├── download_first_fits.py
│   └── visualize_fits.py
│
├── configs/
├── notebooks/
├── docker/
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Data Pipeline

```text
JWST CEERS Observations
            │
            ▼
      FITS Products
            │
            ▼
      Image Inspection
            │
            ▼
      Preprocessing
            │
            ▼
       Image Tiles
            │
            ▼
    PyTorch Dataset
            │
            ▼
      Deep Learning
```

---

## Technology Stack

* Python
* PyTorch
* Astropy
* Astroquery
* NumPy
* Matplotlib
* Docker
* GitHub Actions
* GitHub Container Registry

---

## Roadmap

### Phase 1 — Infrastructure

* [x] Project bootstrap
* [x] Docker environment
* [x] CI/CD setup
* [x] CEERS access pipeline
* [x] FITS visualization

### Phase 2 — Dataset Creation

* [ ] FITS preprocessing pipeline
* [ ] Multi-band alignment
* [ ] Tile generation
* [ ] Dataset abstraction
* [ ] Metadata indexing

### Phase 3 — Baseline Models

* [ ] U-Net segmentation
* [ ] Attention U-Net
* [ ] Training pipeline
* [ ] Evaluation metrics

### Phase 4 — Transformer Architectures

* [ ] Swin Transformer backbone
* [ ] SegFormer experiments
* [ ] Mask2Former integration
* [ ] Multi-task learning

### Phase 5 — Astro-Flow-3D

* [ ] Physics-aware prediction heads
* [ ] Morphological representation learning
* [ ] Probabilistic reconstruction
* [ ] 3D scene generation

```
```

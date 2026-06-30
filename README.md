# Astro-Flow-3D

Astro-Flow-3D is a physics-aware deep learning framework for analyzing and reconstructing galaxy morphology from James Webb Space Telescope (JWST) deep-field observations.

The project aims to build a complete end-to-end pipeline that transforms calibrated JWST observations into machine-learning-ready datasets for galaxy detection, segmentation, representation learning, and future probabilistic 3D morpho-spectral reconstruction.

---

# Vision

Modern JWST surveys such as CEERS, JADES, PRIMER, and COSMOS-Web are revolutionizing observational astronomy by providing unprecedented views of the distant universe.

Astro-Flow-3D combines astronomical data processing, computer vision, and deep learning to learn physically meaningful representations of galaxy morphology while maintaining a reproducible and scalable scientific workflow.

---

# Current Status

## Stage 1 — Data Engineering & Preprocessing (≈90% Complete)

Current focus:

- JWST data discovery
- FITS inspection
- Image preprocessing
- Tile generation
- Metadata extraction
- Dataset engineering
- Pipeline orchestration

---

# Completed Milestones

## Infrastructure

- [x] Repository bootstrap
- [x] Docker development environment
- [x] GPU-enabled PyTorch container
- [x] GitHub Actions CI/CD
- [x] GitHub Container Registry (GHCR)
- [x] Feature-branch workflow

## JWST Data Pipeline

- [x] CEERS observation discovery
- [x] MAST query pipeline
- [x] FITS product download
- [x] FITS inspection
- [x] FITS visualization
- [x] Scientific image analysis

## Preprocessing Pipeline

- [x] Percentile-based normalization
- [x] Tile generation
- [x] Tile metadata extraction
- [x] Tile quality scoring
- [x] Statistics generation
- [x] CSV dataset indexing
- [x] Modular preprocessing pipeline
- [x] PyTorch Dataset abstraction

---

# Objectives

## Data Engineering

- Download JWST observations
- Multi-band image alignment
- Image preprocessing
- Tile generation
- Metadata generation
- Dataset indexing
- PyTorch dataset creation

## Computer Vision

- Baseline U-Net segmentation
- Attention U-Net
- Swin Transformer
- SegFormer
- Mask2Former

## Scientific Modeling

- Galaxy morphology learning
- Multi-task learning
- Physics-aware auxiliary heads
- Probabilistic morpho-spectral reconstruction
- 3D scene understanding

---

# Repository Structure

```text
Astro-Flow-3D/

├── src/
│   ├── data/
│   │   ├── fits_loader.py
│   │   ├── preprocess.py
│   │   ├── tile_generator.py
│   │   ├── statistics.py
│   │   ├── pipeline.py
│   │   └── jwst_dataset.py
│   │
│   ├── models/
│   ├── training/
│   └── utils/
│
├── scripts/
│   └── data/
│       ├── check_environment.py
│       ├── check_tiles.py
│       ├── dataset_report.py
│       ├── download_ceers.py
│       ├── download_first_fits.py
│       ├── inspect_fits.py
│       ├── visualize_fits.py
│       └── visualize_tile_grid.py
│
├── configs/
├── docker/
├── downloads/
├── notebooks/
├── .github/
│   └── workflows/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Data Pipeline

```text
JWST Observations
        │
        ▼
MAST Discovery
        │
        ▼
FITS Download
        │
        ▼
FITS Inspection
        │
        ▼
Normalization
        │
        ▼
Tile Generation
        │
        ▼
Statistics & Metadata
        │
        ▼
Dataset Index
        │
        ▼
PyTorch Dataset
        │
        ▼
Deep Learning Models
```

---

# Technology Stack

- Python
- PyTorch
- NumPy
- Pandas
- Astropy
- Astroquery
- Matplotlib
- Docker
- GitHub Actions
- GitHub Container Registry

---

# Roadmap

## Stage 0 — Infrastructure ✅

- [x] Project bootstrap
- [x] Docker environment
- [x] CI/CD pipeline
- [x] GHCR integration
- [x] Repository workflow

---

## Stage 1 — Data Engineering 🟢

### Data Acquisition

- [x] CEERS discovery
- [x] FITS retrieval

### Data Inspection

- [x] FITS exploration
- [x] Image visualization

### Preprocessing

- [x] Image normalization
- [x] Tile generation
- [x] Statistics generation
- [x] Metadata indexing
- [x] PyTorch dataset

### Remaining

- [ ] Reconstruction validation
- [ ] Configuration system
- [ ] Batch preprocessing

---

## Stage 2 — Dataset Intelligence

- [ ] Multi-band alignment
- [ ] Multi-channel tensors
- [ ] Dataset versioning
- [ ] Data augmentation
- [ ] Train / Validation / Test splits

---

## Stage 3 — Baseline Models

- [ ] U-Net
- [ ] Attention U-Net
- [ ] Training pipeline
- [ ] Evaluation metrics

---

## Stage 4 — Transformer Architectures

- [ ] Swin Transformer
- [ ] SegFormer
- [ ] Mask2Former
- [ ] Multi-task learning

---

## Stage 5 — Astro-Flow-3D

- [ ] Physics-aware prediction heads
- [ ] Morphology representation learning
- [ ] Probabilistic reconstruction
- [ ] 3D morpho-spectral scene generation

---

# Development Philosophy

Astro-Flow-3D is designed as a modular research framework.

Each stage of the pipeline—from FITS ingestion to dataset creation and model training—is implemented as reusable, independently testable components. This design enables reproducibility, scalability to large JWST surveys, and straightforward experimentation with future architectures.
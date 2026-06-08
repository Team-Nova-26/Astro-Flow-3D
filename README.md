# Astro-Flow-3D

Astro-Flow-3D is a physics-aware deep learning framework for probabilistic morpho-spectral reconstruction of JWST deep-field observations.

## Current Phase

Stage 1: Data Infrastructure

## Objectives

* Download and inspect JWST CEERS observations
* Build multi-band aligned tensors
* Create PyTorch dataset pipeline
* Train baseline segmentation models
* Develop transformer-based multi-task architecture

## Repository Structure

src/

* data/
* models/
* training/
* utils/

scripts/
configs/
docker/
notebooks/

## Roadmap

* [ ] Infrastructure setup
* [ ] CEERS download pipeline
* [ ] FITS inspection
* [ ] Multi-band stacking
* [ ] Dataset creation
* [ ] Baseline UNet
* [ ] Swin Transformer backbone
* [ ] Mask2Former integration
* [ ] Physics heads
* [ ] Scene reconstruction

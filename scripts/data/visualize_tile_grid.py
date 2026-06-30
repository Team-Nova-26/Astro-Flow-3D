from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

TILE_DIR = Path("/data/astroflow/processed/tiles")
OUTPUT_FILE = "tile_grid.png"

tiles = sorted(TILE_DIR.glob("*.npy"))

print(f"Found {len(tiles)} tiles")

fig, axes = plt.subplots(4, 4, figsize=(10, 10))

for ax, tile_path in zip(axes.flat, tiles[:16]):
    image = np.load(tile_path)

    ax.imshow(
        image,
        cmap="gray",
        origin="lower",
        interpolation="nearest"
    )

    ax.set_title(tile_path.stem, fontsize=8)
    ax.axis("off")

plt.tight_layout()

plt.savefig(
    OUTPUT_FILE,
    dpi=300,
    bbox_inches="tight"
)

print(f"Saved {OUTPUT_FILE}")
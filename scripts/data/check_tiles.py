import numpy as np
from pathlib import Path

tiles = sorted(
    Path("/data/astroflow/processed/tiles")
    .glob("*.npy")
)

print("Tiles:", len(tiles))

for i in range(5):

    tile = np.load(tiles[i])

    print(
        f"Tile {i}",
        tile.shape,
        tile.min(),
        tile.max(),
        tile.mean()
    )
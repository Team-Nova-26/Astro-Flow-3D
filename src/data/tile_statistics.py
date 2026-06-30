from pathlib import Path

import numpy as np
import pandas as pd

TILE_DIR = Path("/data/astroflow/processed/tiles")
OUTPUT_CSV = Path("/data/astroflow/processed/index.csv")


def compute_statistics(tile_path: Path):
    tile = np.load(tile_path)

    return {
        "tile": tile_path.name,
        "mean": float(tile.mean()),
        "std": float(tile.std()),
        "min": float(tile.min()),
        "max": float(tile.max()),
        "median": float(np.median(tile)),
        "bright_pixels": int((tile > 0.8).sum()),
        "dark_pixels": int((tile < 0.05).sum()),
    }


def main():

    tile_files = sorted(TILE_DIR.glob("*.npy"))

    if len(tile_files) == 0:
        print("No tiles found.")
        return

    stats = []

    for tile in tile_files:
        record = compute_statistics(tile)
        stats.append(record)

    df = pd.DataFrame(stats)

    df.to_csv(OUTPUT_CSV, index=False)

    print("=" * 50)
    print(f"Processed : {len(df)} tiles")
    print(f"Saved CSV : {OUTPUT_CSV}")
    print("=" * 50)

    print(df.head())


if __name__ == "__main__":
    main()
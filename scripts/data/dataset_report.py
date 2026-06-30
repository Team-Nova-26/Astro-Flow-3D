from pathlib import Path

import pandas as pd

CSV = Path("/data/astroflow/processed/index.csv")


def main():

    df = pd.read_csv(CSV)

    print("=" * 60)
    print("JWST TILE DATASET REPORT")
    print("=" * 60)

    print(f"Tiles           : {len(df)}")
    print(f"Mean Brightness : {df['mean'].mean():.4f}")
    print(f"Mean Std        : {df['std'].mean():.4f}")

    print()

    print(f"Brightest Tile  : {df.loc[df['max'].idxmax(), 'tile']}")
    print(f"Darkest Tile    : {df.loc[df['mean'].idxmin(), 'tile']}")

    print()

    print(f"Average Bright Pixels : {df['bright_pixels'].mean():.2f}")
    print(f"Average Dark Pixels   : {df['dark_pixels'].mean():.2f}")

    print()

    print("Top 5 brightest tiles")

    print(
        df.sort_values(
            "mean",
            ascending=False
        )[["tile", "mean"]].head()
    )
    
    


if __name__ == "__main__":
    main()
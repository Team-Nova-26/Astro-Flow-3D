from pathlib import Path

import numpy as np


def generate_tiles(
    image: np.ndarray,
    output_dir,
    source_name: str,
    tile_size: int = 256,
    stride: int = 256,
):
    """
    Generate normalized tiles from a JWST image.

    Parameters
    ----------
    image : np.ndarray
        Normalized 2D image.

    output_dir : str | Path

    source_name : str
        FITS filename (without extension).

    tile_size : int

    stride : int

    Returns
    -------
    int
        Number of tiles generated.
    """

    output_dir = Path(output_dir)

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    count = 0

    height, width = image.shape

    for y in range(
        0,
        height - tile_size + 1,
        stride,
    ):

        for x in range(
            0,
            width - tile_size + 1,
            stride,
        ):

            tile = image[
                y:y + tile_size,
                x:x + tile_size,
            ]

            filename = (
                f"{source_name}"
                f"_tile"
                f"_x{x:05d}"
                f"_y{y:05d}"
                f"_s{tile_size}"
                ".npy"
            )

            np.save(
                output_dir / filename,
                tile.astype(np.float32),
            )

            count += 1

    return count
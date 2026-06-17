import numpy as np
from astropy.io import fits
from pathlib import Path

INPUT_FITS = (
    "downloads/mastDownload/JWST/"
    "jw01345003001_08201_00002_nrca2/"
    "jw01345003001_08201_00002_nrca2_i2d.fits"
)

TILE_SIZE = 256


def normalize(image):

    image = np.nan_to_num(image)

    p1 = np.percentile(image, 1)
    p99 = np.percentile(image, 99.8)

    image = np.clip(image, p1, p99)

    image = (
        image - image.min()
    ) / (
        image.max() - image.min()
    )

    return image.astype(np.float32)


def create_tiles(image, output_dir):

    count = 0

    h, w = image.shape

    for y in range(
        0,
        h - TILE_SIZE + 1,
        TILE_SIZE
    ):

        for x in range(
            0,
            w - TILE_SIZE + 1,
            TILE_SIZE
        ):

            tile = image[
                y:y + TILE_SIZE,
                x:x + TILE_SIZE
            ]

            filename = (
                output_dir /
                f"tile_{count:04d}.npy"
            )

            np.save(filename, tile)

            count += 1

    return count


def main():

    output_dir = Path(
        "/data/astroflow/processed/tiles"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"Saving tiles to: {output_dir}"
    )

    image = fits.open(
        INPUT_FITS
    )["SCI"].data

    print(
        f"Loaded image: {image.shape}"
    )

    image = normalize(image)

    total = create_tiles(
        image,
        output_dir
    )

    print(
        f"Generated {total} tiles"
    )


if __name__ == "__main__":
    main()
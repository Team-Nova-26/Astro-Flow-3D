from astropy.io import fits
import numpy as np


def load_fits(path):
    """
    Load JWST FITS file.
    """

    hdul = fits.open(path)

    print("\nHDU Structure\n")
    hdul.info()

    science = hdul["SCI"].data

    print("\nScience Shape:", science.shape)
    print("Datatype:", science.dtype)

    hdul.close()

    return science


if __name__ == "__main__":

    path = (
        "downloads/mastDownload/JWST/"
        "jw01345003001_08201_00002_nrca2/"
        "jw01345003001_08201_00002_nrca2_i2d.fits"
    )

    image = load_fits(path)

    print("\nMin:", np.nanmin(image))
    print("Max:", np.nanmax(image))
    print("Mean:", np.nanmean(image))
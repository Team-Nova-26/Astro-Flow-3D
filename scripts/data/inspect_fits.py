from astropy.io import fits

path = "downloads/mastDownload/JWST/jw01345003001_08201_00002_nrca2/jw01345003001_08201_00002_nrca2_i2d.fits"

hdul = fits.open(path)

print("\n===== HDU INFO =====\n")
hdul.info()

print("\n===== PRIMARY HEADER =====\n")
print(repr(hdul[0].header))

print("\n===== SCIENCE SHAPE =====\n")

for i, hdu in enumerate(hdul):
    if hasattr(hdu, "data") and hdu.data is not None:
        print(
            f"HDU {i}:",
            hdu.name,
            "Shape:",
            hdu.data.shape
        )

hdul.close()
from astropy.io import fits
from astropy.visualization import ImageNormalize, AsinhStretch
import matplotlib.pyplot as plt
import numpy as np

path = (
    "downloads/mastDownload/JWST/"
    "jw01345003001_08201_00002_nrca2/"
    "jw01345003001_08201_00002_nrca2_i2d.fits"
)

print("Loading FITS...")

image = fits.open(path)["SCI"].data.astype(np.float32)

image = np.nan_to_num(image)

print("Shape:", image.shape)
print("Min:", image.min())
print("Max:", image.max())
print("Mean:", image.mean())

# --------------------------
# 1. Raw Image
# --------------------------

plt.figure(figsize=(10, 10))
plt.imshow(image, origin="lower")
plt.colorbar()
plt.title("Raw Image")
plt.savefig("jwst_raw.png", dpi=300)
plt.close()

# --------------------------
# 2. Log Stretch
# --------------------------

plt.figure(figsize=(10, 10))
plt.imshow(
    np.log1p(np.maximum(image, 0)),
    origin="lower"
)
plt.colorbar()
plt.title("Log Stretch")
plt.savefig("jwst_log.png", dpi=300)
plt.close()

# --------------------------
# 3. Percentile Stretch
# --------------------------

vmin = np.percentile(image, 1)
vmax = np.percentile(image, 99.8)

plt.figure(figsize=(10, 10))
plt.imshow(
    image,
    origin="lower",
    vmin=vmin,
    vmax=vmax
)
plt.colorbar()
plt.title("Percentile Stretch (1-99.8%)")
plt.savefig("jwst_percentile.png", dpi=300)
plt.close()

# --------------------------
# 4. Astronomy Standard
# --------------------------

norm = ImageNormalize(
    image,
    stretch=AsinhStretch()
)

plt.figure(figsize=(10, 10))
plt.imshow(
    image,
    origin="lower",
    norm=norm
)
plt.colorbar()
plt.title("Asinh Stretch")
plt.savefig("jwst_asinh.png", dpi=300)
plt.close()

# --------------------------
# Histogram
# --------------------------

plt.figure(figsize=(10, 6))
plt.hist(
    image.flatten(),
    bins=200,
    log=True
)
plt.xlabel("Pixel Value")
plt.ylabel("Count")
plt.title("Pixel Distribution")
plt.savefig("jwst_histogram.png", dpi=300)
plt.close()

print("\nGenerated:")
print("  jwst_raw.png")
print("  jwst_log.png")
print("  jwst_percentile.png")
print("  jwst_asinh.png")
print("  jwst_histogram.png")
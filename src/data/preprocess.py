import numpy as np


def normalize_image(image):

    image = np.nan_to_num(image)

    p1 = np.percentile(image, 1)
    p99 = np.percentile(image, 99)

    image = np.clip(image, p1, p99)

    image = (image - image.min()) / (
        image.max() - image.min()
    )

    return image.astype(np.float32)
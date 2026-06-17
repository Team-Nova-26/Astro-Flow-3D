from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset


class JWSTDataset(Dataset):

    def __init__(self, tile_dir):

        self.files = sorted(
            Path(tile_dir).glob("*.npy")
        )

    def __len__(self):

        return len(self.files)

    def __getitem__(self, idx):

        image = np.load(
            self.files[idx]
        )

        image = torch.tensor(
            image,
            dtype=torch.float32
        )

        image = image.unsqueeze(0)

        return image
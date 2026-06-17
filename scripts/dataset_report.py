from src.data.jwst_dataset import JWSTDataset

dataset = JWSTDataset(
    "/data/astroflow/processed/tiles"
)

print("Tiles:", len(dataset))

sample = dataset[0]

print("Shape:", sample.shape)
print("Min:", sample.min().item())
print("Max:", sample.max().item())
print("Mean:", sample.mean().item())
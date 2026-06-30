import torch
import astropy
import astroquery

print("=" * 40)

print("PyTorch:", torch.__version__)
print("CUDA Available:", torch.cuda.is_available())
print("GPU Count:", torch.cuda.device_count())

print("Astropy:", astropy.__version__)
print("Astroquery:", astroquery.__version__)

print("=" * 40)
print("Environment OK")
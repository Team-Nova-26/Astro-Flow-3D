from astroquery.mast import Observations

print("Searching CEERS observations...")

obs = Observations.query_criteria(
    obs_collection="JWST"
)

print(obs[:5])
print(f"Total observations: {len(obs)}")
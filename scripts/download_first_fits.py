from astroquery.mast import Observations

obs = Observations.query_criteria(
    obs_collection="JWST",
    proposal_id="1345"
)

target_obs = obs[
    obs["obs_id"] == "jw01345-o003_t023_nircam_clear-f200w"
]

products = Observations.get_product_list(target_obs)

science_products = Observations.filter_products(
    products,
    productSubGroupDescription="I2D"
)

print(science_products["productFilename"])

manifest = Observations.download_products(
    science_products[:1],
    download_dir="/workspace/downloads"
)

print(manifest)
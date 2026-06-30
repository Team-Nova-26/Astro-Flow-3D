from astroquery.mast import Observations

obs = Observations.query_criteria(
    obs_collection="JWST",
    proposal_id="1345"
)

target_obs = obs[
    obs["obs_id"] == "jw01345-o003_t023_nircam_clear-f200w"
]

products = Observations.get_product_list(target_obs)

print("\nRelevant FITS files:\n")

for row in products:
    filename = row["productFilename"]

    if filename.endswith(".fits"):
        print(
            filename,
            "|",
            row["productSubGroupDescription"],
            "| calib:",
            row["calib_level"]
        )
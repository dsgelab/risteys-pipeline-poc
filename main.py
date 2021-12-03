from risteys_pipeline.log import logger
from risteys_pipeline.finregistry.load_data import load_finregistry_data
from risteys_pipeline.finregistry.preprocess_data import preprocess_finregistry_data

df = load_finregistry_data()
df = preprocess_finregistry_data(df)

logger.info("Done!")


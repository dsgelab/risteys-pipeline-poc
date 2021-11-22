"""Load FinRegistry data"""

import pandas as pd
from risteys_pipeline.config import finregistry_data_path

def load_finregistry_data():
    """Load FinRegistry csv data as a data frame"""
    df = pd.read_csv(finregistry_data_path, sep=",", header=0)
    return(df)

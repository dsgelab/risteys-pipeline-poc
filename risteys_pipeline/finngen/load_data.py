"""Load FinnGen data"""

import pandas as pd
from risteys_pipeline.config import finngen_data_path

def load_finngen_data():
    """Load FinnGen csv data as a data frame"""
    df = pd.read_csv(finngen_data_path, sep=",", header=0)
    return(df)

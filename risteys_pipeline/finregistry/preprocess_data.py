"""Preprocess FinRegistry data"""

import pandas as pd
import numpy as np

def preprocess_finregistry_data(df):
    """
    Pre-process FinRegistry data. Add a new column 'dead' to the data.

    Args:
        df (data frame): FinRegistry data frame from finregistry.load_data.py
    """
    df["dead"] = np.nan
    df.loc[df.status == 1, "dead"] = 0
    df.loc[df.status == 2, "dead"] = 1

    return(df)
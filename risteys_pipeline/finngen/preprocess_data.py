"""Preprocess FinnGen data"""

import pandas as pd
import numpy as np

def preprocess_finngen_data(df):
    """
    Apply the following preprocessing steps to the FinnGen data:
    - Drop columns with missing values 

    Args:
        df (data frame): FinnGen data frame from finngen.load_data.py
    """
    
    df = df.dropna(subset=["inst", "time", "status", "age", "sex", "ph.ecog", "ph.karno", "pat.karno", "meal.cal", "wt.loss"]).reset_index(drop=True)

    return(df)
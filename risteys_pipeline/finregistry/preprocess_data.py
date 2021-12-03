"""Preprocess FinRegistry data"""

import pandas as pd
import numpy as np

from risteys_pipeline.log import logger


def preprocess_finregistry_data(df):
    """
    Apply the following preprocessing steps to the FinRegistry data:
    - Drop columns with missing values 

    Args:
        df (data frame): FinRegistry data frame from finregistry.load_data.py
    """

    logger.debug("Preprocessing FinRegistry data")

    df = df.dropna(
        subset=[
            "inst",
            "time",
            "status",
            "age",
            "sex",
            "ph.ecog",
            "ph.karno",
            "pat.karno",
            "meal.cal",
            "wt.loss",
        ]
    ).reset_index(drop=True)

    return df


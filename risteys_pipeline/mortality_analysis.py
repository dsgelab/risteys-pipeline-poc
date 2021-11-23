"""Mortality analysis"""

import pandas as pd
from lifelines import CoxPHFitter

def mortality_analysis(df):
    """
    Implement mortality analysis and return a data frame of coefficients (betas) and their 95 % confidence intervals.

    Args:
        df (data frame): Preprocessed data from finngen.preprocess_data.py or finregistry.preprocess_data.py
    """

    df = df[["time", "age", "sex", "ph.ecog", "ph.karno", "pat.karno", "meal.cal", "wt.loss", "status"]]

    cph = CoxPHFitter()
    cph.fit(df, "time", event_col="status")
    
    res = pd.concat([cph.params_, cph.confidence_intervals_], axis=1)

    return(res)
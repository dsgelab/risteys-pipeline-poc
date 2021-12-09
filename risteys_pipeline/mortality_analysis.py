"""Mortality analysis"""

import pandas as pd
from lifelines import CoxPHFitter
from risteys_pipeline.log import logger


def mortality_analysis(df):
    """
    Implement mortality analysis and return a data frame of coefficients (betas) and their 95 % confidence intervals.

    Args:
        df (data frame): Preprocessed data from finngen.preprocess_data.py or finregistry.preprocess_data.py
    """

    logger.info("Mortality analysis started")

    df = df[["time", "age", "sex", "ph.ecog", "ph.karno",
             "pat.karno", "meal.cal", "wt.loss", "status"]]

    cph = CoxPHFitter()
    cph.fit(df, "time", event_col="status")

    res = pd.concat([cph.params_, cph.confidence_intervals_], axis=1)

    logger.info("Mortality analysis done")

    return(res)

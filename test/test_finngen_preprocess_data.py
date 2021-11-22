import pytest
from numpy import array
from risteys_pipeline.finngen.load_data import load_finngen_data
from risteys_pipeline.finngen.preprocess_data import * 

def test_preprocess_finngen_data():
    df = load_finngen_data()
    df = preprocess_finngen_data(df)
    expected_values = array([0, 1])
    observed_values = sorted(df["status"].unique())
    assert all(observed_values == expected_values)

import pytest
from risteys_pipeline.finngen.load_data import load_finngen_data

def test_load_finngen_data():
    expected_columns = ["inst", "time", "status", "age", "sex", "ph.ecog", "ph.karno", "pat.karno", "meal.cal", "wt.loss"]
    observed_columns = load_finngen_data().columns
    assert all(observed_columns == expected_columns)
    

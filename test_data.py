import pandas as pd
import pytest 

@pytest.fixture
def load_data():
    return pd.read_csv("dataset.csv")

def test_dimension(load_data):
    data = load_data
    assert data.shape == (1000, 9) ,"message"


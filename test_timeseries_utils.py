import pandas as pd
from timeseries_utils import monthly_climatology, anomaly


def test_monthly_climatology():
    temperature_data = pd.read_csv('temperature_data.csv', parse_dates=True, index_col=0)
    assert monthly_climatology(temperature_data).size == 12


def test_anomaly():
    temperature_data = pd.read_csv('temperature_data.csv', parse_dates=True, index_col=0)
    assert anomaly(temperature_data).size == 366

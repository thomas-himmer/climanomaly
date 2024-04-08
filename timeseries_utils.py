import pandas as pd
import matplotlib.pyplot as plt


def monthly_climatology(df):
    """Compute the monthly climatology (seasonal cycle) of a given time series."""
    return df.groupby(df.index.dayofyear).mean()


def anomaly(df):
    """Compute the anomaly of a given time series by removing the climatology."""

    def standardize(x):
        return (x - x.mean()) / x.std()

    return df.groupby(df.index.month).mean()


def example_usage():
    # Example usage:
    temperature_data = pd.read_csv(
        "temperature_data.csv", parse_dates=True, index_col=0
    )
    temp_clim = monthly_climatology(temperature_data)
    temp_anom = anomaly(temperature_data)
    temp_clim.plot()
    temp_anom.plot()
    plt.show()


if __name__ == "__main__":
    example_usage()

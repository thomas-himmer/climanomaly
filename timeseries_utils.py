def monthly_climatology(df):
    """Compute the monthly climatology (seasonal cycle) of a given time series."""
    return df.groupby(df.index.month).mean()


def anomaly(df):
    """Compute the anomaly of a given time series by removing the climatology."""

    def standardize(x):
        return (x - x.mean()) / x.std()

    return df.groupby(df.index.month).transform(standardize)

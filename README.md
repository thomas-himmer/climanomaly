# climanomaly

[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/thomas-himmer/climanomaly/blob/main/LICENSE)

This repository contains Python code for performing time series analysis, including computing monthly climatology and anomalies.

## Overview

The code provides two main functions:

1. `monthly_climatology(df)`: Computes the monthly climatology (seasonal cycle) of a given time series.
2. `anomaly(df)`: Computes the anomaly of a given time series by removing the climatology.

Additionally, an `example_usage()` function demonstrates how to use the provided functions to analyze temperature data.

## Dependencies

The code relies on the following Python libraries:
- pandas
- matplotlib

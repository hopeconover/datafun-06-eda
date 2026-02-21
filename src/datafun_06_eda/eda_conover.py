"""eda_conover.py - Project script.

Author: Hope Conover
Date: 2026-02


Purpose:
- Perform exploratory data analysis (EDA) on the housing dataset
- Practice key Python skills in a notebook environment

This file is written as a runnable script.

Data Source:
- Housing Prices Dataset
- Available from Kaggle: https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

Assumptions:
- The data contains columns like:
  price,area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,
  hotwaterheating,airconditioning,parking,prefarea,furnishingstatus


"""


# === Section 1a. Imports ===

# Imports at the top of the file
# REQ.EXTERNAL.DEPS: External packages must be defined in pyproject.toml
# REQ.EXTERNAL.DEPS.INSTALLED: External packages must be installed using uv sync
# REQ.EXTERNAL.DEPS.IMPORTED: External packages used must be imported here

import logging  # for type hinting only

from datafun_toolkit.logger import get_logger, log_header
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# === Section 1b. Configure Logger (once per file) ===

LOG: logging.Logger = get_logger("EDA", level="DEBUG")


# === Section 1c. Global Constants and Configuration ===

NUMERIC_COLS = ["price", "area", "bedrooms", "bathrooms", "stories"]

GROUP_COL = "furnishingstatus"

# Pandas display configuration (helps in notebooks)
pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)


# === Section 2. Load the Data ===


def load_data() -> pd.DataFrame:
    """Load housing data from CSV file."""
    LOG.info("Loading housing dataset from CSV")

    df = pd.read_csv("Housing.csv")

    LOG.info("Data loaded: %s rows, %s columns", df.shape[0], df.shape[1])
    return df


# === Section 3. Understand Data Shape and Basic Structure ===


def inspect_basic(df: pd.DataFrame) -> None:
    """Inspect basic structure of the dataset.

    This step answers:
    - What columns exist?
    - What types are they?
    - How large is the dataset?
    """
    LOG.info("Inspecting first rows of data")
    LOG.debug("\n%s", df.head())

    LOG.info("Column names")
    LOG.debug("%s", list(df.columns))

    LOG.info("DataFrame info (types and non-null counts)")
    df.info()

    LOG.info("Dataset shape: %s rows, %s columns", df.shape[0], df.shape[1])


# === Section 4. Check for Missing Data ===


def build_data_dictionary(df: pd.DataFrame) -> pd.DataFrame:
    """Build a starter data dictionary.

    Includes:
    - column name
    - data type
    - missing value count
    - percent missing
    """
    LOG.info("Building starter data dictionary")

    data_dictionary = pd.DataFrame(
        {
            "column": df.columns,
            "dtype": [str(t) for t in df.dtypes],
            "missing_count": df.isna().sum().values,
            "missing_pct": (df.isna().mean() * 100).round(2).values,
        }
    )

    LOG.debug("\n%s", data_dictionary)
    return data_dictionary


def check_quality(df: pd.DataFrame) -> None:
    """Perform basic data quality checks.

    Checks include:
    - Missing values
    - Duplicate rows
    - Basic numeric sanity checks
    """
    LOG.info("Checking missing values per column")
    LOG.debug("\n%s", df.isna().sum().sort_values(ascending=False))

    dup_count = int(df.duplicated().sum())
    LOG.info("Duplicate rows detected: %s", dup_count)

    LOG.info("Basic sanity check for numeric columns")
    LOG.debug("\n%s", df[NUMERIC_COLS].describe())


# === Section 5. Optional Cleaning Step (EDA View) ===


def make_clean_view(df: pd.DataFrame) -> pd.DataFrame:
    """Create a cleaned view for EDA.

    Strategy:
    - Keep the original DataFrame unchanged
    - Drop rows missing key numeric fields and grouping field
    """
    LOG.info("Creating cleaned view for EDA (dropping rows with key missing values)")
    df_clean = df.dropna(subset=NUMERIC_COLS + [GROUP_COL]).copy()
    LOG.info(
        "Cleaned view shape: %s rows, %s columns", df_clean.shape[0], df_clean.shape[1]
    )
    return df_clean


# === Section 6. Descriptive Statistics ===


def descriptive_stats(df_clean: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Compute descriptive statistics overall and by group."""

    LOG.info("Computing overall descriptive statistics")
    stats_overall = df_clean[NUMERIC_COLS].describe().T
    LOG.debug("\n%s", stats_overall)

    LOG.info("Computing descriptive statistics by %s", GROUP_COL)
    stats_by_group = df_clean.groupby(GROUP_COL)[NUMERIC_COLS].agg(
        ["count", "mean", "std", "min", "max"]
    )
    LOG.debug("\n%s", stats_by_group)

    return stats_overall, stats_by_group


# === Section 7. Simple Correlations (Numeric Only) ===


def correlation_matrix(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Compute a numeric correlation matrix.

    Args:
        df_clean (pd.DataFrame): Cleaned DataFrame for analysis.

    Returns:
        pd.DataFrame: Correlation matrix of numeric columns.

    Notes:
    - Correlation matrices help identify relationships between numeric variables.
    - Values range from -1 (perfect negative) to +1 (perfect positive).
    """
    LOG.info("Computing correlation matrix for numeric columns")
    corr = df_clean[NUMERIC_COLS].corr()
    LOG.debug("\n%s", corr)
    return corr


# === Section 8. Create a Seaborn Scatter Plot ===


def make_plots(df_clean: pd.DataFrame) -> None:
    """Create simple EDA plots for housing dataset."""
    LOG.info("Creating scatter plot: area vs price")

    scatter_plt: Axes = sns.scatterplot(
        data=df_clean,
        x="area",
        y="price",
        hue=GROUP_COL,
    )
    scatter_plt.set_xlabel("Area")
    scatter_plt.set_ylabel("Price")
    scatter_plt.set_title("Area vs Price (by Furnishing Status)")

    plt.figure()

    sns.boxplot(
        data=df_clean,
        x=GROUP_COL,
        y="price",
    )
    plt.title("Price Distribution by Furnishing Status")

    plt.show()


# === Section LAST. Reminder: Run All before sending to GitHub ===


def main() -> None:
    """Main function to run the EDA workflow."""
    log_header(LOG, "Exploratory Data Analysis (EDA) - Housing Prices")

    LOG.info("Section 1: Setup at the top of the file")

    LOG.info("Section 2: Load the data")
    df = load_data()

    LOG.info("Section 3: Inspect data shape and basic structure")
    inspect_basic(df)

    LOG.info("Section 4: Check data quality")
    build_data_dictionary(df)
    check_quality(df)

    LOG.info("Section 5: Create a cleaned view for EDA")
    df_clean = make_clean_view(df)

    LOG.info("Section 6: Compute descriptive statistics for numeric columns")
    descriptive_stats(df_clean)

    LOG.info("Section 7: Show correlation matrix for numeric columns")
    correlation_matrix(df_clean)

    LOG.info("Section 8: Make plots")
    make_plots(df_clean)

    LOG.info("EDA workflow complete")
    LOG.info("IMPORTANT: This script creates chart windows.")
    LOG.info(
        "Close any chart windows and terminate this process with CTRL+c as needed."
    )


if __name__ == "__main__":
    main()

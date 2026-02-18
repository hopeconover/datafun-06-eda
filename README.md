# datafun-06-eda

## Project 6 EDA Notebook

## Overview

Project 6 is an opportunity to create your own custom
exploratory data analysis (EDA) project using
GitHub, Git, Jupyter, pandas, Seaborn and other popular data analytics tools.

## Objective

Perform and publish a custom EDA project to demonstrate skills with popular tools for data analytics.
The notebook should tell a data story and visually present findings
in a clear and engaging manner.

## Explore Datasets

Choose a dataset for analysis.
You will want a known, clean dataset.
Cleaning data can run 60-80% of the project (or more) - you don't need to
demonstrate cleaning skills for this project.

## Selected Dataset

Data Description: Housing Prices
Dataset Source: Kaggle - Housing Prices Dataset
Download Housing.csv from: <https://www.kaggle.com/datasets/yasserh/housing-prices-dataset?resource=download>

## Dataset Overview

This dataset contains information regarding housing prices and various attributes that influence the cost of a home, such as area, number of rooms, and available amenities.

Row Count: 545
Column Count: 13

## Why this Dataset?

I chose this dataset for my EDA because it provides a mix of numerical data (area, price) and categorical data (furnishing status, air conditioning). This allows for a diverse range of visualizations, such as scatter plots to show the relationship between area and price, and box plots to show how amenities like air conditioning impact the median home value.

## Requirements

### 1. Create and Manage Project Virtual Environment

This project uses external packages, which are not included in the Python Standard Library - we must install them.
To keep our project separate from all other Python projects,
we will create and manage a local project virtual environment and install our packages into the local project virtual environment.

- NEWER: [pro-analytics-02](https://denisecase.github.io/pro-analytics-02/) uses `uv` and `pyproject.toml` for dependencies (RECOMMENDED).
  OLDER: pro-analytics-01 used `pip` and `venv` and `requirements.txt` for dependencies

Both approaches work.
You can almost always use whichever approach you like best - the project results should be exactly the same.

### 2. Start a new EDA Notebook

Document the process and commands you use in your README.md.

Copy/paste and edit a new notebook to hold your custom analysis.

### 3.  Perform Exploratory Data Analysis

Perform a unique exploratory data analysis project using the tools and skills covered previously.

Present your notebook with an opening that introduces yourself and your topic.
Use Markdown section headings to introduce each step.
Interpret the visualizations and statistics to narrate a clear and compelling data story.
Present your findings in a logical and engaging manner.

## Notebook Execution

Run your notebook entirely to ensure it executes without errors.
This includes checking all code cells and ensuring all data visualizations render as expected.
Confirm that your notebook renders correctly on GitHub after pushing, as this ensures your work is viewable by others.

## Resources

- See [datafun-04-notebooks](https://github.com/hopeconover/datafun-04-notebooks) for a guided EDA.

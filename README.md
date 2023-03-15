# Pre Owned Car Price Calculator

## Overview
Predice or Calculate(in real world) the price of used car using parameters such as age, kilo meter run, brand etc... 

Deployed Web App Link: https://praathapj-usedcarpricecalc-carprice-calc-us1aa6.streamlit.app/

## Data Collection
Real world Data is obtained from kaggle website provided by CAR DEKHO company which is entering in used car market. (https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)

## Data Cleaning and Preprocessing
Data had multiple files with multiple features, hence considering a file with adequate features and concat the other data.

Missing values in new files of specific car models are imputed based on the simialr Car Model already present.

Extreame outliers are removed, such as very high selling price or very few model counts.

## Exploratory Data Analysis
Univariant, bivariant and multivarinat analysis

## Feature Engineering and Selection

Modifying numerical features such as number of seats to category since its not ordinal data.

Obtaing Age from Year(Purchased) feature considering 2022 and not 2023 since data was uploaded in 2022.

For encoding Car Variant feature was skipped because too many variants to encode, hence engine, power, milege is used which is not usually used to calculate price because engine power and milege change as variant changes.

## Modelling
Polynomial relation with each independent and dependent feature with multi colinearity with few independent features hence Random Forest Regression with random search CV.

## Model Evaluation
Regular RMSE and R2 used for regression and not more than 50 thound difference in predicted price.

## Improvement
More used cars data in each variant and in each price range.

Using CatBoost model with all the variants will reduce error drastically.


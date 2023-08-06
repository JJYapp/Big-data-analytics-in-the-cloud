# ============================== Columns Reduction ============================== #

# Data can be retrieved from https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml?select=HI-Medium_Trans.csv
# Download and save it in your local machine
# Change the pathways below accordingly
# Copy starts from line 8

# Import necessary libraries for data manipulating
import pandas as pd

# Read data
df = pd.read_csv(r"C:\Users\USER\Desktop\Big Data Analytics in the Cloud\Assignment\Assignment 1\HI-Medium_Trans.csv")

# Retain only the specified columns, exclude the remaining columns
df_reduced = df[['Timestamp', 'To Bank', 'Amount Received', 'Receiving Currency', 'Payment Format']]

# Output the reduced data
df_reduced.to_csv(r"C:\Users\USER\Desktop\Big Data Analytics in the Cloud\Assignment\Assignment 1\HI-Medium_Trans_reduced.csv", index=False)

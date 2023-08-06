# ============================== Analysis (Visualization) ============================== #

# Please change the following pathways accordingly
# Copy starts from line 6

# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df_reduced = pd.read_csv(r"C:\Users\USER\Desktop\Big Data Analytics in the Cloud\Assignment\Assignment 1\HI-Medium_Trans_reduced.csv")

# Compute descriptive statistics grouped by Bank
stats = df_reduced.groupby(['To Bank']).agg({'Amount Received': ['sum', 'count', 'mean']})

# Adjust the data structure
stats.reset_index(inplace=True)
stats = stats.droplevel(1, axis=1)
stats.columns.values[:] = ['Bank', 'Total Amount', 'Number of Transactions', 'Average Amount']
stats['Bank'] = stats['Bank'].astype('string')


## Visualization - Total Amount Received
# Top 20 Banks by Total Amount Received
top_20_banks = stats.sort_values(by = 'Total Amount', ascending = False).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x='Bank', y='Total Amount', data=top_20_banks)
plt.title('Top 20 Banks by Total Amount Received')
plt.xlabel('Bank')
plt.ylabel('Total Amount Received')
plt.xticks(rotation=45)
plt.show()

# Last 20 Banks by Total Amount Received
last_20_banks = stats.sort_values(by = 'Total Amount', ascending = True).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x='Bank', y='Total Amount', data=last_20_banks)
plt.title('Last 20 Banks by Total Amount Received')
plt.xlabel('Bank')
plt.ylabel('Total Amount Received')
plt.xticks(rotation=45)
plt.show()


## Visualization - Number of Transactions
# Top 20 Banks by Number of Transactions
top_20_banks = stats.sort_values(by = 'Number of Transactions', ascending = False).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x='Bank', y='Number of Transactions', data=top_20_banks)
plt.title('Top 20 Banks by Number of Transactions')
plt.xlabel('Bank')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.show()

# Last 20 Banks by Number of Transactions
last_20_banks = stats.sort_values(by = 'Number of Transactions', ascending = True).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x='Bank', y='Number of Transactions', data=last_20_banks)
plt.title('Last 20 Banks by Number of Transactions')
plt.xlabel('Bank')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.show()


## Visualization - Average Amount Received
# Top 20 Banks by Average Amount Received
top_20_banks = stats.sort_values(by = 'Average Amount', ascending = False).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x='Bank', y='Average Amount', data=top_20_banks)
plt.title('Top 20 Banks by Average Amount Received')
plt.xlabel('Bank')
plt.ylabel('Average Amount Received')
plt.xticks(rotation=45)
plt.show()

# Last 20 Banks by Average Amount Received
last_20_banks = stats.sort_values(by = 'Average Amount', ascending = True).head(20)

plt.figure(figsize=(12, 6))
sns.barplot(x='Bank', y='Average Amount', data=last_20_banks)
plt.title('Last 20 Banks by Average Amount Received')
plt.xlabel('Bank')
plt.ylabel('Average Amount Received')
plt.xticks(rotation=45)
plt.show()
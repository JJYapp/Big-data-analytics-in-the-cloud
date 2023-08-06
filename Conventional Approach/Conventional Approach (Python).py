# ============================== Conventional Approach (Python) ============================== #

# Please change the following pathways accordingly

# Import necessary libraries
import pandas as pd
import time

# Stating the start of the programme & record start time
print('start')
start_time = time.time()

# Read data
df = pd.read_csv(r'/home/hadoop/JJ/HI-Medium_Trans_reduced.csv')

# Print time usaed for reading data
read_time = time.time()
print("--- Data reading time ---")
print("--- %s seconds ---" % (read_time - start_time))

# Compute descriptive statistics grouped by Bank
receive = df.groupby(['To Bank']).agg({'Amount Received': ['sum', 'count', 'mean']})

# Adjust the data structure
receive.reset_index(inplace=True)
receive = receive.droplevel(1, axis=1)
receive.columns.values[:] = ['Bank', 'Total Amount', 'Number of Transaction', 'Average Amount']

# Print time used for computing descriptive statistics
aggregation_time = time.time()
print('--- Aggregation time ---')
print("--- %s seconds ---" % (aggregation_time - read_time))

# Output descriptive statistics data & print time used for outputing
receive.to_csv(r'/home/hadoop/JJ/aggregated_output.csv', index=False)
print('--- Data output time ---')
print("--- %s seconds ---" % (time.time() - aggregation_time))

# Print total used time for entire programme
used_time = time.time() - start_time
print('--- Total ---')
print("--- %s seconds ---" % (used_time))
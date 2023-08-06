# ============================== MapReduce Approach (Reducer) ============================== #

# Please change the following pathways accordingly
# Copy starts from line 6

#!/usr/bin/python3

import sys

current_key = None
total_amount_received = 0
count = 0

for line in sys.stdin:
    # Extact key and values from Mapper's output
    to_bank, amount_received, count_per_currency = line.strip().split('\t')
    amount_received = float(amount_received)
    count_per_currency = int(count_per_currency)

    # If it is the first input
    if current_key is None:
        current_key = to_bank
    # If the current_key (Bank) has changed
    if current_key != to_bank:
        # Calculate average and output the result
        average_amount_received = total_amount_received / count
        print(f"{current_key}\t{total_amount_received}\t{count}\t{average_amount_received}")
        # Accumulate amount_received and count for new current_key (Bank)
        current_key = to_bank
        total_amount_received = amount_received
        count = count_per_currency
    # If the current_key (Bank) has not changed
    else:
        # Accumulate amount_received and count
        total_amount_received += amount_received
        count += count_per_currency

# If it is the last input
if current_key is not None:
    # Calculate average and output the result
    average_amount_received = total_amount_received / count
    print(f"{current_key}\t{total_amount_received}\t{count}\t{average_amount_received}")
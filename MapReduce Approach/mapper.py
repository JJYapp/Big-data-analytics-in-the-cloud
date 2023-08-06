# ============================== MapReduce Approach (Mapper) ============================== #

# Please change the following pathways accordingly
# Copy starts from line 6

#!/usr/bin/python3

import sys

for line in sys.stdin:
    # Skip the header line
    if not line.startswith('Timestamp'):
        # Extract bank and amount received data only
        data = line.strip().split(',')
        to_bank = data[1]
        amount_received = float(data[2])
        print(f"{to_bank}\t{amount_received}\t1") #Append 1 for counting
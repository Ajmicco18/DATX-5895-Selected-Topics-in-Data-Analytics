import socket
print(socket.gethostname())

import pandas as pd
df = pd.read_csv('/anvil/projects/tdm/data/flights/subset/1991.csv')
df[df["Month"]==12].head() # see information about a few of the flights from December 1991

#Calculate memory in bytes in Anvil sub-cluster A (Python)
256000*1000000000

#Calculate memory in TB in Anvil sub-cluster A (Python)
256000/1000
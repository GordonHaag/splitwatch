from splitwatch import SplitWatch
import time
import random

# Create SplitWatch object w, with mode set to 'dev'.
# 'dev' mode causes collection of data. If mode = '' or
# the mode arguement is absent, no data is collected and
# calls to SplitWatch have no output and  virtually no overhead.
w = SplitWatch(mode = 'dev')

w.split('First section to benchmark') # First call to SplitWatch.split() leads to the start of a timer tagged with the argument desc.
time.sleep(random.random()) # A bit of long running code

w.split('Second section to benchmark')
time.sleep(random.random())  # Another bit of slow code

w.dump()
from splitwatch import SplitWatch
import time
import random

w = SplitWatch(mode = 'dev')

w.split('first test')
time.sleep(random.random())
w.split('second test')
time.sleep(random.random())
w.dump()
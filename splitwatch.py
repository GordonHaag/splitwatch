import time

class SplitWatch(object):
    def __init__(self, mode = '', sorted = False):
        if mode == 'dev':
            self.init = time.time()
            self.start = None
            self.stop = None
            self.times = []
            self.desc = ''
            self.mode = mode
        elif mode == '':
            self.mode = mode

    def split(self, desc = ''):
        if self.mode == 'dev':
            if self.start == None: # First split
                self.start = time.time()
                self.desc = desc
            else:
                self.times.append((self.desc, time.time()-self.start))
                self.start = time.time()
                self.desc = desc
        else: pass

    def dump(self):
        if self.mode == 'dev':
            self.split()
            longest = max(map(len, [r[0] for r in self.times]))
            if sorted == True:
                self.times.sort(key = lambda x : x[0])
            for each in self.times:
                print each[0].ljust(longest + 1)+': ' +str(each[1]) + 's'
        else: pass

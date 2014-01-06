import time

class SplitWatch(object):
	def __init__(self, mode = ''):
		if mode == 'dev':
			self.init = time.time()
			self.start = None
			self.stop = None
			self.times = []
			self.desc = ''
		elif mode == '':
			pass

	def split(self, desc = ''):
		if self.start == None: # First split
			self.start = time.time()
			self.desc = desc
		else:
			self.times.append((desc, time.time()-self.start))
			self.start = time.time()

	def dump(self):
		longest = max[map(len, [r[0] for r in self.times])]
		for each in self.times:
			print each[0].ljust(longest)+': ' +str(each[1]) 


import sys,string
class ShortURL:

	def getShortURL(self,url):
		#Step 1: Clean the url

		#Step 2: Get Base-10 value
		Base10Value = self.getBase10Value(url)
		#Step 3: Get Base 62 value
		shortUrl = self.getBase62Value(Base10Value)

		return shortUrl

	def getBase10Value(self,url):
		return sum([ord(char) for char in url])

	def getBase62Value(self,URLBase10Value):
		list = []
		Base62 = self.populate()
		while True:
			dividend = URLBase10Value/62
			remainder = URLBase10Value%62
			URLBase10Value = remainder
			if(dividend>0):
				list.append(Base62[dividend])
			else:
				list.append(Base62[remainder])
				break
		return ''.join(list)

	def populate(self):
		Base62 = []
		# 0-9
		for i in range(0,10):
			Base62.append(i)
		# a-z
		for i in range(97,123):
			Base62.append(chr(i))

		# A-Z
		for i in range(65,91):
			Base62.append(chr(i))

		return Base62	


	def __init__(self):
		#print "Starting..."
		#Url = "http://www.google.com"
		Url = sys.argv[1]
		ShortURL = self.getShortURL(Url)
		print ShortURL
		#print "End."

CreateShortURL = ShortURL()



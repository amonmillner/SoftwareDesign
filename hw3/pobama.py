# API call business
# API key bSJDOQnZGZxXHSpHjCTnh1Oxf

import time

query = str(raw_input("enter search query: "))

def search(query):

	from pattern.web import Twitter

	t = Twitter()
	i = None
	for j in range(3):
		for tweet in t.search(query, start = i, count = 10):
			print tweet
			# print tweet.text
			print 
			i = tweet.id


search(query);


# def stream():
# 	print "hello world"

# 	from pattern.web import Twitter

# 	s = Twitter().stream('#fail')
# 	for i in range(10):
# 		time.sleep(1) 
# 		s.update(bytes=1024)
# 		print s[-1].text if s else ''

# stream()
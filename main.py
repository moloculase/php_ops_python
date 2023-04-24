#null coalescing
def qq(a, b, c=None):
	if a == c:
		return b
	return a

#simple spaceship
def ss(a, b):
	if a < b:
		return -1
	elif a > b:
		return 1
	elif a == a:
		return 0
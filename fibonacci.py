def fibonacci(n):
	x1 = 0
	x2 = 1
	while x1 <= n:
		aux = x2
		print x1,
		x2 = x1 + x2
		x1 = aux
		
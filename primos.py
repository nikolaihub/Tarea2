def primos(n):
	if n > 1:
		lista = range(2,n+1)
		for prime in lista:
			for num in lista:
				if num != prime and num % prime == 0:
					lista.remove(num)
		print lista

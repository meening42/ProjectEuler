def find_prime_factors(n):
	remaining = n
	primefactors = []
	while(remaining != 1):
		if primefactors == []:
			i=1
		else:
			i=primefactors[len(primefactors)-1]-1
		while i < remaining:
			i+=1
			if remaining%i == 0:
				remaining = remaining/i
				primefactors.append(i) 
				break
	return primefactors


print(find_prime_factors(100))


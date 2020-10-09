def swap_unique_keys_values(n):
	d = {}
	for i in n:
		if not n[i] in d:
			d[n[i]] = i
		else:
			del d[n[i]]
	return d

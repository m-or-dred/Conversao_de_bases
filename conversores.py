
def a_to_ten(val, base):
	if base == 1:
		return len(val)
	res = 0
	for i, char in enumerate(val):
		if char.isdigit():
			res += int(char) * base ** (len(val)-1-i)
		else:
			res += (ord(char)-87) * base ** (len(val)-1-i)
	return res

def ten_to_b(val, base):
	if base == 1:
		return '|' * val
	quot = val // base
	rest = val % base
	res = str(rest) if 10 > rest else chr(rest + 87)
	while quot:
		rest = quot % base
		res = str(rest) + res if 10 > rest else chr(rest + 87) + res
		quot //= base
	return res


print(a_to_ten('0111100', 2)-128)

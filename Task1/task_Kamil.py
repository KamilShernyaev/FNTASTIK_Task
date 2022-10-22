_str = input().lower()

res = ""
for char in _str:
	if _str.count(char) == 1:
		res += "("
	else:
		res += ")"

print(res)

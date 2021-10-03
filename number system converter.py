num_to_char = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
char_to_num = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
num = input("Number = ")
input_base = int(input("Base = "))
target_base = int(input("Target base = "))
integer = 0
decimal = 0
for i in num:
	if i == '.':
		for k in reversed(num):
			if k == '.':
				break
			else:
				decimal = (decimal + char_to_num[k]) * input_base ** (- 1)
		break
	else:
		integer = (integer + char_to_num[i]) * input_base
integer /= input_base
out = ""
while integer != 0:
	out = num_to_char[integer % target_base] + out
	integer /= target_base
	integer = int(integer)
print(out, end = '.')
while decimal != 0:
	decimal *= target_base
	print(num_to_char[int(decimal)], end = '')
	decimal %= 1
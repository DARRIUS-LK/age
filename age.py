a = input('have you drive before? (yes/no): ')
if a != 'yes' and 'no':
	print('please enter yes or no only')
	raise SystemExit
b = input('please enter your age: ')
def is_number(b):
		try: 
			int(b)
			return True
		except ValueError:
			pass

if is_number(b) == True:
	b = int(b)
	if a == 'yes'and b >= 18:
		print('you passed the test')
	elif a == 'no' and b >= 18:
		print('you passed the test')
	elif a == 'yes' and b < 18:
		print('you failed the test')
	elif a == 'no' and b < 18:
		print('you passed the test')
else:
	print('Please input the number for your age info! ')
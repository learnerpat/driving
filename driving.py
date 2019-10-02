country = input("where are you from? ")
country = country.upper()
age = input("how old are you? ")
age=int(age)
if country == 'CHINA':
	if age >= 18:
		print("You can take a licence after the driving exam.")
	else:
		print("You can't take a licence cause your age.")
elif country == 'UNITED STATES':
	if age >= 16:
		print("You can take a licence after the driving exam.")
	else:
		print("You can't take a licence cause your age.")

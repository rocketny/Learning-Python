semi_annual_raise = 0.07
r = 0.04 # annually
total_cost = 1000000
portion_down_payment = 0.25
needed_cost = total_cost * portion_down_payment

annual_salary = float(input("Enter the starting salary: "))

def testM(annual_salary):
	month_salary_start = annual_salary / 12.0
	# first let's see if it is impossible to save enough money in 36 months.
	c_s = 0
	for i in range(1,37):
		c_s = c_s * (1+(r/12.0)) + month_salary_start * (1+semi_annual_raise)**(i//6)
	if c_s < needed_cost:
		print("It is not possible to pay the down payment in three years.")
	else:
		low = 0
		high = 10000
		ans = (low+high)//2
		numGuesses = 0
		while True:
			current_saving = 0
			for i in range(1,37):
				monthly_saving = month_salary_start * (1+semi_annual_raise)**(i//6) * (ans /10000.0)
				current_saving = current_saving * (1+(r/12.0)) + monthly_saving
			numGuesses += 1
			if abs(current_saving - needed_cost) <= 100:
				break
			
			if current_saving < needed_cost:
				low = ans
			elif current_saving > needed_cost:
				high = ans
			ans = (low+high)//2
		print("Best savings rate:", ans/10000)
		print("Steps in bisection search",numGuesses)

testM(annual_salary)

annual_salary = float(input("Enter your annual salary: "))
month_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, \
as a decimal: "))
monthly_saving = annual_salary / 12 * portion_saved


total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
needed_cost = total_cost * portion_down_payment

current_saving = 0.0
r = 0.04


t = 0
while current_saving < needed_cost:
    current_saving = current_saving*(1+r/12) +  monthly_saving
    t = t + 1

print("Number of months: ", t)

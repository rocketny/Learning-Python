"""
I think my script is good, However the result just didn't match perfectly 
with the pdf downloaded from the 600's course site.
I think the approximation is the reason why the difference happen, but 
not for sure. If you know the reason plz let me contact me.
"""


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, \
as a decimal: "))
                    


total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
needed_cost = total_cost * portion_down_payment

semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

current_saving = 0.0
r = 0.04


month_salary_start = annual_salary / 12

t = 0
while current_saving < needed_cost:
    month_salary = month_salary_start * (1+semi_annual_raise)**((t+1)//6)
    current_saving = current_saving*(1+r/12) + month_salary * portion_saved 
    t += 1
    

print("Number of months: ", t)
